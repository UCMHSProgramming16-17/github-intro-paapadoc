# open file
file = open('mylist.txt', 'w')
#write something in file
file.write(input("item")+ '\n')
file.write(input("item")+ '\n')
for n in range(10):
    file.write(str(n=1) + input('item')+ '\n')
#close file
file.close()