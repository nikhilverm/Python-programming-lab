a = int(input('Enter the value of number '))

Reverse=0
while(a>0):
    Remainder = a%10
    Reverse = (Reverse *10)+ Remainder
    a = a//10
print("\n reverse of entered number",Reverse)    
        
