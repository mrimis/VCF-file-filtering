# VCF-file-filtering

#PHFilter v1.0

It removes private heterozygous genotype from vcf file


##Requirements:

Python 2.7 and above


Usage:

python phf_local.py -i input_vcf_file -o output_file -cutoff 1 (or any other numerical value)

-cutoff is optional. Default is set to 1.

You can also call -cutoff all to remove lines that has all 0/1 entries.

python phf_local.py -i input_vcf_file -o output_file -cutoff all


to remove both conditions use

python phf_local.py -i input_vcf_file -o output_file -cutoff 1 (or any other numerical value)

python phf_local.py -i output_file -o output_final -cutoff all

To perform hybrid analysis in order to remove locus in hybrid file filename1 that has 0/1 genotype and ECS/SCS file filename2 contains all 0/0 at that locus, you can use -hybrid tag

python phf_local.py -file1 filename1 -file2 filename2 -o output_file -hybrid
