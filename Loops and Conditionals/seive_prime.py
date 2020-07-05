# Find all the prime numbers from 1 to 50



from math import sqrt
def seive_prime(num):
    prime_arr = [1]*(num+1) # from 0 to number  and defining 1 throught array
    prime_arr[0] =0
    prime_arr[1] = 0

    for i in range(2, int(sqrt(num))):
        if prime_arr[i] ==1: # if the array is 1 go for j ...
            j = 2
            while(i * j < num+1):
                prime_arr[j*i] = 0
                j = j + 1

            # After ....
            # for i in range(i*i,num+1,i):
            #     prime_arr[i] = 0
            #


    # returning number
    for i in range(0, len(prime_arr)):
        if prime_arr[i] == 1:
            print(i, end=" ")



num = int(input())
seive_prime(num)