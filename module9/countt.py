print("Saloni 1803010120")
def countlines(fname,mode='r+'):
	count=0
	with open(fname) as f:
		for _ in f:
			count += 1
	print('total number of lines in file : ',count)

countlines('file1.txt')