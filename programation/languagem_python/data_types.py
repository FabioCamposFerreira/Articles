#----------------------
# List

# Add list
numbers = [1,2,3,4,5]
numbers_str = ["1","2","3"]
numbers.append(numbers_str)
print(numbers)
# ??

numbers = [1,2,3,4,5]
numbers += [numbers_str]
print(numbers)
# ??

#----------------------------
# Numpy

# Reduce dimension
a = np.array([[1,2,3],[4,5,6]])
a_v = np.vstack(a)
print(a_v)
# ??
a_h = np.hstack(a)
print(a_v)
# ??
