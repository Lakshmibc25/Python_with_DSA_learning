list= [89,45,64,32,10,27]
list_even = 0
list_odd = 0
for num in list:
    if num%2==0:
        list_even +=1
    else:
        list_odd +=1
print("even numbers count:",list_even)
print("odd numbers count:",list_odd)
    