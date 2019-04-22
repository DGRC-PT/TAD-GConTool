#!/usr/bin/python2
import cgi
import os
import cgitb
from time import time, localtime, strftime
import datetime
import calendar

cgitb.enable()

clock=strftime("%a, %b %d %Y %H:%M:%S", localtime())

def index():
	""" Show the default page
	"""
	print 'content-type: text/html'
	print #Blank line to divide headers
	print '</html>'

index()

def printers(v1, v2):
        print 'content-type: text/html'
        print v1
        print v2

def showForm1():
	"""Show a form
	"""
	root = "/cgi-bin"
	processor = "bp2omim2/comand.py"
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

aaa {
  font-family:Arial;
  font-size:20px;
  line-height: 0.7;
}

rodape {
  font-family:Arial;
  font-size:17px;
}

#regForm {
  background-color: #ffffff;
  margin: 20px auto;
  font-family: Arial;
  font-size:20px;
  padding: 20px;
  width: 70%;
  min-width: 100px;
  line-height: 0.7;
}

h1 {
  text-align: center;  
}

button {
  font-family: Arial;
}

input {
  padding: 10px; 
  font-size: 20px;
  font-family: Arial;
  border: 1px solid #aaaaaa;
  line-height: 0.5;
}

/* Mark input boxes that gets an error on validation: */
input.invalid {
  background-color: #ffdddd;
}

