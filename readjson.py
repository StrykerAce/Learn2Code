import json

with open('test.json') as progressfile:
    data = json.load(progressfile)
    print(type(data))
    print("\n")
    print(data)
    print("\n")
    print([element["Description"] for element in data]) 
    