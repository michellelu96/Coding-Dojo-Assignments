num1 = 42 # variable declaration, number data type
num2 = 2.3 #varable declaration, numbers
boolean = True # variable declaration, boolean data type
string = 'Hello World' #variable declaration, string data
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable declaration, list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #varable declaration, dictionary
fruit = ('blueberry', 'strawberry', 'banana') #variable declaration, tuples
print(type(fruit)) # log statement
print(pizza_toppings[1]) #log statement
pizza_toppings.append('Mushrooms') #add value -list
print(person['name']) #log statement
person['name'] = 'George' #dictionary change value
person['eye_color'] = 'blue' #dictionary change value
print(fruit[2]) #log statement

if num1 > 45: #if conditional
    print("It's greater") #log statement
else: #else conditional
    print("It's lower") #log statement

if len(string) < 5: #if conditional
    print("It's a short word!") #log statement
elif len(string) > 15: #else if conditional
    print("It's a long word!") #log statement
else: #else conditional
    print("Just right!") #log statement

for x in range(5): #for loop start
    print(x) #log statement 
for x in range(2,5):#for loop start
    print(x)#log statement
for x in range(2,10,3): #for loop start
    print(x) #log statement
x = 0 #variable declaration
while(x < 5): #while statement., start
    print(x) #log statement
    x += 1 #while statement increment

pizza_toppings.pop()#decrease list
pizza_toppings.pop(1) #decrease list

print(person)#log statement
person.pop('eye_color') #decrease dictionary
print(person) #log statement

for topping in pizza_toppings: #for loop start
    if topping == 'Pepperoni': #if conditional
        continue #for loop continue
    print('After 1st if statement') #log statement
    if topping == 'Olives': #if conditional
        break #for loop break,

def print_hello_ten_times(): #function
    for num in range(10):#for loop start,function argument
        print('Hello') #log statement, function return

print_hello_ten_times()#function

def print_hello_x_times(x):#function
    for num in range(x):#for loop start, function argument
        print('Hello')#log statement, function return

print_hello_x_times(4)#function

def print_hello_x_or_ten_times(x = 10):#function
    for num in range(x):#for loop start, function argument
        print('Hello')#log statement,function return

print_hello_x_or_ten_times()#function
print_hello_x_or_ten_times(4)#function


"""
Bonus section
"""

# print(num3)#NameError: name <variable name> is not defined
# num3 = 72 
# fruit[0] = 'cranberry' TypeError: 'tuple' object does not support item assignment
# print(person['favorite_team']) KeyError: 'favorite_team'
# print(pizza_toppings[7])IndexError: list index out of range
#   print(boolean) IndentationError: unexpected indent
# fruit.append('raspberry') AttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1) AttributeError: 'tuple' object has no attribute 'pop'