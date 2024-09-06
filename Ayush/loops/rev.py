num = int(input(" enter the number: "))
sum1 = 0
while num!=0:
    rem = num%10
    sum1 = sum1*10+rem
    num//=10
print("Your ans is " , sum1)