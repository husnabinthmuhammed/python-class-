def is_prime(number):
    if number <= 1:

        return False

    for divisor in range (2,number):
        if number % divisor == 0:


            return False

        return True

num = int(input("enter the num:"))
if is_prime(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")