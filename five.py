# if else

a=int(input("enter ur age: "))
print("ur age is ", a)

if(a>=18):
    print("u are eligible to drive and vote")
else:
    print("u cannot drive and vote")



b = int(input("enter the number: "))
print(f'ur number is: {b}')

if (b<0):
    print('ur number is negative')
elif(b>0):
    if(b>0 and b<20):
        print('ur number is in range of 1-20.')
    elif(b>20):
        print('ur number is greater than 20')
else:
    print('not a valid number')