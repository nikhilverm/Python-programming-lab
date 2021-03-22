a = input('enter the number: ')
a = int(a)
i = 2

while i<a:

    if a%i==0:
       print('It is not prime')
       break
    i+=1

else:
     print('It is prime number')
