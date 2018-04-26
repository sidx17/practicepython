''' TO create a program to get factorial of a number
by Siddharth Rautary
siddharthrautary@ymail.com
'''
def factorize(num):
    result=1
    for i in range(1,num+1):
        result=result*i
    return result

print(factorize(5))