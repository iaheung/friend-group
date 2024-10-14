"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group = [
        {'name': 'Jill', 'age':26, 'job':'Biologist','connection': [('friend','Zalika'),('partner','John')]},
        {'name': 'Zalika', 'age':28, 'job':'artist','connection': [('friend','Jill')]},
        {'name': 'John', 'age':27, 'job':'writer','connection': [('partner','Jill')]},
        {'name': 'Nash', 'age':34, 'job':'chef','connection': [('landlord','Zalika'),('cousin','John')]}
    ]

def max_age(my_group):
    maxAge = -1
    for i in range(len(my_group)):
        age = my_group[i]['age']
        if maxAge < age:
            maxAge = age
    return maxAge

def mean_relations(my_group):
    num_relations = 0
    for i in range(len(my_group)):
        num_relations += len(my_group[i]['connection'])
        
    return num_relations / len(my_group)

def max_age_with_relation(my_group):
    maxAge = -1
    for i in range(len(my_group)):
        age = my_group[i]['age']
        if maxAge < age and len(my_group[i]['connection']) > 0:
            maxAge = age
    if maxAge == -1:
        return None
    return maxAge

def max_age_with_friend(my_group):
    maxAge = -1
    for i in range(len(my_group)):
        age = my_group[i]['age']
        if maxAge < age and len(my_group[i]['connection']) > 0:
            for j in range(len(my_group[i]['connection'])):
                if my_group[i]['connection'][j][0] == 'friend':
                    maxAge = age
    if maxAge == -1:
        return None
    return maxAge

print("Max Age: ", max_age(my_group))
print("Mean Relations: ", mean_relations(my_group))
print("Max Age with Connection: ", max_age_with_relation(my_group))
print("Max Age with Friend: ", max_age_with_friend(my_group))

             
