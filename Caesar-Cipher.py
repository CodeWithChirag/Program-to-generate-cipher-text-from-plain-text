a=[]
z=int(input('\nTo Encrypt Press:0 \nTo Decrypt Press:1 \n'))
x=input('Enter Text: ')
y=int(input('Enter Key: '))
while (y%26 is 0):
    y=int(input('Choose Different Key: '))
for i in x:
    n=ord(i)
    if(n==32):
        a.append(chr(n))
    elif(64<n<91):
        for j in range(y):
            if (z is 0):
                n=n+1
                if(n>90):
                    n=65
            elif(z is 1):
                n=n-1
                if(n<65):
                    n=90
        a.append(chr(n))
    elif(66<n<123):
        for k in range(y):
            if (z is 0):
                n=n+1
                if(n>122):
                    n=97
            elif(z is 1):
                n=n-1
                if(n<97):
                    n=122
        a.append(chr(n))
print('Your Cipher Text Is: ')
for k in range(len(x)):
    print(a[k],end='')
