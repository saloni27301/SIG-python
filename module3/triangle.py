print("SALONI (180301020)")
print('Enter length of the triangles')
x=int(input("Enter x:"))
y=int(input('Enter y:'))
z=int(input("Enter z:"))
if x==y==z:
    print("Equilateral triangle")
elif x==y or y==z or z==x:
    print("Isosceles triangle")
else:
    print("Scalene triangle")