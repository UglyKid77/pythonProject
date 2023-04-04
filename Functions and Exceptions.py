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

