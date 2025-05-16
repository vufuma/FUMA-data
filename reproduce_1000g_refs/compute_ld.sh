#!/bin/bash
#SBATCH --job-name=ld # Job name
#SBATCH -o ld.%j.out                # STDOUT (%j = JobId)
#SBATCH -e ld.%j.err                # STDERR (%j = JobId)
#SBATCH -N 1
#SBATCH -t 01:00:00
#SBATCH --exclusive

/gpfs/home6/tphung/software/plink_program/plink -bfile chr21_splitmultiallelicsnps_filtered --r2 --ld-window 99999 --ld-window-r2 0.05 --out chr21_splitmultiallelicsnps_ld