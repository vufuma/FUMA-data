import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-b', '--bim', required=True)
parser.add_argument('-o', '--out', required=True)
args = parser.parse_args()

outfile = open(args.out, "w")

kept_snps = set()
kept_snps_repeated = set()

with open(args.bim, "r") as f:
    for line in f:
        items = line.rstrip("\n").split("\t")
        if items[4].startswith("<"):
            continue
        else:
            alleles = sorted([items[4], items[5]])
            id = items[0] + ":" + items[3] + ":" + alleles[0] + ":" + alleles[1]
            if id not in kept_snps:
                kept_snps.add(id)
            else:
                kept_snps_repeated.add(id)
                
kept_snps_rmdups = kept_snps-kept_snps_repeated
print(len(kept_snps))
print(len(kept_snps_repeated))
print(len(kept_snps_rmdups))
for i in kept_snps_rmdups:
    print(i, file=outfile)