### FUNCTIONS

def saludo():
    print('Hey you!')

saludo()

### Parameters

num_in = [5, 3, 7, 8, 10, 4]
def  get_average(nin):
    sum = 0.0
    for i in nin:
        sum += i
    average = sum / len(nin)
    print(average)

get_average(num_in)


nam = 'Nathalie'
def show_truth():
    nam = 'Vanessa'     #SHADOWING the variable (nam) content changes only inside the function, it stop working is a list is changed.
    print(nam)
show_truth()
print(nam)

def show_truth():
    global nam
    nam = 'Vanessa'     #Global makes the change to outside the function
    print(nam)
show_truth()
print(nam)

### RETURN keyword

def  get_average(nin):
    sum = 0.0
    for i in nin:
        sum += i
    average = sum / len(nin)
    return average

A = [5, 4, 6, 10, 7]
print(get_average(A))


### recursion

def get_factorial_recursive(number):
    if number <= 1:
        return 1
    return number * get_factorial_recursive(number -1)

print(get_factorial_recursive(3))

### generators

def get_number():
    for i in range(1, 4):
        yield i


print(get_number())
gen = get_number()
print(next(gen))
print(next(gen))
print(next(gen))

for x in get_number():
    print(x)

numbers = list(get_number())   #creating a list
print(numbers)

