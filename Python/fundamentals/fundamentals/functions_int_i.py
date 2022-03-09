#Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0]= 15

print(x)
students[0]["last_name"]="Bryant"
print(students)
sports_directory['soccer'][0]="Andres"
print(sports_directory)
z[0]["y"]=30
print(z)

#iterate through a list of dictionaries
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(dictionary):
    for x in range(len(dictionary)):
        first = dictionary[x]["first_name"]
        last=dictionary[x]["last_name"]
        string = f"first_name - {first}, last_name - {last}"
        print(string)


iterateDictionary(students) 

#get values from a list of dictionaries

def iterateDictionary2(name,list):
    for x in range(len(list)):
        print (list[x][name])

iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

#iterate through a dictionary with list values
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dict):
    for key in dict:
        print("-"*30)
        print(f"{len(dict[key])} {key.upper()}")
        for val in dict[key]:
            print(val)



printInfo(dojo)
