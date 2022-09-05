import re
import string

def matrix_sum(mat1,mat2):
                resul = [[ mat1[0][0]+mat2[0][0] , mat1[0][1]+mat2[0][1]] ,[mat1[1][0]+mat2[1][0] , mat1[1][1]+mat2[1][1]]]
                return resul 
def camel_case(s):
                lw = string.ascii_lowercase
                up = string.ascii_uppercase
                count = 0
                count2 = 0
                words = re.split('\s', s)
                for s in words:
                                for ch in lw:
                                                if s[0]==ch:
                                                                words[count2] = up[count]+s[1:]
                                                count = count+1
                                count = 0
                                count2+=1
                x =0
                y = len(words)
                result = ''
                while x< y:
                                result = result+ words[x]
                                x+=1
                return result
                                
#Era pra ser um modulo

#mat = [[56,78], [12,34]]
#mat_i = [[12,34], [56,78]]
#print (matrix_sum(mat,mat_i))

s = 'mais eficiente no uso de memória do que a concatenação convencional.'
print(camel_case(s))
