# Dictionary = {
#     "name":"Sushant",
#     "age":17,
#     "Class 12th percentage":89.75
# }

# dict = {"name":"sushant",
# "age":17,
# "percentage": 89.91,
# "Education": "Undergrad"}

# x = dict.keys()
# y = dict.values()
# print(x,"\n",y)

dict={
    "class":{
        "student":{
            "name":"Aditya",
            "marks":{
                "python":90,
                "web":95
            }
        }
    }
}
print(dict["class"]["student"]["marks"]["web"])
