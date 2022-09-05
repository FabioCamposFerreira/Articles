list=[]
for x in range(1,101):
    list.append(x)
for i in list:
    number = i
    if number==2 or number==3 or number==5 or number==7:
       print (number, 'é primo!')
    else:
        if number%2==0 or number%3==0 or number%5==0 or number%7==0:
           print (number, 'não é primo!')
        else:
            print (number, 'é primo!')
