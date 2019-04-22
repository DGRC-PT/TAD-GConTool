#!/usr/bin/env python
#coding=UTF-8

#report table subscript
##############################################################
###Dependencies:
import sys
sys.path.append('/home/analise_liWGSseqs/software/biomart')
sys.path.append("/usr/lib/pymodules/python2.7/openpyxl")
sys.path.append("/usr/local/apache/cgi-bin/bp2omim")
import subprocess
from openpyxl import Workbook
from openpyxl.styles import Font, Fill, PatternFill
from openpyxl.styles.borders import Border, Side
import cgi
import cgitb
from biomart import BiomartServer
import urllib2
from urllib2 import Request, urlopen, URLError
from collections import OrderedDict
import time
import random
import report_tableV3beta2N
import genomicfeatV2
###HTML dealling

cgitb.enable()


def indesx():
        """ Show the default page
        """
        print 'content-type: text/html'
        print #Blank line to divide headers
        print '</html>'

indesx()


def index():
	#print 'Content-type: text/html; charset=utf-8'
	print """
 <html>
 <meta name="viewport" content="width=device-width, initial-scale=1.0">
<link href="https://fonts.googleapis.com/css?family=Arial" rel="stylesheet">
<style>
* {
  box-sizing: border-box;
}

body {
  background-color: #f1f1f1;
}

#regForm {
  background-color: #ffffff;
  margin: 80px auto;
  font-family: Arial;
  padding: 40px;
  width: 70%;
  min-width: 300px;
}

hgh {
  text-align: center;
  font-family: Arial;
}

h1 {
  text-align: center;
  font-family: Arial;
}

head2 {
  padding: 10px;
  width: 100%;
  font-size: 17px;
  font-family: Arial;
  border: 1px solid #aaaaaa;
}

button {
  font-family: Arial;
}

input {
  padding: 10px;
  width: 100%;
  font-size: 17px;
  font-family: Arial;
  border: 1px solid #aaaaaa;
}

/* Mark input boxes that gets an error on validation: */
input.invalid {
  background-color: #ffdddd;
}

/* Hide all steps by default: */
.tab {
  display: block
}

.nn {
  display: none;
}

button:hover {
  opacity: 0.8;
}

#prevBtn {
  background-color: #bbbbbb;
}

/* Make circles that indicate the steps of the form: */
.step {
  height: 15px;
  width: 15px;
  margin: 0 2px;
  background-color: #bbbbbb;
  border: none;  
  border-radius: 50%;
  display: inline-block;
  opacity: 0.5;
}

.step.active {
  opacity: 1;
}

/* Mark the steps that are finished and valid: */
.step.finish {
  background-color: #4CAF50;
}

input[type=checkbox]
{
  /* Double-sized Checkboxes */
  -ms-transform: scale(1.2); /* IE */
  -moz-transform: scale(1.2); /* FF */
  -webkit-transform: scale(1.2); /* Safari and Chrome */
  -o-transform: scale(2); /* Opera */
  padding: 10px;
}

</style>

<head>
<title>TAD-GConTool</title>
</head>
<body bgcolor="#f0f0f8">
</body>
</html>
        
"""



def take_space_coma(val):## vai para o command.py
	aa=val.strip(" ")
	if ":" in aa:
		ss=aa.split(":")[1]
	else:
		ss=aa
	bb=ss.replace(",","")
	return bb

index()

