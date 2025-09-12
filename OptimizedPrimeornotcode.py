num = int(input("Enter a number: "))

if num < 2:
    print(f"{num} is not a prime number")
else:
    i = 2
    while i * i <= num:
        if num % i == 0:
            print(f"{num} is not a prime number")
            break
        if i == 2:
            i += 1
        else:
            i += 2 
    else:
        print(f"{num} is a prime number")
