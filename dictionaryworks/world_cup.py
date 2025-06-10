world_cup_winners = {
    "Australia": 6,   
    "India": 2,      
    "West Indies": 2,
    "Pakistan": 1,    
    "Sri Lanka": 1,   
    "England": 1,     
}



def get_value_by_key(key):

    return world_cup_winners.get(key)

most_wins=max(world_cup_winners,key=get_value_by_key)

print(most_wins)

least_wins_team=min(world_cup_winners,key=get_value_by_key)

least_win_count=world_cup_winners.get(least_wins_team)

for k,v in world_cup_winners.items():

    if v==least_win_count:

        print(k,v)

total_world_cup_count=sum(world_cup_winners.values())

print(total_world_cup_count)