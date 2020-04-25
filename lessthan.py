def main():
    less5 = []
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    for inspect in a:
        if inspect < 5:
            less5.append(inspect)
    print(less5)
