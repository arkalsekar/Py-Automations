import math
print("What do you want to?? ")
print("1. nth Term of an AP ")
print("2. Sum of the nth term of the AP")

'''
Nth term of an AP = tn = a+(n-1)d
'''

def intput(Text):
    int(input(Text))
    return intput

z = int(input("What do You want to Do"))


while True:
    a = int(input("Enter your the First Term of an AP \n"))
    b = int(input("Enter your the Last Term of an AP \n"))
    c = int(input("Enter your the Nth Term of an AP \n"))

    if (z==1):
        print(a+(b-1)*c)

    a = intput("Enter your First Number")