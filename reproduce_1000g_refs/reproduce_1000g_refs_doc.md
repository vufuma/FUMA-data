- Download `https://ftp.1000genomes.ebi.ac.uk/vol1/ftp/release/20130502/ALL.chr21.phase3_shapeit2_mvncall_integrated_v5b.20130502.genotypes.vcf.gz` (date: 2024-07-29)
- Wrote Python script `reproduce_1000g_refs/match_1000gVCF_dbSNP146.py` to attempt to reproduce the file `1KG/Phase3/ALL/ALL.chr21.rsID.gz`
- Compared the new output and the current FUMA output
```
# new output
less ALL.chr21.rsID.txt | wc -l
1109767

# current FUMA output
zless ALL.chr21.rsID.gz | wc -l
1105982
```
- Diff the new output and the current FUMA output to find the discrepanices
    - Annotated the diff output. See the excel file: `reproduce_1000g_refs/annotated_diff_output.xlsx`
    - Summary of discrepancies

**Explanation #1**
In current FUMA, if the variant is for example A,C:T, then it would be split into 2 variants with the uniqID and the rsID is ignored. 
However, current FUMA does not account for this if it's reversed. For example, if it's T:A,C, it does not get split into 2 variants with the uniqID

For example, look at this variant from dbSNP146 (file: dbSNP/dbSNP146.chr21.vcf.gz)
21      9415721 rs569225703     T       A,C
This is how it is represented in current FUMA (file: 1KG/Phase3/ALL/ALL.chr21.rsID.gz)
21      9415721 21:9415721:A:T  21:9415721:A:T
21      9415721 21:9415721:C:T  21:9415721:C:T

Here is another example:
dbSNP146: 21      9417961 rs66525445      T       C,G
current FUMA:
21      9417961 21:9417961:C:T  21:9417961:C:T
21      9417961 21:9417961:G:T  21:9417961:G:T

However, this rule does not work all the time
21      9416257 rs368069649     C       A,G
This is how it is represented in current FUMA
21      9416257 21:9416257:A:C  rs368069649
Here, the problem is that this rule does not seem to be applied 100% of the time

Other examples:
dbSNP146: 21      9420059 rs71266703      C       A,T
current FUMA: 21      9420059 21:9420059:A:C  rs71266703

dbSNP146: 21      9437763 rs373434506     C       G,T
current FUMA: 21      9437763 21:9437763:C:T  rs373434506

dbSNP146: 21      9484661 rs76913230      A       G,T
current FUMA: 21      9484661 21:9484661:A:T  rs76913230

dbSNP146: 21      9489246 rs531920136     T       A,C
current FUMA: 21      9489246 21:9489246:A:T  rs531920136

dbSNP146: 21      9489360 rs552053719     A       AAT,ATG
current FUMA: 21      9489360 21:9489360:A:ATG        rs552053719

Therefore, I have no clue as to why some variants with 2 alternate alleles are separated but this rule does not seem to apply to other variants

- Another discrepancy has to do with some variants in dbSNP146 that are not found in current FUMA AND also NOT found in other resources such as gnomAD
- However, some variants that are in dbSNP146 that are not found in current FUMA BUT ARE FOUND in gnomAD. WHY is it the case? Why are some variants removed randomly? 