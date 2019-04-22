#!/usr/bin/env Rscript
#.libPaths() 
#.libPaths("/home/joanafino/R/x86_64-pc-linux-gnu-library/3.3/httr")
#.libPaths()

args = commandArgs(trailingOnly=TRUE)
library("httr")
res <- GET(args)
cont <- content(res)
aa<-paste(cont, collapse=", ")
grepl("not found" , aa)
