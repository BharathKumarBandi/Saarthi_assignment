dict1 = {'a': 100, 'b': 200, 'c':300}
dict2 = {'a': 300, 'b': 200, 'd':400}  
# adding the values with common key
for key in dict2:
    if key in dict1:
        dict1[key] = dict2[key] + dict1[key]
    elif key not in dict1:
        dict1[key]= dict2[key]
        
          
print(dict1)
