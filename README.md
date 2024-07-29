# FUMA-data
This is an attempt for an automated way to download and reproduce fuma reference data.


## Data repositories and tools currently used in FUMA:

Here is the table reformatted to markdown:


**Source: https://static-content.springer.com/esm/art%3A10.1038%2Fs41467-017-01261-5/MediaObjects/41467_2017_1261_MOESM1_ESM.docx**
**Category** | **Name** | **Description** | **Last accessed** | **Link**
-----------|---------|-----------------|---------------|------
Reference Variants | dbSNP 146 | Map rsID of input files to dbSNP build 146 | 18-Mar-16 | [link](http://ftp.ncbi.nlm.nih.gov/snp/organisms/human_9606_b146_grch137p13/database/organism_data/RsMergeArch.bcp.gz)
Reference Genome | 1000 Genomes Project Phase3 | Compute MAF and r2 for each available population | 25-Apr-16 | [link](http://ftp.1000genomes.ebi.ac.uk/vol1/ftp/release/20130502/)
Functional annotations of SNPs | CADD v1.3 | Deleteriousness score of variants | 09-Jul-16 | [link](http://cadd.gs.washington.edu/download)
Functional annotations of SNPs | RegulomeDB | Score of regulatory variants | 16-Feb-16 | [link](http://www.regulomedb.org/downloads)
Functional annotations of SNPs | 15-core chromatin state | Chromatin states of genomic region in 127 tissue/cell types | 15-May-16 | [link](http://egg2.wustl.edu/roadmap/data/byFileType/chromhmmSegmentations/ChmmModels/coreMarks/jointModel/final/)
Functional annotations of SNPs | GWAS catalog | Known trait associated variants | 05-Oct-16 | [link](https://www.ebi.ac.uk/gwas/)
eQTLs | GTEx v6 | cis-eQTLs of 44 tissue types | 16-Mar-16 | [link](http://www.gtexportal.org/home/)
eQTLs | Blood eQTL Browser | cis-eQTLs of blood cell | 06-Jun-16 | [link](http://genenetwork.nl/bloodeqtlbrowser/)
eQTLs | BIOS QTL Browser | cis-eQTLs of blood cell | 07-Oct-16 | [link](http://genenetwork.nl/biosqtlbrowser/)
eQTLs | BRAINEAC | cis-eQTLs of 10 brain regions | 09-Sep-16 | [link](http://www.braineac.org/)
HiC | GSE87112 | HiC data for 14 tissue types and 7 cell lines | 24-Apt-17 | [link](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE87112)
Regulatory elements | Roadmapc epigenomics project | Enhancer, promoter and dyadic enhancer/promoter regions in 111 epigenomes | 24-Apt-17 | [link](http://egg2.wustl.edu/roadmap/data/byDataType/dnase/)
Gene score | pLI | Probability of being loss-of-function intolerance | 24-Apt-17 | [link](http://ftp.broadinstitute.org/pub/ExAC_release/release0.3.1/functional_gene_constraint)
Gene score | ncRVIS | Non-coding residual variation intolerance score | 24-Apt-17 | [link](http://journals.plos.org/plosgenetics/article/file?type=supplementary&id=info:doi/10.1371/journal.pgen.1005492.s011)
Gene expression | GTEx v6 | Normalized gene expression (RPKM: Read Per Kilo base per Million) for 53 tissue types | 16-Mar-16 | [link](http://www.gtexportal.org/home/)
Gene sets | MsigDB v5.2 | Curated pathways and gene sets | 26-Dec-16 | [link](http://software.broadinstitute.org/gsea/msigdb/)
Gene sets | WikiPathways | Curated pathways | 22-Apr-16 | [link](http://wikipathways.org/index.php/WikiPathways)
Tools | ANNOVAR | Variant annotation tool | 11-Feb-16 | [link](http://annovar.openbioinformatics.org/en/latest/)
Tools | MAGMA v6.0 | Software for gene-based test and gene-set analyses of GWAS | 17-Jan-17 | [link](https://ctg.cncr.nl/software/magma)