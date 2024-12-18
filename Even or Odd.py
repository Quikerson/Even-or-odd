num = int(input("Type an int number between 1 and 1000: "))

print("---------")
if num < 1:
    print("Please type a number higher than 1")
elif num > 1000:
    print("Please type a number lower than 1000")
else:
    if (num%2) == 0:
        print("Your number is even")
    else:
        print("Your number is odd")
print("---------")