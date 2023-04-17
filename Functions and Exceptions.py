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
print(next(gen))   #'next' function to call the yieled (yield function) values one by one
print(next(gen))
print(next(gen))

for x in get_number():
    print(x)

numbers = list(get_number())   #creating a list
print(numbers)

#Exeptions intro

# try:
#     val = int(input('enter value (integer): '))
#     print('The inverted value is ', 1/val)
# except ValueError:
#     print('Not a number')
# except ZeroDivisionError:
#     print('Impossible to divide by 0')
# except:
#     print('Something wrong happened')
#

#Assertions

def calculate_inv(number):
      assert (number != 0), '0 is not valid'
      return 1/number

calculate_inv(0)



