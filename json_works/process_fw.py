
from json import load

file_path="C:\\Users\\Luminar\\Desktop\\MarchPythonWorks\\json_works\\frameworks.json"


with open(file_path,"r") as fr:

    data=load(fr)

    trending=[fw.get("name")for fw in data if fw.get("trending")==True]
    
    print(trending)


