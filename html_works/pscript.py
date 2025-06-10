person = {
    "data1": { "name": "aa", "age": 45, "place": "kottayam" },
    "data2": { "name": "bb", "age": 50, "place": "tvm" },
    "data3": { "name": "cc", "age": 60, "place": "knr" }
}


# // print the person name of age greaterthen 50

for p in person:
    if (person[p]["age"]>50):

        print(person[p]["name"])
        
    
    