
# Basic for loop using interger
# for i in range(5):
#     print(i)

# Basic for loop Using String
# fruits = ["apple", "banana", "mango"]

# for fruit in fruits:
#     print(fruit)

n = int(input("Enter a number: "))

for num in range(2, n + 1):
    is_prime = True

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, "is a Prime Number")
    else:
        print(num, "is Not a Prime Number")