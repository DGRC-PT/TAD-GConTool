def get_dd2p(infile):
	f=open(infile)
	dd2p={}
	for i in f:
		line=i.split(",")
		if line[0] not in dd2p:
			dd2p[line[0]]=[[],[],[],[],[]]
		dd2p[line[0]][0].append(line[4])
		dd2p[line[0]][1].append(line[3])
		dd2p[line[0]][2].append(line[2])	
		if len(line[9])>5:
			ch=line[9].split(";")
			el=ch[:2]
			if len(el)==2:
				dd2p[line[0]][3].append('=HYPERLINK("https://www.ncbi.nlm.nih.gov/pubmed/'+el[0]+'","'+el[0]+'")')
				dd2p[line[0]][4].append('=HYPERLINK("https://www.ncbi.nlm.nih.gov/pubmed/'+el[1]+'","'+el[1]+'")')
			elif len(el)==1:
				dd2p[line[0]][3].append('=HYPERLINK("https://www.ncbi.nlm.nih.gov/pubmed/'+el[0]+'","'+el[0]+'")')
				dd2p[line[0]][4].append('na')
			else:
				dd2p[line[0]][3].append('na')
				dd2p[line[0]][4].append('na')
		elif len(line[9])<6:
			dd2p[line[0]][3].append('na')
			dd2p[line[0]][4].append('na')

	f.close()
	return dd2p
	
def read_panel_list(infile):
	f=open(infile)
	panel=set()
	for i in f:
		line=i.strip()
		panel.add(line)
	f.close()
	return panel

