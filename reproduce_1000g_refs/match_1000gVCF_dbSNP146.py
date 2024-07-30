# This script is used to obtain the rsID for the variants in the 1000G VCF file
# 1000G VCF file: ALL.chr21.phase3_shapeit2_mvncall_integrated_v5b.20130502.genotypes.vcf.gz
# dbSNP146 stored in FUMA: dbSNP/dbSNP146.chr21.vcf.gz
import gzip

# create a dictionary from dbSNP146
# sort alleles alphabetically because this was how it was done

dbSNP146_dict = {} #key: 21:9411199:C:T & value: rs376129767
with gzip.open("/mnt/p/reference_data/dbSNP/dbSNP146.chr21.vcf.gz", 'rb') as f:
    for line in f:
        items = line.rstrip(b'\n').split(b'\t')
        allele_1 = items[3].decode("utf-8")
        allele_2 = items[4].decode("utf-8")
        if "," not in allele_1 and "," not in allele_2:
            alleles_sorted = sorted([allele_1, allele_2])
            uniqID = items[0].decode("utf-8") + ":" + items[1].decode("utf-8") + ":" + alleles_sorted[0] + ":" + alleles_sorted[1]
            if uniqID not in dbSNP146_dict:
                dbSNP146_dict[uniqID] = items[2].decode("utf-8")
        elif "," in allele_1 and "," not in allele_2:
            first_allele_all = allele_1.split(",")
            for i in first_allele_all:
                alleles_sorted = sorted([i, allele_2])
                uniqID = items[0].decode("utf-8") + ":" + items[1].decode("utf-8") + ":" + alleles_sorted[0] + ":" + alleles_sorted[1]
                if uniqID not in dbSNP146_dict:
                    dbSNP146_dict[uniqID] = uniqID
        elif "," not in allele_1 and "," in allele_2:
            second_allele_all = allele_2.split(",")
            for j in second_allele_all:
                alleles_sorted = sorted([allele_1, j])
                uniqID = items[0].decode("utf-8") + ":" + items[1].decode("utf-8") + ":" + alleles_sorted[0] + ":" + alleles_sorted[1]
                if uniqID not in dbSNP146_dict:
                    dbSNP146_dict[uniqID] = uniqID
        elif "," in allele_1 and "," in allele_2:
            first_allele_all = allele_1.split(",")
            for i in first_allele_all:
                second_allele_all = allele_2.split(",")
                for j in second_allele_all:
                    alleles_sorted = sorted([i, j])
                    uniqID = items[0].decode("utf-8") + ":" + items[1].decode("utf-8") + ":" + alleles_sorted[0] + ":" + alleles_sorted[1]
                    if uniqID not in dbSNP146_dict:
                        dbSNP146_dict[uniqID] = uniqID

# print(dbSNP146_dict["21:9657704:G:T"])

# Initialize an outfile
outfile = open("ALL.chr21.rsID.txt", "w")
notfound = open("uniqID_notfound.txt", "w")

with gzip.open("ALL.chr21.phase3_shapeit2_mvncall_integrated_v5b.20130502.genotypes.vcf.gz", 'rb') as f:
    for line in f:
        if not line.startswith(b'#'):
            items = line.rstrip(b'\n').split(b'\t')
            allele_1 = items[3].decode("utf-8")
            allele_2 = items[4].decode("utf-8")
            if "," not in allele_1 and "," not in allele_2:
                alleles_sorted = sorted([allele_1, allele_2])
                uniqID = items[0].decode("utf-8") + ":" + items[1].decode("utf-8") + ":" + alleles_sorted[0] + ":" + alleles_sorted[1]
                if uniqID in dbSNP146_dict:
                    out = [items[0].decode("utf-8"), items[1].decode("utf-8"), uniqID, dbSNP146_dict[uniqID]]
                    print("\t".join(out), file=outfile)
                else:
                    print(uniqID, file=notfound)
            
            elif "," in allele_1 and "," not in allele_2:
                first_allele_all = allele_1.split(",")
                for i in first_allele_all:
                    alleles_sorted = sorted([i, allele_2])
                    uniqID = items[0].decode("utf-8") + ":" + items[1].decode("utf-8") + ":" + alleles_sorted[0] + ":" + alleles_sorted[1]
                    if uniqID in dbSNP146_dict:
                        out = [items[0].decode("utf-8"), items[1].decode("utf-8"), uniqID, dbSNP146_dict[uniqID]]
                        print("\t".join(out), file=outfile)
                    else:
                        print(uniqID, file=notfound)

            elif "," not in allele_1 and "," in allele_2:
                second_allele_all = allele_2.split(",")
                for j in second_allele_all:
                    alleles_sorted = sorted([allele_1, j])
                    uniqID = items[0].decode("utf-8") + ":" + items[1].decode("utf-8") + ":" + alleles_sorted[0] + ":" + alleles_sorted[1]
                    if uniqID in dbSNP146_dict:
                        out = [items[0].decode("utf-8"), items[1].decode("utf-8"), uniqID, dbSNP146_dict[uniqID]]
                        print("\t".join(out), file=outfile)
                    else:
                        print(uniqID, file=notfound)

            elif "," in allele_1 and "," in allele_2:
                first_allele_all = allele_1.split(",")
                for i in first_allele_all:
                    second_allele_all = allele_2.split(",")
                    for j in second_allele_all:
                        alleles_sorted = sorted([i, j])
                        uniqID = items[0].decode("utf-8") + ":" + items[1].decode("utf-8") + ":" + alleles_sorted[0] + ":" + alleles_sorted[1]
                        if uniqID in dbSNP146_dict:
                            out = [items[0].decode("utf-8"), items[1].decode("utf-8"), uniqID, dbSNP146_dict[uniqID]]
                            print("\t".join(out), file=outfile)
                        else:
                            print(uniqID, file=notfound)

outfile.close()