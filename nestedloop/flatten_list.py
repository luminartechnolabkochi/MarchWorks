
parent_list=[
    [10,20,[1,3]],
    [11,[20,51,37]],
    [12,22,13,53],
]

flatten_list=[]#10,20

for collection in parent_list:
    #collection= [10,20,[1,3]],

    for el in collection:
        #el=[1,3]

        if type(el)==list:            
            for n in el:
                flatten_list.append(n)

        else:
            flatten_list.append(el)
print(flatten_list)













