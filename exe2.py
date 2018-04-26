"""to reverse a string
#By Siddharth Rautaray  
#mail: siddharthrautaray@ymail.com
#educational purpose only
"""
def reverse_string(str):
    #convert string to a list
    str_list=list(str)
    #reverse the list
    str_list.reverse()
    #join the list with an empty string and return it
    return ("".join(str_list))

#Let's test it
reverse_string("hello")
reverse_string("siddharth")
#printing a value
print(reverse_string("student"))