def conr(form):
	tdds=[]
	ta=[]
	try:
		for i in form["tads[]"]:
			tdds.append(i.value)
			ta.append(i.value[:-1])
	except TypeError:
		tdds.append(form["tads[]"].value)
		ta.append(form["tads[]"].value[:-1])
	version=form["version"].value
	tadd=form["tad"].value
	tt=form["tt"].value
	if "ddd" in form:
		if form["ddd"].value =="A":
			der=form["chrA"].value
		else:
			der=form["chrB"].value
	else:
		der=""
	if version=="hg19":
		at1=[ 'start_position', 'end_position','external_gene_id', 'strand', 'mim_gene_accession', 'gene_biotype', 'ensembl_gene_id']
		at2=['description',  'start_position', 'end_position','external_gene_id', 'strand', 'mim_gene_accession', 'gene_biotype', 'ensembl_gene_id']
		if tadd=="IMR90":
			tad="IMR90 fibroblasts"
			tadfile="imr90_hg19.domain"
			ref="Dixon et al. 2012"
		elif tadd=="LCL":
			tad="LCL"
			tadfile="lcl_hg19.domain"
			ref="Moore et al. 2015"
		elif tadd=="hesc":
			tad="hESC "
			tadfile="hesc_hg19.domain"
			ref="Dixon et al. 2012"
	elif version=="hg38":
		at1=['start_position', 'end_position','external_gene_name', 'strand', 'mim_gene_accession', 'gene_biotype', 'ensembl_gene_id']
		at2=['description',  'start_position', 'end_position','external_gene_name', 'strand', 'mim_gene_accession', 'gene_biotype', 'ensembl_gene_id']
		if tadd=="IMR90":
			tad="IMR90 fibroblasts"
			tadfile="imr90_hg38.domain"
			ref="Dixon et al. 2012"
		elif tadd=="LCL":
			tad="LCL"
			tadfile="lcl_hg38.domain"
			ref="Moore et al. 2015"
		elif tadd=="hesc":
			tad="hESC "
			tadfile="hesc_hg38.domain"
			ref="Dixon et al. 2012"
	print '<br /><hgh><font size="5em;"><center><b> Input parameters: </hgh></center></b></font>'
	print '<hgh><p><b>Genome version: </b>'+ version+'</p></hgh>'
	print '<hgh><p><b>Reference: </b>'+ tad+'</p></hgh>'
	print '<hgh><p><b>TADs to analyse: </b>'+ ",".join(ta)+'</p></hgh>'
	print '<hgh><p><b>Type of alteration: </b>'+ tt.replace("_", " ")+'</p></hgh>'
	if tt=="Specific_region":
		chh=form["chrA"].value
		name11=time.strftime("analysed_region"+chh+"_"+form["version"].value+"_"+tadd+"_%d-%m-%Y_report_table.xlsx")
		name22=time.strftime("analysed_region"+chh+"_"+form["version"].value+"_"+tadd+"_%d-%m-%Y_complete_table.xlsx")
		outfile1=("/usr/local/apache/htdocs/"+name11)
		outfile2=("/usr/local/apache/htdocs/"+name22)
		print("<hgh><p><b>Chromosome: </b>"+chh+"</p></hgh>")
		print("<hgh><p><b>Region: </b>"+take_space_coma(form["brA"].value)+"-"+ take_space_coma(form["brB"].value)+"</p></hgh>")
		name1, name2= report_tableV3beta2N.main(tdds, at1, tad, tadfile, ref, outfile1, chh, "del", take_space_coma(form["brA"].value), take_space_coma(form["brB"].value), take_space_coma(form["version"].value), True, tt, der)
		genomicfeatV2.main(at2, tadfile, ref, outfile2, chh, "del", take_space_coma(form["brA"].value), take_space_coma(form["brB"].value), take_space_coma(form["version"].value), True, tt,der,tad)
		print '<hgh><font size="5em;"><center><p><b>Output:</center></b></p></hgh></font>'
	elif tt=="Deletion":
		chh=form["chrA"].value
		name11=time.strftime("del"+chh+"_"+form["version"].value+"_"+tadd+"_%d-%m-%Y_report_table.xlsx")
		name22=time.strftime("del"+chh+"_"+form["version"].value+"_"+tadd+"_%d-%m-%Y_complete_table.xlsx")
		outfile1=("/usr/local/apache/htdocs/"+name11)
		outfile2=("/usr/local/apache/htdocs/"+name22)
		print("<hgh><p><b>Chromosome: </b>"+chh+"</p></hgh>")
		print("<hgh><p><b>Deleted region: </b>"+take_space_coma(form["brA"].value)+"-"+ take_space_coma(form["brB"].value)+"</p></hgh>")
		name1, name2= report_tableV3beta2N.main(tdds, at1, tad, tadfile, ref, outfile1, chh, "del", take_space_coma(form["brA"].value), take_space_coma(form["brB"].value), take_space_coma(form["version"].value), False, tt, der)
		print '<hgh><font size="5em;"><center><p><b>Output:</center></b></p></hgh></font>'
		print("<hgh><p><b>Deletion: </b>"+name1+"</p></hgh>")
		genomicfeatV2.main(at2, tadfile, ref, outfile2, chh, "del", take_space_coma(form["brA"].value), take_space_coma(form["brB"].value), take_space_coma(form["version"].value), False, tt,der,tad)
	elif tt=="Duplication":
		chh=form["chrA"].value
		name11=time.strftime("dup"+chh+"_"+form["version"].value+"_"+tadd+"_%d-%m-%Y_report_table.xlsx")
		name22=time.strftime("dup"+chh+"_"+form["version"].value+"_"+tadd+"_%d-%m-%Y_complete_table.xlsx")
		outfile1=("/usr/local/apache/htdocs/"+name11)
		outfile2=("/usr/local/apache/htdocs/"+name22)
		print("<hgh><p><b>Chromosome: </b>"+chh+"</p></hgh>")
		print("<hgh><p><b>Duplicated region: </b>"+take_space_coma(form["brA"].value)+"-"+ take_space_coma(form["brB"].value)+"</p></hgh>")
		name1, name2= report_tableV3beta2N.main(tdds, at1, tad, tadfile, ref, outfile1, chh, "del", take_space_coma(form["brA"].value), take_space_coma(form["brB"].value), take_space_coma(form["version"].value), False, tt, der)
		print '<hgh><font size="5em;"><center><p><b>Output:</center></b></p></hgh></font>'
		print("<hgh><p><b>Duplication: </b>"+name1+"</p></hgh>")
		genomicfeatV2.main(at2, tadfile, ref, outfile2, chh, "del", take_space_coma(form["brA"].value), take_space_coma(form["brB"].value), take_space_coma(form["version"].value), False, tt,der,tad)
	elif tt=="Inversion":
		chrA=form["chrA"].value
		name11= time.strftime("inv"+chrA+"_"+form["version"].value+"_"+tadd+"_%d-%m-%Y_report_table.xlsx")
		name22= time.strftime("inv"+chrA+"_"+form["version"].value+"_"+tadd+"_%d-%m-%Y_complete_table.xlsx")
		outfile1=("/usr/local/apache/htdocs/"+name11)
		outfile2=("/usr/local/apache/htdocs/"+name22)
		print("<hgh><p><b>Chromosome: </b>"+chrA+"</p></hgh>")
		print("<hgh><p><b>Inverted region: </b>"+take_space_coma(form["brA"].value)+"-"+ take_space_coma(form["brB"].value)+"</p></hgh>")
		name1, name2= report_tableV3beta2N.main(tdds, at1, tad, tadfile, ref, outfile1, chrA, chrA, take_space_coma(form["brA"].value), take_space_coma(form["brB"].value), take_space_coma(form["version"].value), False, tt, der)
		print '<hgh><font size="5em;"><center><p><b>Output:</center></b></p></hgh></font>'
		print("<hgh><p><b>Rearrangement: </b>"+name1+"</p></hgh>")
		genomicfeatV2.main(at2, tadfile, ref, outfile2, chrA, chrA, take_space_coma(form["brA"].value), take_space_coma(form["brB"].value), take_space_coma(form["version"].value), False, tt,der,tad)
	elif tt=="Balanced_translocation":
		chrA=form["chrA"].value
		chrB=form["chrB"].value
		name11= time.strftime("t"+chrA+"_"+chrB+"_"+form["version"].value+"_"+tadd+"_%d-%m-%Y_report_table.xlsx")
		name22= time.strftime("t"+chrA+"_"+chrB+"_"+form["version"].value+"_"+tadd+"_%d-%m-%Y_complete_table.xlsx")
		outfile1=("/usr/local/apache/htdocs/"+name11)
		outfile2=("/usr/local/apache/htdocs/"+name22)
		print("<hgh><p><b>Chromosome A: </b>"+chrA+"</p></hgh>")
		print("<hgh><p><b>Chromosome B: </b>"+chrB+"</p></hgh>")
		print("<hgh><p><b>Breakpoint A: </b>"+take_space_coma(form["brA"].value)+"</p></hgh>")
		print("<hgh><p><b>Breakpoint B: </b>"+take_space_coma(form["brB"].value)+"</p></hgh>")#######################
		name1, name2= report_tableV3beta2N.main(tdds, at1, tad, tadfile, ref, outfile1, chrA, chrB, take_space_coma(form["brA"].value), take_space_coma(form["brB"].value), take_space_coma(form["version"].value), False, tt, der)
		genomicfeatV2.main(at2, tadfile, ref, outfile2, chrA, chrB, take_space_coma(form["brA"].value), take_space_coma(form["brB"].value), take_space_coma(form["version"].value), False, tt, der, tad)
		print '<hgh><font size="5em;"><center><p><b>Output:</center></b></p></hgh></font>'
		print("<hgh><p><b>Rearrangement A: </b>"+name1+"</p></hgh>")
		print("<hgh><p><b>Rearrangement B: </b>"+name2+"</p></hgh>")
	elif tt=="Insertion":
		chrA=form["chrA"].value
		chrB=form["chrB"].value
		name11= time.strftime("ins"+chrB+"_"+chrA+"_"+form["version"].value+"_"+tadd+"_%d-%m-%Y_report_table.xlsx")
		name22= time.strftime("ins"+chrB+"_"+chrA+"_"+form["version"].value+"_"+tadd+"_%d-%m-%Y_complete_table.xlsx")
		outfile1=("/usr/local/apache/htdocs/"+name11)
		outfile2=("/usr/local/apache/htdocs/"+name22)
		print("<hgh><p><b>Chromosome A: </b>"+chrA+"</p></hgh>")
		print("<hgh><p><b>Chromosome B: </b>"+chrB+"</p></hgh>")
		print("<hgh><p><b>Breakpoint A: </b>"+take_space_coma(form["brA"].value)+"</p></hgh>")
		print("<hgh><p><b>Breakpoint B: </b>"+take_space_coma(form["brB"].value)+"</p></hgh>")
		name1, name2= report_tableV3beta2N.main(tdds, at1, tad, tadfile, ref, outfile1, chrB, chrA, take_space_coma(form["brB"].value), take_space_coma(form["brA"].value), take_space_coma(form["version"].value), False, tt, der)
		print '<hgh><font size="5em;"><center><p><b>Output:</center></b></p></hgh></font>'
		print("<hgh><p><b>Rearrangement A: </b>"+name1+"</p></hgh>")
		print("<hgh><p><b>Rearrangement B: </b>"+name2+"</p></hgh>")
		genomicfeatV2.main(at2, tadfile, ref, outfile2, chrA, chrB, take_space_coma(form["brA"].value), take_space_coma(form["brB"].value), take_space_coma(form["version"].value), False, tt,der,tad)
	elif tt=="Unbalanced_translocation":
		chrA=form["chrA"].value
		chrB=form["chrB"].value
		name11= time.strftime("Unb_t"+chrB+"_"+chrA+"_"+form["version"].value+"_"+tadd+"_%d-%m-%Y_report_table.xlsx")
		name22= time.strftime("Unb_t"+chrB+"_"+chrA+"_"+form["version"].value+"_"+tadd+"_%d-%m-%Y_complete_table.xlsx")
		outfile1=("/usr/local/apache/htdocs/"+name11)
		outfile2=("/usr/local/apache/htdocs/"+name22)
		print("<hgh><p><b>Chromosome A: </b>"+chrA+"</p></hgh>")
		print("<hgh><p><b>Chromosome B: </b>"+chrB+"</p></hgh>")
		print("<hgh><p><b>Breakpoint A: </b>"+take_space_coma(form["brA"].value)+"</p></hgh>")
		print("<hgh><p><b>Breakpoint B: </b>"+take_space_coma(form["brB"].value)+"</p></hgh>")
		name1, name2= report_tableV3beta2N.main(tdds, at1, tad, tadfile, ref, outfile1, chrA, chrB, take_space_coma(form["brA"].value), take_space_coma(form["brB"].value), take_space_coma(form["version"].value), False, tt, der)
		print '<hgh><font size="5em;"><center><p><b>Output:</center></b></p></hgh></font>'
		print("<hgh><p><b>Rearrangement A: </b>"+name1+"</p></hgh>")
		print("<hgh><p><b>Rearrangement B: </b>"+name2+"</p></hgh>")
		genomicfeatV2.main(at2, tadfile, ref, outfile2, chrA, chrB, take_space_coma(form["brA"].value), take_space_coma(form["brB"].value), take_space_coma(form["version"].value), False, tt,der,tad)	
	print('<hgh><center><p><a href=/'+name11+'>Download report table!</center></a></p></hgh>')
	print('<hgh><center><p><a href=/'+name22+'>Download complete table!</center></a></p></hgh>')
	print('<aaa><center>If you using this tool please acknowledge either by <i>This table was performed by the TAD-GConTool</i> or by citing <a href="http://www.insa.min-saude.pt/category/areas-de-atuacao/genetica-humana/">our reference publication</a></center><br><br />')


def remake():
	print """
<html>

<body>

<center><hgh><button onclick="goBack()">New search</button></center></hgh>

<script>
function goBack() {
  window.location.replace("../TAD-GConTool.py");
}
</script>

</body>
</html>"""
	print('<br><br />')
	print('<b><center><a href=/tadgctV2_tutorial.pdf>Reference manual</a></center></b><br><br />')
	print('<center><address>Correspondance: <a href="mailto:doencasgenomicas@insa.min-saude.pt">Genomic Diseases Group</a>.<br><br /></address>')
	print('<center><aaa><a href="http://www.insa.min-saude.pt/category/areas-de-atuacao/genetica-humana/">Department of Human Genetics</a></aaa></center><br>')
	print('<p>National Institute of Health Doutor Ricardo Jorge</p> </aaa></center>')
	print('<center><img src="https://cld.pt/dl/download/1f715328-21eb-49bd-b04c-b46bf2f08c61/aaa.jpg" width=641 height=122 border=0 alt=""><br><br />')
	print('<center><p><rodape>This file was last modified 13/12/2018</p></font></rodape>')



