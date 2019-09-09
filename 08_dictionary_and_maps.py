
"""Task
Given n  names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers.
You will then be given an unknown number of names to query your phone book for.
For each name queried, print the associated entry from your phone book on a new line in the form
name=phoneNumber; if an entry for name is not found, print Not found instead.

Note: Your phone book should be a Dictionary/Map/HashMap data structure."""

t = int(input())
phone_dict = {}
for i in range(0, t):
    name_phone_no = input()
    name, phone_no = str.split(name_phone_no)
    phone_dict.update({name:phone_no})

for k in range(0,t):
    name = input()
    if name in phone_dict:
        print("{}={}".format(name, phone_dict[name]))
    else:
        print("Not found")

