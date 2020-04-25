# String list challenge at https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html
def stringindex():
    x = str(input("Please enter a string: "))
    reverse = x[::-1]
    if x == reverse:
        print("This is a Palindrome")
    else:
        print("This is not a Palindrome")


stringindex()
