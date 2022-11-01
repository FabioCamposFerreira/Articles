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
# Dictionary
## Clone dict key only
d = {"numbers":[1,2,3,4],"letters":['a','b',"c","d","e"]}
d_2 = dict.fromkeys(self.methods.keys(),[])
print(d_2)
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
# Set array
np.unique(a)
# ??

# Filter and replace
a=np.array([0,1,2,3,4])
a[a>2] = 10
# ??

# Histrogram
a=np.array([0,3,5,7,3])
u, i = np.unique(a, return_inverse=True)
print(u)
# ??
