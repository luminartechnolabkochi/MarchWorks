
from json import load

file_path="C:\\Users\\Luminar\\Desktop\\MarchPythonWorks\\json_works\\countries.json"


with open(file_path,"r",encoding="utf-8") as fr:

    data=load(fr)



# display all countries name

all_country_name=[c.get("name") for c in data]
# print(all_country_name)
# display name of most populated country

# def get_population(country_dictionary):

#     return country_dictionary.get("population")
# most_populated_country=max(data,key=get_population)
# print(most_populated_country.get("name"))
# # display name of least_populated_country




# lest_populated_country=min(data,key=lambda dictionary:dictionary.get("population"))
# print(lest_populated_country.get("name"))
# # display indepenedent country names
# independent_country_names=[c.get("name") for c in data if c.get("independent")==True]
# print(independent_country_names)
# display all regions

all_regions={c.get("region") for c in data}
# print(all_regions)
# display asian countries

asian_countries=[c.get("name") for c in data if c.get("region")=="Asia"]
print(asian_countries)
# display indian borders

indian_borders=[c.get("borders") for c in data if c.get("name")=="India"][0]


indian_border_names=[c.get("name") for c in data if c.get("alpha3Code") in indian_borders]

# print(indian_border_names)


country_languages=[l.get("name") for c in data for l in c.get("languages") if c.get("name")=="India"]



print(country_languages)


# which region has highest number of countries?

region_count={}#Asia:2

for c in data:

    region=c.get("region")

    region_count[region]=region_count.get(region,0)+1

print(region_count)







