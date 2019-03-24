
# Guidance for Installing PEHaplo and TAR-VIR via conda

This is a guidance for installing PEHaplo and TAR-VIR via conda. Noted that all the dependencies for these two tools are avaliable on anaconda.cloud, which means you can easily install them by using conda.The whole pipeline for installing them via conda is shown below. To make this self-contained, we also briefly introduce the two tools before giving detailed instructions for installation. 

## Introduction

### [TAR-VIR](https://github.com/chjiao/TAR-VIR)

TAR-VIR is developed to classify RNA viral reads from viral metagenomic data and and also to produce the assembled viral strains (i.e. haplotypes) from classified reads. It mainly has two components: (1) Viral read classification using partial or remotely related reference genomes; (2) de novo assembly of viral haplotypes from recruited reads with PEHaplo, which is a haplotype reconstruction tool.

To use TAR-VIR, you need to have two types of data. (1) read set, such as viral metagenomic data containing reads from viruses. (2) a reference sequence, which can be a gene or a related genome. In the first step, you need to align the reads against the reference sequence using a read mapping tool. We recommend to use Bowtie2 with default parameters and the allowed error function "L,0,-0.6". The output of this step is a sam file. This sam file and the read data set will be used as input to TAR-VIR.

### [PEHaplo](https://github.com/chjiao/PEHaplo)

PEHaplo is a *de novo* assembly tool for recovering virus haplotypes from virus quasispecies sequencing data. It utilizes overlap graph and paired-end information to recover virus haplotypes. Unlike many existing assembly tools, PEHaplo targeted at strain-level assembly for reads sequenced from viruses. 

It requires paired-end reads file as input and outputs contigs that are part of or full haplotypes.

PEHaplo does not need any reference genomes and thus can be applied for identifying new haplotyps or haplotypes that are remotely related to characterized ones.

## Preparation - Installing Anaconda/Miniconda

The webiste of Anaconda provides a nice summary: "Anaconda is a free and open-source distribution of the Python and R programming languages for scientific computing (data science, machine learning applications, large-scale data processing, predictive analytics, etc.), that aims to simplify package management and deployment. Package versions are managed by the package management system conda. You can easily create several individual environments with different python version such as 2.7, 3.5, 3.6.". 

