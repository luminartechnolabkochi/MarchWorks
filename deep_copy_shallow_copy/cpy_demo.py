

manav_fvt_food=["biriyani"]

anoop_fvt_food=manav_fvt_food.copy()


print(manav_fvt_food == anoop_fvt_food) #== value 
print(manav_fvt_food is anoop_fvt_food)#chk two variables point in same object

import copy


manu_daily_foods=[ 
                        ["tea","idly"],
                        ["juice"],
                        ["alfham"]
                        
                ]


adarsh_daily_foods=copy.deepcopy(manu_daily_foods)

adarsh_daily_foods[0][0]="coffe"

print(adarsh_daily_foods)
print(manu_daily_foods)



