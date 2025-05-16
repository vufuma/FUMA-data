# Purpose: 
- Documenting how reference panels were created in FUMA (the files located in `/data/1KG/Phase3`)

```
├── AFR
├── ALL
├── AMR
├── EAS
├── EUR
├── SAS
```

- Content inside each pop directory: 
```
{pop}.chr*.ld.gz
{pop}.chr*.ld.gz.tbi
{pop}.chr*.rsID.gz
{pop}.chr*.rsID.gz.tbi
{pop}.chr*.frq.gz
{pop}.chr*.frq.gz.tbi
```

## Reproducing `{pop}.chr*.rsID.gz`
```
pwd; date
/home/tphung/tphung_proj/projects/fuma/jira_FUMA_96/reproduce_1000g_refs
Tue May 13 11:00:52 AM CEST 2025
```

- Download 
```
wget https://ftp.1000genomes.ebi.ac.uk/vol1/ftp/release/20130502/ALL.chr21.phase3_shapeit2_mvncall_integrated_v5b.20130502.genotypes.vcf.gz
```

- `Multi allelic SNPs were first split into separate columns using vcfmulti2oneallele.jar from JVARKIT (http://lindenb.github.io/jvarkit/). `
    - I downloaded the pre-compiled jar archive for JVARKIT from: https://uncloud.univ-nantes.fr/index.php/s/4sL77oWR2BFzSBH
    - Copied to snellius: `/gpfs/home6/tphung/software/jvarkit.jar`
    - Run: 
    ```
    java -jar jvarkit.jar vcfmulti2oneallele ~/tphung_proj/projects/fuma/jira_FUMA_96/reproduce_1000g_refs/ALL.chr21.phase3_shapeit2_mvncall_integrated_v5b.20130502.genotypes.vcf.gz > ~/tphung_proj/projects/fuma/jira_FUMA_96/reproduce_1000g_refs/chr21_splitmultiallelicsnps.vcf.gz
    ```

- `VCF files were then converted to PLINK bfile (PLINK v1.9). `
```
 ~/software/plink_program/plink --vcf chr21_splitmultiallelicsnps.vcf.gz --out chr
21_splitmultiallelicsnps
```

- Modify the output `.bim` files so that it contains the unique ID in order to use the flag `--extract`

```
mv chr21_splitmultiallelicsnps.bim chr21_splitmultiallelicsnps.bim.orig
python add_uniqueID_bim.py -b chr21_splitmultiallelicsnps.bim.orig -o chr21_splitmultiallelicsnps.bim
```

```
python create_include_snps.py --bim chr21_splitmultiallelicsnps.bim.orig --out chr21_kept_snps.txt
```

```
~/software/plink_program/plink --bfile chr21_splitmultiallelicsnps --extract chr21_kept_snps.txt --maf 0.00000000001 --out chr21_splitmultiallelicsnps_filtered --make-bed
```
**Notes: ** instead of using a very low value for maf threshold, I should compute freq (`~/software/plink_program/plink -bfile chr21_splitmultiallelicsnps --freq`) and then update the file `chr21_kept_snps.txt`.

```
cat chr21_splitmultiallelicsnps_filtered.bim | wc -l
1105982

zless ALL.chr21.rsID.gz | wc -l
1105982
```

### Documenting issues/problems with rsID in FUMA currently
- One of the "reference" files used in FUMA is `1KG/Phase2/{pop}.chr${i}.rsID.gz`. This is how the file looks like:
```
21      24930699        21:24930699:A:T rs9989944
21      24930714        21:24930714:A:G rs9989942
21      24930718        21:24930718:A:G rs113275176
21      24930723        21:24930723:A:T rs546961150
21      24930738        21:24930738:C:T rs566916315
```
- The unique ID from this file (`chr:pos:allele1:allele2`) is obtained from 1000 genomes VCF files. I can replicate this. 
- The VCF files from 1000 genomes did not include rsID. I suspect that it was obtained from dbSNP version 146 (location on FUMA: `/data/dbSNP/`)
- For chr21, there are `1,105,982` variants in the file `1KG/Phase2/ALL.chr21.rsID.gz`
    - 137 variants did not have a match with dbSNP146
21      46572182        21:46572182:G:GTCTGCTGTGGGAGATTTGTTTCCCTAGAAGATTCACGGCTGTCGTTCTCTCCCC   esv3647144

- rsID reported in FUMA does not match with gnomad
chr21:38406362
variant: 21:38406362:G:GTATATATATAGTGTATATATAGTGTATATATAG
fuma rsID rs534247948

At 21:38406362, 2 variants are found in dbSNP146:
```
21      38406362        rs559922945     G       C
21      38406362        rs773453784     GTA     G
```
Using rs534247948 to search on gnomad (GRCh37): https://gnomad.broadinstitute.org/variant/rs534247948?dataset=gnomad_r2_1

Multiple matching variants found:

21-38406362-GTA-G
21-38406362-GTATA-G

- Some variants have an rsID in FUMA but they are not found both in dbSNP146 or gnomad. For example: 
fuma rsid: `21      9863664 21:9863664:G:T  rs426010`
variant `21:9863664` does not exist in dbSNP
rs426010 does not exist on gnomad

- For variants where chr:pos has multiple rsID in dbSNP146, the rsID is picked seemingly at random
```
21      26551624        rs772700312     G       GA
21      26551624        rs369723461     GA      G
21      26551624        rs11364549      GA      G
21      26551624        rs397971706     G       GA
```

These 4 are the same because sorted(allele1, allele2) are used in FUMA
This variant `21:26551624:G:GA` is given rs369723461 in FUMA

## Reproducing `{pop}.chr*.frq.gz`
```
~/software/plink_program/plink -bfile chr21_splitmultiallelicsnps_filtered --freq --out chr21_splitmultiallelicsnps_filtered_maf
```

## Reproducing `{pop}.chr*.ld.gz`
```
/gpfs/home6/tphung/software/plink_program/plink -bfile chr21_splitmultiallelicsnps_filtered --r2 --ld-window 99999 --ld-window-r2 0.05 --out chr21_splitmultiallelicsnps_ld
```