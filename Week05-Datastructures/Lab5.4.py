# Author: Cesaire Tchoudjuen

# Program that stores a student name and a list of her courses and grades in a dict

student = {
    "name":"Mary",
    "modules": [
        {
            "courseName":"Programming",
            "grades": 45
        },
        {
            "courseName":"History",
            "grades": 99
        }
    ]
}
print("Student: {}".format(student["name"]))
for module in student["modules"]:
    print("\t {} \t: {}".format(module["courseName"], module["grades"]))