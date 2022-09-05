import string

def list_mix(list):
         simple_list = []
         for i in list:
                  simple_list += i
         return simple_list

number = []

for i in range(1,101):
         number.append(i)
letter = string.ascii_lowercase

print (list_mix([number, letter]))
