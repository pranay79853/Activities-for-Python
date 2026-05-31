dict1 = {
    "Student1": {
    "Name" : "Virat",
    "Scores" : 87
},

"Student2":{
    "Name" : "Rahul",
    "Scores" : 91
},

"Student3":{
    "Name" : "Abhishek",
    "Scores" : 97
},

"Student4":{
    "Name" : "Eshan",
    "Scores" : 71
},

"Student5":{
    "Name" : "Pranay",
    "Scores" : 100
},
}

total = 0

for i in dict1:
    total = total + dict1[i]["Scores"]
average = total // len(dict1)
print(average)
top_scorer = max(dict1)
bottom_scorer = min(dict1)
student = dict1.get("Student1")
print(student.get("Name"))
for i in dict1:
    student = dict1.get(i)
    print(student.get("Name"), "-", student.get("Scores"))