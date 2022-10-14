def conv(n,radix):
    digits="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    r=""
    while(n>0):
        k=n%radix   
        r=digits[k]+r 
        n=n//radix
    return r 
while True:                                        #Проверка на дурака
    try:
        n=int(input("n="))
        d=int(input("d="))                              
        break
    except ValueError:
        print('Вы должны ввести число! Попробуйте снова!')
while True:                                        #Проверка на дурака
    try:
        d !=8 or d !=2                            
        break
    except ValueError:
        print('Вы должны ввести число! Попробуйте снова!')
if d==8:
   x8=conv(n,d)
   print(x8)
else:
     if d==2:
        x2=conv(n,d)
print(x2)