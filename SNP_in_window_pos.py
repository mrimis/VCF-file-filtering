
fdata = open("Final_filtered_All_60_SNPS.vcf", "rU") # Open vcf file
SCS=[1,22,23,24,25,26,27,28,29,30]#Indexes of samples belonging to SCS allopatric population
SCS_Allo = [x-1 for x in SCS]
ECS=[3,5,6,12,13,14,16,17,19,20,37,38,40,41,42,43,54,55,56,57,58,59,60]#Indexes of samples belonging to ECS population
ECS_Symp = [x-1 for x in ECS]
SCS_Sym = [2,4,7,8,9,10,11,15,18,21,31,32,33,34,35,36,44,45,46,47,48,49,50,51,52,53]#Indexes of samples belonging to SCS Sympatric population
SCS_Symp = [x-1 for x in SCS_Sym]
list1=[]
with open("SCS_Symp_scaffold8_7509_7927.txt", "w") as fp, open("SCS_Allo_scaffold8_7509_7927.txt","w") as fp1,  open("ECS_scaffold8_7509_7927.txt","w") as fp2: #Open file for writing
   for lines in fdata: #Loop over all the lines of the VCF file
        lobj = lines.strip().split("\t") #Split the lines using tab delimited character
        if "#" not in lobj[0] and lobj[0] =="BS.genome_hic_scaffold_8" and float(lobj[1]) > 36747509 and float(lobj[1]) < 36747927: #extracting elements within particular window
        	elements=lobj[9:]
        	for i in SCS_Symp:
        		gt=elements[i].split(':')[0]
        		fp.write(lobj[0] + "\t" + str(lobj[1]) + "\t" + str(lobj[2]) + "\t" + str(lobj[3])+ "\t" + str(lobj[4]) + "\t" + str(gt) + "\n")
        	for j in SCS_Allo:
        		gt1=elements[j].split(':')[0]
        		fp1.write(lobj[0] + "\t" + str(lobj[1]) + "\t" + str(lobj[2]) + "\t" + str(lobj[3])+ "\t" + str(lobj[4]) + "\t" + str(gt1) + "\n")
        	for k in ECS_Symp:
        		gt2=elements[k].split(':')[0]
        		fp1.write(lobj[0] + "\t" + str(lobj[1]) + "\t" + str(lobj[2]) + "\t" + str(lobj[3])+ "\t" + str(lobj[4]) + "\t" + str(gt2) + "\n")
