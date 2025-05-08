import numpy as np

#define number of value

val = np.arange(1,101)

#create function to apply logic for prime number
def prime_num(n):
    if n < 2:
        return False
    for i in range(2, n):  
        if n % i == 0:
            return False
    return True

#create list for output values
prime_list = []

#iterate over valray to apply prime_num function
for x in val:
    prime_list.append(prime_num(x))

result = val.astype(object)

#Replace numbers divisible by both 3 and 5 with "FooBar"
rep_3and5 = (val % 15 == 0)
result[rep_3and5] = "FooBar"

#Replace numbers divisible by 3 with "Foo" and excluding value from past step that already handled
rep_3 = (val % 3 == 0) & ~rep_3and5
result[rep_3] = "Foo"

#Replace numbers divisible by 5 with "Bar" and excluding value from past step that already handled
rep_5 = (val % 5 == 0) & ~rep_3and5 
result[rep_5] = "Bar"

#filter values for prime numbers
result[prime_list] = ""

#Print output horizontally
print(" ".join(map(str, result)))