
# Guidance for Installing PEHaplo and TAR-VIR

This is a guidance for installing PEHaplo and TAR-VIR. Noted that all the dependencies for these two tools are avaliable on anaconda.cloud, which means you can easily install them by using conda.The whole pipeline are shown below.

## Introduction

### [PEHaplo](https://github.com/chjiao/PEHaplo)

PEHaplo is a *de novo* assembly tool for recovering virus haplotypes from virus quasispecies sequencing data. It utilizes overlap graph and paired-end information to recover virus haplotypes. 

It requires paired-end reads file as input and outputs contigs that are part of or full haplotypes.

PEHaplo does not need any reference genomes and thus can be applied for identifying new haplotyps or haplotypes that are remotely related to characterized ones.

### [TAR-VIR](https://github.com/chjiao/TAR-VIR)

TAR-VIR is developed to classify RNA viral reads from viral metagenomic data and and also to produce the assembled viral strains (i.e. haplotypes) from classified reads. It mainly has two components: (1) Viral read classification using partial or remotely related reference genomes; (2) de novo assembly of viral haplotypes from recruited reads with PEHaplo, which is a haplotype reconstruction tool.

To use TAR-VIR, you need to have two types of data. (1) read set, such as viral metagenomic data containing reads from viruses. (2) a reference sequence, which can be a gene or a related genome. In the first step, you need to align the reads against the reference sequence using a read mapping tool. We recommend to use Bowtie2 with default parameters and the allowed error function "L,0,-0.6". The output of this step is a sam file. This sam file and the read data set will be used as input to TAR-VIR.

## Advance Preparation - Installing Anaconda/Miniconda

Anaconda is a free and open-source distribution of the Python and R programming languages for scientific computing (data science, machine learning applications, large-scale data processing, predictive analytics, etc.), that aims to simplify package management and deployment. Package versions are managed by the package management system conda. You can easily create several individual environments with different python version such as 2.7, 3.5, 3.6.

Since there are a lot of required dependencies for PEHaplo and TAR-VIR. You are suggested to install them using [Anaconda](https://www.anaconda.com/distribution/) or [miniconda](https://docs.conda.io/en/latest/miniconda.html) so that you can easily create a well equipped environment.

*Please note that, **ALL** the module we used in installing PEHaplo and TAR-VIR **ONLY** supply on **Linux**. So please make sure your OS is correct.*


1. Download the .sh file from the above link
2. Bash the .sh file and install anaconda to your computer
3. Add the anaconda to your PATH

Then you can use the conda command on your terminal. Detail information of conda can be found in this [link](https://conda.io/en/latest/)

There are several commands you may need to use:

+ See what enviroments you have already had

  > conda info -e

+ List all the packages in your current enviroments

   > conda list
   
+ Search if there is a avalible in your channel

   > conda search

+ Create a new enviroment (replace [env_name] with your name and [version] with python version

   > conda create -n [env_name] python = [version]

+ Activate an enviroment
  
   > conda activate [env_name]
   
+ Install a new module
  
   > conda install [module_name]

+ Add a new resource to your channel (replace [link of channel] with the resource website). Once you have added the channels for your conda, You can use it to search packages forever for every environment.

   > conda config --add channels [link of channel]

## The whole pipeline for building an environment

If you can use your conda on your terminal, let's begin.

1. Add some resource for your local channel

```
    conda config --add channels defaults
    conda config --add channels conda-forge
    conda config --add channels bioconda
    conda config --add channels kennethshang
    
    
    # You can add the following links to accelerate when you are in China mainland
    conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/ 
    conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
    conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
    conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r/
    conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/bioconda/
    conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/msys2/
    conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/menpo/
    conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/

```

2. Create a new environment with python2.7

```
    conda create -n bio2 python=2.7     # You can replace bio2 to any name you like
    conda activate bio2                 # Activate your env
```

3. Install Python module: [networkx 1.11](https://github.com/networkx/networkx/releases/tag/networkx-1.11)

```
    pip install networkx=1.11           

```
4. Install [Karect](https://github.com/aminallam/karect), [Readjoiner](http://www.zbh.uni-hamburg.de/forschung/gi/software/readjoiner.html), [Apsp](https://github.com/chjiao/Apsp), [SGA](https://github.com/jts/sga), [Samtools](http://samtools.sourceforge.net/), [Bowtie2](http://bowtie-bio.sourceforge.net/bowtie2/index.shtml)

```
    conda install Karect bamtools apsp sga samtools bowtie2 overlap_extension
```

# Installing TAR-VIR

To download the source code:
```
git clone --recursive https://github.com/chjiao/TAR-VIR.git
```

# Testing PEHaplo

*Please note that, **your env should be activated** when testing. If not, please do `conda activate [env_name]`*

Run the example for testing
```
cd TAR-VIR/PEHaplo
mkdir assembly
cd assembly
python ../apsp_overlap_clique.py ../processed_test_data/Plus_strand_reads.fa ../processed_test_data/pair_end_connections.txt 180 250 600 210
```

180: initial overlap threshold before merging cliques
    
    
250: read size
    
    
600: paired-end insert size
    
    
210: overlap threshold after merging cliques

Output:
    Contigs.fa: the produced contigs
    PEG_nodes_sequences.fa: the nodes sequences in the graph


# Testing Overlap


1. Install Overlap extension module
This program requries the supports of C++11.
cd TAR-VIR
cd Overlap_extension
make

2. Install PEHaplo
Please look at the ReadMe file for PEHaplo at:
https://github.com/chjiao/PEHaplo

3. Run the example for testing
```
cd TAR-VIR/Overlap_extension/
build -f test_data/virus.fa -o virus
overlap -S test_data/HIV.sam -x virus -f test_data/virus.fa -c 180 -o virus_recruit.fa
```
If everything is good, the recruited reads number should be 8008.
