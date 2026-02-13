
# Basic while loop using integer
# i = 1

# while i <= 5:
#     print(i)
#     i += 1

n = int(input("Enter a number: "))

num = 2
while num <= n:
    i = 2
    is_prime = True

    while i <= int(num ** 0.5):
        if num % i == 0:
            is_prime = False
            break
        i += 1

    if is_prime:
        print(num, "is a Prime Number")
    else:
        print(num, "is Not a Prime Number")

    num += 1
