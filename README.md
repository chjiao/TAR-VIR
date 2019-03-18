# TAR-VIR
TAR-VIR is developed to classify RNA viral reads from viral metagenomic data and and also to produce the assembled viral strains (i.e. haplotypes) from classified reads.  It mainly has two components: (1) Viral read classification using partial or remotely related reference genomes; (2) *de novo* assembly of viral haplotypes from recruited reads with PEHaplo, which is a haplotype reconstruction tool. As TAR-VIR has a modular structure, the users have options to use other assembly tools after read classification in step (1). 

To use TAR-VIR, you need to have two types of data. (1) read set, such as viral metagenomic data containing reads from viruses. (2) a reference sequence, which can be a gene or a related genome. In the first step, you need to align the reads against the reference sequence using a read mapping tool. We recommend to use Bowtie2 with default parameters and the allowed error function "L,0,-0.6". The output of this step is a sam file. This sam file and the read data set will be used as input to TAR-VIR. 

We provide two methods for installing TAR-VIR and PEHaplo. You can directly install these tools following the instructions below. In addition, we also provide packaged TAR-VIR and PEHaplo via Anaconda, which makes the installation more straightforward. 

## Installing via conda
Noted that all the packages can be found on anaconda.cloud, which means you can easily install them by using conda. You can follow the [Guaidance](https://github.com/chjiao/TAR-VIR/blob/master/Guidance%20for%20Installing%20PEHaplo%20and%20TAR-VIR.md) to install step by step.

## Installation without using conda
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

## Preprocessing
1. You need to conduct error correction for the reads. By dafault, we use karect ("Karect: accurate correction of substitution, insertion and deletion errors for next-generation sequencing data", Bioinformatics)
2. As mentioned earlier, please use Bowtie2 to align the input reads against the reference sequence. Use all the default parameters except the error function "L,0,-0.6". The output sam file will be used as input to the next step. 

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


