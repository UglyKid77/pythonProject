### LIST   [0,...,n]

top = ['Amsterdam','Berlin','Madrid','Colonia','Santander']

print(top[3])
print(top[-1])
print(top[0:3])

del top[3]
print(top)

top.append('Praga')
print(top)
top.insert(3,'Colonia')
print(top)

for index in top:
    print('city: ', index)

first = 10    #swaping positions
second = 20
first, second = second, first
print(first, second)

top[0],top[1] = top[1],top[0]
print(top)

top.sort()   #sort in alphatic/numeric order, not easy to reverse
print(top)
top.sort(reverse=True)
print(top)
top = ['Prage','Amsterdam','Berlin','Madrid','Colonia','Santander']
print(sorted(top))  #avoiding change the list

top_copy = top[:]   #collections only can be copied via slicing [:]
print(top)
print(top_copy)
                                      #List comprehensions
numbers = [i for i in range(1,101)]   #to build a 1 to 100 list
print(numbers)
numbers = [i for i in range(1,101) if i % 3 != 0] #exepto those divisible by 3
print(numbers)

cells = [[1,2,3],[8,9,10]] #nested lists
print(cells[0][1])

table = [[i for i in range(1,6)] for j in range(4)]  #creating a table
print(table)

#### String features

band = 'Iron Maiden'
print(band[5])
print(band[:5])

band_cap = band.upper()
print(band_cap)


#### Tuples