#!/usr/bin/env python
#coding=UTF-8
import comand
import sys
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
import report_tableV3beta2
import genomicfeatV2
###HTML dealling

def index():
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

hgh {
  text-align: center;
  font-family: Arial;
}

h1 {
  text-align: center;
  font-family: Arial;
}


</style>

<head>
<title>TAD-GConTool</title>
</head>
<body bgcolor="#f0f0f8">
<br><br />
<center><img src="https://cld.pt/dl/download/c3ba7b53-2d29-46fa-a2e0-c6dfbf2310e9/banner_HMSP.jpeg" width=622 height=153 border=0 alt=""><br><br />
<center><h1>TAD-Gene Content Tool - Search Results</h1></center>
<hgh><center><p>The retrieved data from each breakpoint is compiled in a complete table that includes all acquired information and a report table that mainly includes clinically relevant data</p></center></hgh>
<br /><hgh><center><b> While you wait for the results, please fill out our <a  href="https://goo.gl/forms/WKiyDJtXbXuSgDYG2" target="_blank">usage survey</a>. Thank you! </center></b></font><br>
<br /><center>Results will appear shortly...</center>
</body>
</html>
        
"""

index()
cgitb.enable()
form=cgi.FieldStorage()
comand.index()
comand.conr(form)
comand.remake()

