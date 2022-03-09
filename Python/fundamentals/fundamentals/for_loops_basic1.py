#Basic
count = 0
while count <= 150:
    print(count)
    count+=1

#Multiples of 5
for x in range(5, 1005, 5):
    print(x)

#Counting the Dojo Wy
for a in range(1,101):
    if(a%10==0):
        print("Coding Dojo")
    elif(a%5==0):
        print("Coding")
    else:
        print(a)

#Whoa. That Sucker's Huge
b=1
sum = 0
while b<=500000:
    sum = b+sum
    b+=2
    if b == 0:
        break
else:
    print(sum)
    
#Countdown by Fours
y=2018
while y > 0:
    print(y)
    y = y - 4
    if y == 0:
        break

#Flexible Counter
lowNum = 2
highNum = 9
mult = 3

for f in range(lowNum, highNum + 1):
    if f % mult == 0:
        print(f)