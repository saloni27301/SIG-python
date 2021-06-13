print("1803010120 Saloni")
a_list = ["abc", "def", "ghi"]
f = open("../python/a_file.txt", "w")
for item in a_list:
   f.write(item + "\n")
f.close()