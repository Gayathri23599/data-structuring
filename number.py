import csv
with open('number.csv') as csvfile:	
	reader=csv.reader(csvfile)
	lines=[l for l in reader]
	i=0
	j=0
	t=0
	for l in lines:
		for k in l:
			if k=='':
				z=i+j
				if z%2==0:
					l.pop(i)
					j=j+1
				else:
					l[i]=i+j
			i=i+1
with open('number.csv','w') as csvfile:
	writer=csv.writer(csvfile)
	writer.writerows(lines)
		

		
