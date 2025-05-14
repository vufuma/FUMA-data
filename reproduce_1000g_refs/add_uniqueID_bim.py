import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-b', '--bim', required=True)
parser.add_argument('-o', '--out', required=True)
args = parser.parse_args()

outfile = open(args.out, "w")

with open(args.bim, "r") as f:
    for line in f:
        items = line.rstrip("\n").split("\t")
        alleles = sorted([items[4], items[5]])
        id = items[0] + ":" + items[3] + ":" + alleles[0] + ":" + alleles[1]
        new_line = [items[0], id] + items[2:]
        print("\t".join(new_line), file=outfile)