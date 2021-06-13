print("1803010120 Saloni")
def Appendtext(fname):
	with open(fname,'a+') as f:
		f.write('appending line 1, ')
		f.write('appending line 2. ')
	f.close()
Appendtext('file1.txt')

x= open('../python/file1.txt')
print(x.read())