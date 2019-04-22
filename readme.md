# TAD-Gene Content Tool (TAD-GConTool)


**This tool was developed to support prediction of the phenotypic outcome of chromosomal or genomic structural variants
(unbalanced and balanced translocations, inversion, insertion, deletions, duplications or of a specific genomic region).**

## Before starting

The tool, based on the genomic position of the breakpoints, identifies the Topologically Associated Domains (TADs) from the breakpoint regions
and retrieves series protein-coding and non-coding RNA genes and genomic elements found within these domains and associated structural and functional information.

The tool was developed to work as a CGI application. The web acessible version of the application will be available soon.

## Dependencies:
+ Web Server with CGI support and configured to handle CGI Programs.
+ python2
+ [biomart](https://pypi.org/project/biomart/)
+ [openpyxl](https://openpyxl.readthedocs.io/en/stable/) 
+ [biopython](https://github.com/biopython/biopython)
+ [urllib2](https://docs.python.org/2/library/urllib2.html)
+ [cgi](https://docs.python.org/2/library/cgi.html), [cgitb](https://docs.python.org/2/library/cgitb.html)
+ other python libraries as sys, collections and time

## External sources used:
This tool uses a set of external sources and information that is available in text files along with the scripts.
These external informations are:
+ Vista enhancers from [UCSC Genome Browser](https://genome.ucsc.edu/)
+ Cytoband and Chromosome sizes for hg19 and hg38 genome versions from [UCSC Genome Browser](https://genome.ucsc.edu/)
+ Haploinsufficiency index (HI) and probability that a gene is intolerant to a Loss of Function mutation (pli) from [Decipher](https://decipher.sanger.ac.uk/)
+ observed / expected score (oe) from [gnomad](https://gnomad.broadinstitute.org/)
+ Topological Associated Domains (TADs) for Stem Cells (hESC) and fibroblasts (IMR90) from [Dixon et al., 2012](https://www.ncbi.nlm.nih.gov/pubmed/22495300)
+ Topological Associated Domains (TADs) for lymphoblastoid cell lines (GM12878) from [Moore et al., 2015](https://github.com/blmoore/3dgenome)
+ Mouse Genome Informatics (MGI) associated acessions from [MGI](http://www.informatics.jax.org/)
+ Gene2Phenotype (G2P) data from [G2P](https://www.ebi.ac.uk/gene2phenotype)
+ Overlap with Truesight panels from [Illumina](https://www.illumina.com/products/by-type/clinical-research-products/trusight-one.html)

## Usage:

To put this tool up and runing just clone the repository, and move the contents to the cgi-bin folder of your webserver.
Point your browser for:

<pre><code> http://[your_web_server]/cgi-bin/TAD-GConTool.py
</code></pre> 

Where [your_web_server] iths the adress of your webserver.

## The output:

For each breakpoint, the retrieved data is compiled in a complete table that includes all acquired information and a report table that mainly includes clinically relevant data.
Examples of output tables are available in the output directory in this repository.

## License:

GPLv2


## Found a bug?

Or maybe just wanto to drop some feedback? Just open an issue on github!