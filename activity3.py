
num = int(input("Enter number to be checked: "))

if num > 50:
    print("Number is greater than 50.")
    if num % 2 == 0:
        print("And its even too.")
    else:
        print("And its odd.") 
else:
    print("The number is less than 50.")        
