print("Saloni (1803010120)")
def returnSum(myDict):
    sum = 0
    for i in myDict:
        sum = sum + myDict[i]

    return sum
dict = {'a': 1000, 'b': 900, 'c': 600}
print("Sum :", returnSum(dict))