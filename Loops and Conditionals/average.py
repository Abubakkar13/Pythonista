'''
Write the code that reads 2 numbers from the keyboard, a and b. As an output, it shows the mean of all numbers that lie on the interval between a and b, and can be divided by 3.

What does it mean? In the example, you are to calculate the mean of the numbers in the range [-5; 12][−5;12]

The numbers divided by 3 without the remainder are: -3, 0, 3, 6, 9, 12−3,0,3,6,9,12. There are six of them, and the mean is 4.5.

The input interval always contains at least one dividend of 3. Remember to include the values of a and b in your calculations.

'''
a, b = int(input()), int(input())

c = []

for x in range(a, b + 1):
    if (x % 3) == 0:
        c.append(x)

print(sum(c) / len(c))

