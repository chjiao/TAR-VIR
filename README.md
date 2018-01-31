# OL_PEHaplo
OL_PEHaplo is a tool to assemble viral haplotypes from metagenomic data with partial or remotely related references. It mainly has two components: (1) Recruit reads from initial aligned reads with overlap extension; (2) *de novo* assembly of viral haplotypes from recruited reads.  

## Installation
1. Install Overlap extension module
This program requries the supports of C++11.   
cd ./Overlap_extension/   
make    

2. Install PEHaplo
Please look at the ReadMe file for PEHaplo at:   
https://github.com/chjiao/PEHaplo

## Usage
1. Overlap extension
After compilation, there will be two binary files: build and overlap   
./build -f reads.fa -o prefix   
./overlap -S align.sam -x prefix -f reads.fa -c overlap_cutoff -o recruited_reads.fa   

2. Assemble
The recruited reads usually contain both single- or paired-end reads, use the '-f' option of PEHaplo to input one fasta file. 
For details, please look at https://github.com/chjiao/PEHaplo.
