dictionary_name = {'key': 'value',
                   'IDK':'I don\'t know',
                   'TBH': 'to be honest'}

print(dictionary_name['key'])

#dictionaries can hold any key and value pair. 

#adding new dictionary items or updating the value
dictionary_name["LOL"] = "laugh out loud"
print(dictionary_name)

#delete a key-value pair
del dictionary_name['IDK']
print(dictionary_name)

#none type
#none means the absence of a value, and evaluates to false in a conditional
definition = dictionary_name = dictionary_name.get('BTW')
#would return as none or false b/c it isn't in our list