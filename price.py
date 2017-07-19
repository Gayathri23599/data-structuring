import csv
import rotten
with open('price.csv') as csvfile:
	reader=csv.reader(csvfile)
	line=[l for l in reader]
	i=0
	for l in line:
		for k in l:
			if rotten.lines[0][i]=='t':
				l[i]=0.0
			else:
				if k!='':
					l[i]=float(l[i])
				else:
					l[i]=0.0
			i=i+1
	print l