Since there are some required dependencies for PEHaplo and TAR-VIR, you are suggested to install them using [Anaconda](https://www.anaconda.com/distribution/) or [miniconda](https://docs.conda.io/en/latest/miniconda.html) so that you can easily create a well equipped environment.

*Please note that, **ALL** the modules we used in installing PEHaplo and TAR-VIR **ONLY** supply on **Linux**. So please make sure your OS is correct.*


1. Go to [Anaconda] (https://www.anaconda.com/distribution/). Choose "Linux". Then you see a title named  **Anaconda 2018.12 for Linux InstallerDownload**. Download the .sh file by clicking the **Download** buttons. Both Python 3.7 and 2.7 versions are OK. 
2. Bash the .sh file and install anaconda to your computer.
3. Add the anaconda to your PATH. 
The following is from the FAQ of Anaconda. Conda will not work until you add the PATH manually. To add the PATH manually, open a text editor and open the file .bashrc or .bash_profile from your home directory. Add the line `export PATH="/<path to anaconda>/bin:$PATH" ` . NOTE: Replace \<path-to-anaconda>\ with the actual path of your installed anaconda file.
4. If you are using a high performance computing center's cluster, it is possible that conda had been installed previously. To check this, use commands
```
  >module spider conda
 
 ----------------------------------------------------------------------------
  Anaconda2: Anaconda2/4.2.0
----------------------------------------------------------------------------
    Description:
      Built to complement the rich, open source Python community, the
      Anaconda platform provides an enterprise-ready data analytics
      platform that empowers companies to adopt a modern open data science
      analytics architecture. 


    This module can be loaded directly: module load Anaconda2/4.2.0
 
 >module load Anaconda2/4.2.0
```

You can test whether the installation of anaconda is successful by typing some of the following commands. You will need to use some of them when installing TAR-VIR. Detailed information about conda commands can be found in this [link](https://conda.io/en/latest/)

+ See what enviroments you have already had

  > conda info -e

+ List all the packages in your current enviroments

   > conda list
   
+ Search if there is a avalible package in your channel

   > conda search

+ Create a new enviroment (replace [env_name] with your name and [version] with python version

   > conda create -n [env_name] python = [version]

+ Activate an enviroment
  
   > conda activate [env_name]
   
+ Install a new module
  
   > conda install [module_name]

+ Add a new resource to your channel (replace [link of channel] with the resource website). Once you have added the channels for your conda, You can use it to search packages forever for every environment.

   > conda config --add channels [link of channel]

## Build an environment and install dependencies

If the above commands work, this indicates that you have successfully installed conda. You are ready to install the tools now. There are only a few commands to run.

Step 1. Add some resource for your local channel

```
    conda config --add channels defaults
    conda config --add channels conda-forge
    conda config --add channels bioconda
    conda config --add channels kennethshang

```

Step 2. Create a new environment with python2.7

```
    conda create -n bio2 python=2.7     # You can replace bio2 to any name you like
    conda activate bio2                 # Activate your env
    source activate bio2                # Sometimes you need to use this command to activate the environment. Try conda activate first. 
```

Step 3. Install Python module: [networkx 1.11](https://github.com/networkx/networkx/releases/tag/networkx-1.11)

```
    pip install networkx=1.11           # currently TAR-VIR only works with this version. Under some systems, use pip install networkx==1.11. Type both and see the hints. 

```
Step 4. Install dependencies and other needed tools [Karect](https://github.com/aminallam/karect), [Readjoiner](http://www.zbh.uni-hamburg.de/forschung/gi/software/readjoiner.html), [Apsp](https://github.com/chjiao/Apsp), [SGA](https://github.com/jts/sga), [Samtools](http://samtools.sourceforge.net/), [Bowtie2](http://bowtie-bio.sourceforge.net/bowtie2/index.shtml)

```
    conda install Karect bamtools apsp sga samtools bowtie2 overlap_extension
    conda install -c bioconda genometools-genometools
```

# Installing TAR-VIR and PEHaplo

To download the source code:
```
git clone --recursive https://github.com/chjiao/TAR-VIR.git
```
Output of this command might look like 
```
Cloning into 'TAR-VIR'...
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 37 (delta 0), reused 0 (delta 0), pack-reused 34
Unpacking objects: 100% (37/37), done.
Submodule 'Overlap_extension' (https://github.com/chjiao/Overlap_extension.git) registered for path 'Overlap_extension'
Submodule 'PEHaplo' (https://github.com/chjiao/PEHaplo.git) registered for path 'PEHaplo'
Cloning into 'Overlap_extension'...
remote: Enumerating objects: 64, done.
remote: Total 64 (delta 0), reused 0 (delta 0), pack-reused 64
Unpacking objects: 100% (64/64), done.
Submodule path 'Overlap_extension': checked out '371909a3bcd0792b5f93f39970e2612f8010de7a'
Cloning into 'PEHaplo'...
remote: Enumerating objects: 200, done.
remote: Total 200 (delta 0), reused 0 (delta 0), pack-reused 200
Receiving objects: 100% (200/200), 10.74 MiB | 0 bytes/s, done.
Resolving deltas: 100% (126/126), done.
Submodule path 'PEHaplo': checked out '861fbd6c7ab281ee7864014209d7733afa9bd887'
```

# Testing TAR-VIR

*Please note that, **your env should be activated** when testing. If not, please do `conda activate [env_name]`* 


1. Run the example for testing read classification by TAR-VIR
```
cd TAR-VIR/Overlap_extension/
build -f test_data/virus.fa -o virus
overlap -S test_data/HIV.sam -x virus -f test_data/virus.fa -c 180 -o virus_recruit.fa
```
The output contains the number of recruited reads for each iteration, e.g.
```
...
Iteration: 55, recruited reads number: 1294
Seeds number: 1294
Iteration: 56, recruited reads number: 1198
Seeds number: 1198
Iteration: 57, recruited reads number: 1258
Seeds number: 1258
Iteration: 58, recruited reads number: 1260
Seeds number: 1260
Iteration: 59, recruited reads number: 1160
Seeds number: 1160
Iteration: 60, recruited reads number: 1106
Seeds number: 1106
Iteration: 61, recruited reads number: 1075
Seeds number: 1075
Iteration: 62, recruited reads number: 986
Seeds number: 986
Iteration: 63, recruited reads number: 1052
Seeds number: 1052
...
```

If everything is good, the recruited reads number should be 81326.


# Testing PEHaplo

*Please note that, **your env should be activated** when testing. If not, please do `conda activate [env_name]`* 

Run the example for testing (it takes about 3 minutes to get the results)
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
    Contigs_clipped.fa is the output after contig correction - we applied one more step to align reads to assembled contigs and try to break some misjoined contigs.
    PEG_nodes_sequences.fa: the nodes sequences in the graph before doing any assembly.

# A running Example For Whole TAR-VIR (read recruting and strain assembly)

*Please note that, **your env should be activated** when Running. If not, please do `conda activate [env_name]`* 

1. Commands for generating sam file
```
cd test_data
mkdir index
bowtie2-build -f HIV_ref.fa index/HXB2
bowtie2 -x index/HXB2 -f virus.fa --score-min L,0,-0.05 -t -p 4 -S result.sam
```
To get only the mapped reads (to save loading time for large data set):

```
samtools view -F 4 result.sam >result_mapped.sam
```

2. Using the Overlap component in TAR-VIR to recruit reads from given references.

```
cd ..
build -f test_data/virus.fa -o virus
overlap -S test_data/result.sam -x virus -f test_data/virus.fa -c 180 -o virus_recruit.fa
```
The output contains the number of recruited reads for each iteration, e.g.
```
...
Iteration: 55, recruited reads number: 1294
Seeds number: 1294
Iteration: 56, recruited reads number: 1198
Seeds number: 1198
Iteration: 57, recruited reads number: 1258
Seeds number: 1258
Iteration: 58, recruited reads number: 1260
Seeds number: 1260
Iteration: 59, recruited reads number: 1160
Seeds number: 1160
Iteration: 60, recruited reads number: 1106
Seeds number: 1106
Iteration: 61, recruited reads number: 1075
Seeds number: 1075
Iteration: 62, recruited reads number: 986
Seeds number: 986
Iteration: 63, recruited reads number: 1052
Seeds number: 1052
...
```

If everything is good, the recruited reads number should be 81326.

2. Copy the output file form the Overlap to PEHaplo

Since we need to use the output file from the Overlap as the input of PEHaplo, we need to copy it to the PEHaplo dictionary. Do the following command.

```
cp virus_recruit.fa ../PEHaplo
```

3. Preprocessing your raw data into correct form for PEHaplo

```
cd ../PEHaplo
mkdir test
cd test
python ../tools/get_read_pairs.py ../virus_recruit.fa
```
Output of this command should be:
```
The number of read pairs is: 11590, single-end reads is: 58146
```
And it will output three files: single_end.fa, pair1.fa, and pair2.fa. 

4. Running PEHaplo with your input data (It will take a few minutes to get the results)

```
python ../pehaplo.py -f1 pair1.fa -f2 pair2.fa -l 180 -l1 210 -r 250 -F 600 -std 150 -n 3 -correct yes

Output:
Contigs.fa: the raw output contigs
Contigs_clipped.fa: the contigs after error correction
PEG_nodes_sequences.fa: the nodes sequences in the graph
```
# FAQ
1. If you see an error, very likely it is caused by missing packages/dependencies. For example, if you see an error like below when running PEHaplo:
Traceback (most recent call last):
  File "/mnt/home/yannisun/TAR-VIR/PEHaplo/tools/identify_misjoin_contigs.py", line 5, in <module>
    from scipy import stats
ImportError: No module named scipy
Traceback (most recent call last):
  File "../pehaplo.py", line 157, in <module>
    contigs_mapped.sam 250 600 150' returned non-zero exit status 1
 The message **ImportError: No module named scipy** means that you did not have scipy installed. In this case, run the following command will solve this problem. 

```  
> pip install scipy
```
2. Sometimes, just try to re-run the packaging installing command will solve most issues.
For example, we find that we need to reinstall sga when we test our program under one environment. In this case, you can uninstall the old packages and reinstall the new one. 
```
conda uninstall sga
conda install sga
```
3. You can add the following links to accelerate adding channels when you are in mainland China.
    conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/ 
    conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
    conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
    conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r/
    conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/bioconda/
    conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/msys2/
    conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/menpo/
    conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/
  
