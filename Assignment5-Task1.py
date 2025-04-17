#list --->[] index value

#Dictionary ----> key and value pair ----> {'key' : 'value'}

students = {"Shivraaj": 89,"Atharv":90,"Rohan":50,"Sumit":70}

name = input('Enter the name of the student')

if name in students:
    print(f"{name}'s marks :, {students[name]}")
else:
    print("Student name Anot found")