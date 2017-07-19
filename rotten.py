import csv
with open('rotten.csv') as csvfile:
	reader=csv.reader(csvfile)
	lines=[l for l in reader]
	i=0
	for l in lines:
		for k in l:
			if k=='1':
				l[i]='t'
			elif k=='0':
				l[i]='f'
			i=i+1
with open('rotten.csv','w') as csvfile:
	writer=csv.writer(csvfile)
	writer.writerows(lines)
