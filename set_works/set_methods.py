

# methods
# class set:
    #def add(object)
    #def union(set)
    #def intersection
    #def difference()




yuvi_friends={"sachin","dravid","sanju","rahul","rohit","kohli"}

dhoni_friends={"aswin","raina","dravid","jadeja","maxwell"}

all_users=yuvi_friends.union(dhoni_friends)

print(all_users)

mutual_friends=yuvi_friends.intersection(dhoni_friends)

print(mutual_friends)

friend_suggestions_dhoni=all_users.difference(dhoni_friends)

print(friend_suggestions_dhoni)







