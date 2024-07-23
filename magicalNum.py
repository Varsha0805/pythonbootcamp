num=1729
temp = num
sum=0
while(num>0):
    rem=num%10 
    sum=sum+rem
    num=num//10#int numbers
print(f"The sum is {sum}")
#sum=str(sum)
#rev=sum[::-1]
#print(f"The reverse is {rev}")
sum = str(sum)
reversed_digits = sum[::-1]
reversed_digits = int(reversed_digits)
sum = int(sum)
mul= sum*reversed_digits
print(mul)
if(temp == mul):
    print("It is a magical number")
else:
    print("Not a magical number")
