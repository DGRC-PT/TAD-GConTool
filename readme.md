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
   