#!/usr/bin/env python
# -*- coding: utf-8 -*-


################################################################################################################
#                                                                                                              #
# Copyright (C) {2019}  {Mrinal Mishra, Miyamoto lab, Biology Department, University of Florida}      #
#                                                                                                              #
# This program is free software: you can redistribute it and/or modify                                         #
# it under the terms of the GNU General Public License as published by                                         #
# the Free Software Foundation, either version 3 of the License, or                                            #
# (at your option) any later version.                                                                          #
#                                                                                                              #
# This program is distributed in the hope that it will be useful,                                              #
# but WITHOUT ANY WARRANTY; without even the implied warranty of                                               #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                                                #
# GNU General Public License for more details.                                                                 #
#                                                                                                              #
# This program comes with ABSOLUTELY NO WARRANTY;                                                              #
# This is free software, and you are welcome to redistribute it                                                #
# under certain conditions;                                                                                    #
#                                                                                                              #
################################################################################################################

import os

name = "HetFilter"
__author__ = "Mrinal Mishra <mrinalmishra@.ufl.edu>"
__date__ = "1st March 2019"
__version__ = "1.0"


class PHF():
    def execute(self, input_file, output_file, heterozygous_cutoff=1): #Function to filter locus with private heterozygotes and locus having only 0/1 genotype for all the individuals 
        fdata = open(input_file, "rU") # Open vcf file
        with open(output_file, "w") as fp: #Open file for writing
            for lines in fdata: #Loop over all the lines of the VCF file
                lobj = lines.strip().split("\t") #Split the lines using tab delimited character
                if "#" not in lobj[0]: #Check if line starts with 'BS.genome' tag and lack '##' character. Example skip line - '##contig=<ID=BS.genome_hic_scaffold_3612,length=6955>'
                    count_01 = 0 # Initiate counter for 0/1
                    count_11 = 0 # Initiate counter for 1/1
                    elemnts = lobj[9:] #Collect all the GT:AD:DP:GQ:PL values for a locus
                    for in_element in elemnts: #Loop over all the GT:AD:DP:GQ:PL values for a locus
                        elObj = in_element.split(":") #split GT:AD:DP:GQ:PL values for a locus using ':' as a split character
                        if elObj[0] == "0/1": # increase counter of 0/1 if the first element has 0/1 tag
                            count_01 = count_01 + 1
                        if elObj[0] == "1/1": # increase counter of 1/1 if the first element has 0/1 tag
                            count_11 = count_11 + 1

                    if heterozygous_cutoff != "all": #Perform this step if heterozygous cutoff is not set to 'all'
                        if count_01 == heterozygous_cutoff and count_11 == 0: #Skip the line if it has count of 0/1 == heterozygous cuttoff (default 1) and zero 1/1
                            continue
                        else:
                            fp.write(lines) # Write everything else
                    else:
                        if count_01 > 1 and count_11==0: #Skip the line if all individual having > 1 and zero 1/1 count genotype for a locus
                            continue
                        else:
                            fp.write(lines) #Write everything else

                else:
                    fp.write(lines)

    def compare(self, file1, file2, output_file): #Function to filter private heterozygous allele from Hybrid VCF file by comparing Hybrid locus positions to locus positions of ECS/SCS VCF file
        fdata = open(file1, "rU") # Open vcf file1 (hybrid vcf file)
        with open(output_file, "w") as fp: #Open file for writing
            for lines in fdata: #Loop over all the lines of the VCF file
                lobj = lines.strip().split("\t")#Split the lines using tab delimited character
                if "#" not in lobj[0]: #Check if line starts with 'BS.genome' tag and lack '##' character. Example skip line - '##contig=<ID=BS.genome_hic_scaffold_3612,length=6955>'
                    pos = lobj[1] #Collect all the locus position in file 1
                    os.system("grep -i \t%s\t %s > check.txt" %(pos, file2)) # check and store the lines of file2 with matching locus positions in file1
                    try:
                        fdata_in = open("check.txt", "rU").readlines()#open "check.txt" file
                        lobj_in = fdata_in[0].strip().split("\t")#Split the lines first index (locus position) using tab delimited character
                    except:
                        fp.write(lines) #Write locus line if its completely absent in file2 and move to the next line
                        continue
                     
                    elements_1 = lobj[9] #Collect the GT:AD:DP:GQ:PL values for a locus in file 1 (hybrid vcf file)
                    elements_2 = lobj_in[9:] ##Collect all the GT:AD:DP:GQ:PL values for a locus in file 2 (ECS/SCS file)
                    obj_1 = elements_1.split(":")[0]#split GT:AD:DP:GQ:PL values for a locus using ':' as a split character in file1
                    obj_2 = list(set([x.split(":")[0] for x in elements_2]))#split GT:AD:DP:GQ:PL values for a locus using ':' as a split character in file2
                    if obj_1 == "0/1" and obj_2 == ["0/0"]:#Skip the line if hybrid file have 0/1 and ECS or SCS file have only 0/0 for all the individuals at particular locus
                        continue
                    else:
                        fp.write(lines) # Write everything else
                    os.system("rm check.txt")
                else:
                    fp.write(lines) # Write everything else

