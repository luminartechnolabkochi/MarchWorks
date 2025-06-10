

file_path="C:\\Users\\Luminar\\Desktop\\MarchPythonWorks\\file_works\\all_years.txt"

f=open(file_path,"w")

for year in range(1800,2026):

    f.write(str(year)+"\n")

