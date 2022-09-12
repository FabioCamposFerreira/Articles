# Python 3
# Author: Fábio Campos

# The Python types are numbers (int, float, complex), string, list,

# int
int1 = -1.99
print("int1 = "+int1)
int1 = 2.99e10         # Exponent notacion
print("int1 = "+int1)
print("\n")

# float
float1 = 2.99
print("float1 = "+float1)
print("2 + 3 = "+2 + 3)    # Sum
print("2 - 3 = "+2 - 3)    # Diference
print("2 * 3 = "+2 * 3)    # Multiplication
print("2 / 3 = "+2 / 3)    # Division
print("2 // 3 = "+2 // 3)  # Integer Division
print("2 % 3 = "+2 % 3)    # Rest of the division (modulo)
print("2 ** 3 = "+2 ** 3)  # Potencia
print("\n")

# complex
complex_number = 4+5j
print("complex_number = "+complex_number)
print("complex_number.real() = "+complex_number.real())            # Part real
print("complex_number.imag() = "+complex_number.imag())            # Part imagine
print("complex_number.conjugate() = "+complex_number.conjugate())  # Conjugate
print("\n")

# String
text = "This is a string!"
print("text = "+text)
print("text[0:3] = "+text[0:3])
print("text[1:] = "+text[1:])
print("Firts,"+text+", ok?")                                                                                           # Concatenation
print("Integer %d inside of the string" % (123))                                                                       # Interpolation with int
text_interpolate = "entire = {0}; floating_point = {1}; text = {}"                                                    
print("text_interpolate.format(123,1.23, text) = "+text_interpolate.format(123, 1.23, text))                           # Interpolation with format()
print("text.upper() = "+text.upper())                                                                                  # Uppercase
print("3*text = "+3*text)
print("\n")

# List
list_example = [123, 1.23, 4+j5, "This is a string!", 'text1', "text2", 1, 1.5, 6+7j]
print("list_example = "+list_example)
print("list_example[1:] = "+list_example[1:])
list_example[-1] = 24                  # Change elemento position -1 (last elemente) to 24
print(list_example.pop(0))             # Remove and return firt element
print("list_example = "+list_example)
print(list_example.pop())              # Remove and return last element
print("list_example = "+list_example)
list_example.append("Added text!")     # Add element
print("list_example = "+list_example)
list_example.remove("entire")          # Remove element
print("list_example = "+list_example)
list_example.sort()                    # Sorting list
print("list_example = "+list_example)
list_example.reverse()                 # Reverte list
print("list_example = "+list_example)
print("\n")

# Tuple
tuple_example = (123, 1.23, 4+j5, "This is a string!", 'text1', "text2", 1, 1.5, 6+7j,list_example)
print(tuple_example)
print("tuple_example[0] = "+tuple_example[0])        # First element
print("tuple(list_example) = "+tuple(list_example))  # list to tuple
print("list(tuple_example) = "+list(tuple_example))  # tuple to list
tuple_example[-1].append(100)                        # Add 100 element in the list inside tuple (interative mode)
print(tuple_example)

# set and frozenset
set_example1 = set(1,1, 3, 2,4,5,'abc')
set_example2 = set("a","b","c","d","e",123, 'abc')
print("set_example1 = "+str(set_example1))
print("set_example2 = "+str(set_example2))
print("set_example1.union(set_example2) = "+str(set_example1.union(set_example2)))                # Union between set_example1 and set_example2
print("set_example1.difference(set_example2) = "+str(set_example1.difference(set_example2)))      # Difference between set_example1 and set_example2
print("set_example1.intersection(set_example2) = "+str(set_example1.intersection(set_example2)))  # Intersection between set_example1 and set_example2
print("set_example1.issuperset([1,2]) = "+str(set_example1.issuperset([1,2])))                     # Test if set_example1 incluide apresenta the elements [1,2]
print("set_example1.isdisjoint(set_example2) = "+str(set_example1.isdisjoint(set_example2)))      # Test if set_example1 and set_example2 do not have common elements

# Dictionaries
dic = {"1":"a", "2":"b", "3":"c", "union": "abc", "list_":[1,2,3]}
print("dic = "+str(dic))
print("dic[\"union\"] = "+str(dic["union"]))  # Accesing element
print("dic.items() = "+str(dic.items()))      # Get items
print("dic.keys() = "+str(dic.keys()))        # Get keys
print("dic.values() = "+str(dic.values()))    # Get values
# deleting element
del dic['2']                                  
print("dic = "+str(dic))
# sparse matrix
dic2 = {}                                     
dic2[1,1]=2
dic2[3,3]=4
print("dic2 = "+str(dic2))

# Booleans
true_ = True
false_ = False
print("true_ = "+str(true_))
print("false_ = "+str(false_))
print("False and True = "+str(False and True ))  # operator "and"
print("False or True = "+str(False or True ))    # operator "or"
print("not True = "+str(not True))               # operator "Not" 
print("2 is 2 = "+str(2 is 2))               
print("2 in [1,2,3] = "+str(2 in [1,2,3]))               

