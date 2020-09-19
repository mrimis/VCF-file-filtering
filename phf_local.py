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



try:
    import argparse
except ImportError, e:
    sys.exit('Requires python 2.7 and above to run ConCat-1.0. Program Terminated')

import textwrap
from src import *

parser = argparse.ArgumentParser(prog='HetFilter',
                                 version= 'HetFilter-1.0',
                                 formatter_class=argparse.RawDescriptionHelpFormatter,
                                 description=textwrap.dedent('''\
    ----------------------------------------------------------------------------------------------------------
    \t\t\t\t  Welcome to HetFilter-1.0
    \t\t\t\t VCF file filtering program
    \t\t\tWritten by Mrinal Mishra, University of Florida
    ----------------------------------------------------------------------------------------------------------
    
    
    '''))

parser.add_argument('-i', type=str, default=None,
                    help='Enter input file name')
parser.add_argument('-o', type=str, required=True,
                    help='Enter output file name')
parser.add_argument('-cutoff', default=1,
                    help='Enter the heterozygous cutoff value. It can also take "all" for genetypes with all heterozygous entries (all 0/1 = all entries). Default is 1.')
parser.add_argument('-hybrid', action='store_true', default=False,
                    help='Use this function if you want to perform hybrid locus comparison')
parser.add_argument('-file1', type=str, default=None,
                    help='Enter first input file name')
parser.add_argument('-file2', type=str, default=None,
                    help='Enter second input file name')

args = parser.parse_args()

try:
    args.cutoff = int(args.cutoff)
except:
    if args.cutoff != "all":
        parser.error('-cutoff argument can either take numerical value of heterozygous cutoff count or it can take "all" for genetypes with all heterozygous entries (all 0/1 = all entries)')

if args.hybrid == False and args.i == None:
    parser.error('-i argument is required when not using hybrid comparison')
if args.hybrid == True and args.file1 == None:
    parser.error('-file1 argument is required when using hybrid comparison')
if args.hybrid == True and args.file2 == None:
    parser.error('-file2 argument is required when using hybrid comparison')




def main():
    if args.hybrid == True:
        PHF().compare(args.file1, args.file2, args.o)
    else:
        PHF().execute(args.i, args.o, args.cutoff)

if __name__ == "__main__":
    main()
