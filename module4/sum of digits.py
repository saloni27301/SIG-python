print("Saloni \n180301020")
n=int(input("Enter number:"))
sum=0
while(n>0):
    rem=n%10
    sum=sum+rem
    n=n//10
print("\n sum of the digits =%d" %sum)