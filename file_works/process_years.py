

# all_years.txt
# century_years.txt
# non_century_years.txt

all_years_path="C:\\Users\\Luminar\\Desktop\\MarchPythonWorks\\file_works\\all_years.txt"
century_years_path="C:\\Users\\Luminar\\Desktop\\MarchPythonWorks\\file_works\\century_years.txt"
non_century_years_path="C:\\Users\\Luminar\\Desktop\\MarchPythonWorks\\file_works\\non_century_years.txt"

f_all_year=open(all_years_path,"r")

f_century=open(century_years_path,"w")

f_non_century=open(non_century_years_path,"w")


for line in f_all_year:
    #line="1800"
    year=int(line.rstrip("\n"))

    if year%100==0:

        f_century.write(str(year)+"\n")
    else:
        f_non_century.write(str(year)+"\n")



d_year=int("1800\n")

print(d_year)
f_non_century.close()
f_all_year.close()
f_century.close()
