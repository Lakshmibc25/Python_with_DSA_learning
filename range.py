start =(int (input("enter start number: ")))
end = int(input("enetr your end number: "))

s= 0
for i in range(start,end +1):
    print(i)
    s = s+i
print('sum = ', s)