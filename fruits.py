import csv
import number
with open('number.csv') as file1,open('fruits.csv') as file2:
	reader1=csv.reader(file1)
	reader2=csv.reader(file2)
	line=[l for l in reader2]
	i=0
	x=0
	if 3 in number.lines:
		print ('true')
	for l in line:
		for k in l:
			b=i+x
			if b in number.lines:
				print("Entered if...")
				j=0
				z=i-1
				while j<10:
					if z<0:
						z-=100
					if l[z]!='':
						z=z-1
						j=j+1
				print z
				l[i]=l[z]
			else:
				l.pop(i)
				x=x+1
			i=i+1
	print line
						
			
