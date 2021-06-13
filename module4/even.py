print("SALONI\n 1803010120")
start=int(input("enter start digit:"))
end=int(input("Enter end digit:"))
for i in range(start,end+1):
    if(i%2==0):
        continue
    print(i,end=" ")