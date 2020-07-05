# To check whether a number is prime or not

def prime_num(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
is_prime = prime_num(23)
if is_prime:
    print("Number is a prime Number")
else:
    print("Number is not a prime number")

# Here the time complexity is 0(n), which can be reduced using
# taking int(num/2) which will give O(n/2)


# from math import sqrt
# for i in range(2, int(sqrt(num))+1:
# the time complexity is root(n) i.e 