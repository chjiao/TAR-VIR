# TAR-VIR
TAR-VIR is a tool to assemble viral haplotypes from metagenomic data with partial or remotely related references. It mainly has two components: (1) Recruit reads from initial aligned reads with overlap extension; (2) *de novo* assembly of viral haplotypes from recruited reads with PEHaplo.   

## Installation
To download the source code:   
git clone --recursive  https://github.com/chjiao/TAR-VIR.git   

1. Install Overlap extension module   
This program requries the supports of C++11.   
cd TAR-VIR   
cd Overlap_extension   
make    

2. Install PEHaplo   
Please look at the ReadMe file for PEHaplo at:   
https://github.com/chjiao/PEHaplo   

## Usage   
1. Overlap extension   
After compilation, there will be two binary files: build and overlap   
(1) build reads index    
./build -f reads.fa -o prefix   
(2) recruite reads   
./overlap -S align.sam -x prefix -f reads.fa -c overlap_cutoff -o recruited_reads.fa   
align.sam is the alignment results of reads.fa on available reference   

Test data and running examples   
The test data sets are in folder Overlap_extension/test_data/.   
virus.fa   
This data set contains simulated viral reads from HIV-1, HCV genotype 1, and HGV.   
HIV.sam   
This SAM file contains a small subset of aligned HIV-1 reads. With these aligned (287) reads, more HIV-1 reads can be recruited from the viral metagenomics data set.   

Example:   
cd Overlap_extension/   
./build -f test_data/virus.fa -o virus   
./overlap -S test_data/HIV.sam -x virus -f test_data/virus.fa -c 180 -o virus_recruit.fa   
If everything is good, the recruited reads number should be 8008.   

2. Assemble   
The recruited reads usually contain both single- or paired-end reads, use the '-f' option of PEHaplo to input one fasta file.    
For details, please look at https://github.com/chjiao/PEHaplo.
