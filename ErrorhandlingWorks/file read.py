


file_path="C:\\Users\\Luminar\\Desktop\\MarchPythonWorks\\ErrorhandlingWorks\\sample.txt"

try:
    with open(file_path,"r") as f:

        for line in f:

            print(line)
except Exception as e:
    print(e)

print("line 13")

print("line 15")