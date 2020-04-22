# Divisors challenge at https://www.practicepython.org/exercise/2014/02/26/04-divisors.html
def divisors():
    num = int(input("Please enter your number: "))
    list1 = []
    for x in range(1, num):
        result = num % x
        if result == 0:
            list1.append(x)
    print(num, "Divisors are: ", list1)


divisors()
