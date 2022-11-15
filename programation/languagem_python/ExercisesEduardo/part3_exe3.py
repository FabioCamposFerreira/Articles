import time
#Gerador que produz tuplas com as cores do padrão RGB (R, G e B variam de 0 a 255) usando xrange()
def apos_gen():
    for r in range(0,255):
        for g in range(0,255):
            for b in range(0,255):
                yield ((r,g,b))

#Função que produz uma lista com as tuplas RGB usando range()
def tuples_rgb():
    tuples2= []
    for r in range(0,255):
        for g in range(0,255):
            for b in range(0,255):
                tuples2.append((r,g,b))  
    return tuples2                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   


# a = tuples_rgb()
# print(a[0])
# print(a[-1])
a=[]
for rgb in apos_gen():
    a.append(rgb)
print(a[0])
print(a[-1])

print(time.perf_counter())