#!/bin/bash
# wget https://ftp.1000genomes.ebi.ac.uk/vol1/ftp/release/20130502/ALL.chr${i}.phase3_shapeit2_mvncall_integrated_v5b.20130502.genotypes.vcf.gz

i=19

java -jar jvarkit.jar vcfmulti2oneallele ~/tphung_proj/projects/fuma/jira_FUMA_96/reproduce_1000g_refs/ALL.chr${i}.phase3_shapeit2_mvncall_integrated_v5b.20130502.genotypes.vcf.gz > ~/tphung_proj/projects/fuma/jira_FUMA_96/reproduce_1000g_refs/chr${i}_splitmultiallelicsnps.vcf.gz

~/software/plink_program/plink --vcf chr${i}_splitmultiallelicsnps.vcf.gz --out chr${i}_splitmultiallelicsnps

mv chr${i}_splitmultiallelicsnps.bim chr${i}_splitmultiallelicsnps.bim.orig

python add_uniqueID_bim.py -b chr${i}_splitmultiallelicsnps.bim.orig -o chr${i}_splitmultiallelicsnps.bim

python create_include_snps.py --bim chr${i}_splitmultiallelicsnps.bim.orig --out chr${i}_kept_snps.txt

~/software/plink_program/plink -bfile chr${i}_splitmultiallelicsnps --extract chr${i}_kept_snps.txt --maf 0.00000000000000000001 --out chr${i}_splitmultiallelicsnps_filtered --make-bed