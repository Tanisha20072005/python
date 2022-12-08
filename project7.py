num = int(input("Enter a number:"))
reverse = int(str(num)[::-1])
print("reversed string:",reverse)
if num>1:
    for i in range(2,num):
        if (num%i)==0:
            print(num,"is not prime number! but it is palidrome")
            break
    else:
        print(num,"is palidromic prime number")
else:
    if num>1:
        for i in range(2,num):
            if (num%i)==0:
                print(num,"is not prime number! as well asit is palidrome")
                break
        else:
            print(num,"is prime number but not palidrome!")