/* Hide all steps by default: */
.tab {
  display: inline;
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
  display: inline;
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
<br><br />
<center><img src="https://cld.pt/dl/download/c3ba7b53-2d29-46fa-a2e0-c6dfbf2310e9/banner_HMSP.jpeg" width=622 height=153 border=0 alt=""><br><br />
<head>
<center><title>TAD-GConTool</title></center>
</head>
<aaa>
<center><h1>TAD-Gene Content Tool (TAD-GConTool) </h1></center>
<center><p><b>This tool was developed to support prediction of the phenotypic outcome of chromosomal or genomic structural variants</b></p></center>
<center><p><b>(unbalanced and balanced translocations, inversion, insertion, deletions, duplications or of a specific genomic region).</b></p></center>
<center><p>The tool, based on the genomic position of the breakpoints, identifies the Topologically Associated Domains (TADs) from the breakpoint regions</b></p></center>
<center><p>and retrieves series protein-coding and non-coding RNA genes and genomic elements found within these domains and associated structural and functional information.</b></p></center>
<center><p>For each breakpoint, the retrieved data is compiled in a complete table that includes all acquired information and a report table that mainly includes clinically relevant data.</p></center><br>
</aaa>
<body>
<form id="regForm" method=POST action="bp2omim/results.py">
  <h1>Input Form</h1><br>
  <br />
  <!-- One "tab" for each step in the form: -->
  <div class="tab" > <center> <b>Reference genome assembly:</b><br>
  <br />
    <p><input type="radio" value="hg19" name="version" style="margin-right: 10">Hg19 </p>
    <p><input type="radio" value="hg38" name="version" style="margin-right: 10">Hg38</p></center><br>
    <br />
  </div>
  <div class="tab"> <center><b>Reference cell line:</b>
    <p><font color="grey" > Select one cell type only </font></p>
    <p><input type="radio" name="tad" value="IMR90" style="margin-right: 10" >IMR90 <font color="grey"> &ensp; (Dixon et al., 2012) </font> </p>
    <p><input type="radio" name="tad" value="LCL" style="margin-right: 10" >LCL <font color="grey"> &ensp; (Moore et al., 2015) </font> </p>
    <p><input type="radio" name="tad" value="hesc" style="margin-right: 10" >hESC <font color="grey"> &ensp; (Dixon et al., 2012) </font></p></center><br>
    <br />
  </div>
  <div class="tab"><b> <center> Select additional TADs to be included in the report table:</b>
    <p> <font color="grey" > By default, the three TADs are incorporated in the complete table whereas only the brTAD is included in the report table. </font> </p>
    <p><input type="checkbox" name="tads[]" value="TAD-1_" style="margin-right: 10"  >TAD-1</p>
    <p><input type="checkbox" name="tads[]" value="brTAD_" checked onclick="return false;" style="margin-right: 10" >brTAD</p>
    <p><input type="checkbox" name="tads[]" value="TAD+1_" style="margin-right: 10">TAD+1</p></center><br>
    <br />
  </div>
  <div class="tab" ><center><b>Select type of alteration to be analysed:</b>
    <p><select style="padding:10px; font-size: 18px; font-family: Arial;" name="tt" form="regForm" onchange="yesnoCheck(this);"></p>
      <option value="">Select</option>
      <option value="Specific_region">Specific genomic region</option>
      <option value="Balanced_translocation">Balanced translocation</option>
      <option value="Inversion">Inversion</option>
      <option value="Deletion">Deletion</option>
      <option value="Duplication">Duplication</option>
      <option value="Insertion">Insertion</option>
      <option value="Unbalanced_translocation">Unbalanced translocation</option></center>
      </select>
  </div>
      <div id="ifmeh" style="display: none;"> <b>Fill the form with chromosome and breakpoint information:</b>
        <p><font color="grey" > This tools accepts coordinates or intervals, with or without commas.</p></font>
        <p><font color="grey" > When given an interval, if the interval is greater than 1 kb, the tool interprets the given region as a deletion near the breakpoint.</p></font>
        <p><b>Chromosome A: <input type="text" size="50" name="chrA" placeholder="e.g. 6"/></p>
        <p>Breakpoint A:<input type="text" size="50" name="brA" placeholder="e.g. 168529498 or 168,529,498"/></p
         <p>Deletion <input type="checkbox" name="vvv" value="del">
        Duplication <input type="checkbox" name="vvv" value="dup"></p>       
        <p><b>Chromosome B: <input type="text" size="50" name="chrB" placeholder="e.g. 11"/></p>
        Breakpoint B: <input type="text" size="50" name="brB" placeholder="e.g. 116,812,107-116,912,603 or 116812107-116912603"/></p></b>
        <p>Deletion <input type="checkbox" name="ddd" value="del">
        Duplication <input type="checkbox" name="ddd" value="dup"></p>
      </div>
      <div id="ifins" style="display: none;"> <b>Fill the form with chromosome and insertion information:</b>
        </b><p><font color="grey" > This tools accepts coordinates or intervals, with or without commas.</p></font>
        <p><font color="grey" > When given an interval, if the interval is greater than 1 kb, the tool interprets the given region as a deletion near the breakpoint.</p></font>
        <p><b>Donor Chromosome: <input type="text" size="50" name="chrA" placeholder="e.g. 11"/></p>
	    <p><b>Recipient Chromosome: <input type="text" size="50" name="chrB" placeholder="e.g. 6"/></p>
	    <p>Inserted region: <input type="text" size="50" name="brA" placeholder="e.g. 116812107-116912603 or chr11:116,812,107-116,912,603"/></p>
	    <p>Recipient Breakpoint: <input type="text" size="50" name="brB" placeholder="e.g. 168529498 or chr6:168,529,498"/></p></b>
      </div>
      <div id="ifno" style="display: none;"> <b>Fill the form with chromosome and breakpoint information:</b>
       </b> <p><font color="grey" > This tools accepts coordinates or intervals, with or without commas.</p></font>
       <p><font color="grey" > When given an interval, if the interval is greater than 1 kb, the tool interprets the given region as a deletion near the breakpoint.</p></font>
        <p><b>Chromosome: <input type="text" size="50" name="chrA" placeholder="e.g. 6"/></p>
	    <p>Breakpoint A: <input type="text"size="50"  name="brA" placeholder="e.g. 168529498 or chr6:168,529,498"/></p>
        <p>Breakpoint B: <input type="text" size="50" name="brB" placeholder="e.g. chr6:116812107-116912603 or 116,812,107-116,912,603"/></p></b>
      </div>
      <div id="ifYes" style="display: none;"> <b>Fill the form with chromosome and breakpoint information:</b>
       </b> <p><font color="grey" > This tools accepts coordinates or intervals, with or without commas.</p></font>
       <p><font color="grey" > When given an interval, if the interval is greater than 1 kb, the tool interprets the given region as a deletion near the breakpoint.</p></font>
        <p><b>Chromosome A: <input type="text" size="50" name="chrA" placeholder="e.g. 6"/></p>
        <p><b>Chromosome B: <input type="text" size="50" name="chrB" placeholder="e.g. 11"/></p>
	    <p>Breakpoint A: <input type="text" size="50" name="brA" placeholder="e.g. chr6:168529498 or 168,529,498"/></p>
        <p>Breakpoint B: <input type="text" size="50" name="brB" placeholder="e.g. chr11:116812107-116,912,603 or 168,529,498"/></p></b>
      </div>
      <script>
      function yesnoCheck(that){
       if (that.value == "Balanced_translocation") {
         document.getElementById("ifYes").style.display = "block";
         document.getElementById("ifno").style.display = "none";
         document.getElementById("ifmeh").style.display = "none";
         document.getElementById("ifins").style.display = "none";
       } else if (that.value == "Unbalanced_translocation") {
         document.getElementById("ifYes").style.display = "none";
         document.getElementById("ifno").style.display = "none";
         document.getElementById("ifmeh").style.display = "block";
         document.getElementById("ifins").style.display = "none";
       } else if (that.value == "Insertion") {
         document.getElementById("ifYes").style.display = "none";
         document.getElementById("ifno").style.display = "none";
         document.getElementById("ifmeh").style.display = "none";
         document.getElementById("ifins").style.display = "block";
       } else if (that.value == "") {
         document.getElementById("ifYes").style.display = "none";
         document.getElementById("ifno").style.display = "none";
         document.getElementById("ifmeh").style.display = "none";
         document.getElementById("ifins").style.display = "none";
       } else {
         document.getElementById("ifno").style.display = "block";
         document.getElementById("ifYes").style.display = "none";
         document.getElementById("ifmeh").style.display = "none";
         document.getElementById("ifins").style.display = "none";
       }
     }
</script>
<center><p><input type="submit" value="Submit"/p></center></b><br>
<br />
</form>
<aaa><center>If you using this tool please acknowledge either by <i>This table was performed by the TAD-GConTool</i> or by citing <a href="http://www.insa.min-saude.pt/category/areas-de-atuacao/genetica-humana/">our reference publication</a></center><br><br />
<b><center><a href=/tadgctV2_tutorial.pdf>Reference manual</a></center></b><br><br />
<center><address>
Correspondance: <a href="mailto:doencasgenomicas@insa.min-saude.pt">Genomic Diseases Group</a>.<br><br />
</address>
<center><aaa><a href="http://www.insa.min-saude.pt/category/areas-de-atuacao/genetica-humana/">Department of Human Genetics</a></aaa></center><br>
<p>National Institute of Health Doutor Ricardo Jorge</p> </aaa></center>
<center><img src="https://cld.pt/dl/download/1f715328-21eb-49bd-b04c-b46bf2f08c61/aaa.jpg" width=641 height=122 border=0 alt=""><br><br />
<center><p><rodape>This file was last modified 13/12/2018</p></font></rodape>
</body>
</html>"""

showForm1()

