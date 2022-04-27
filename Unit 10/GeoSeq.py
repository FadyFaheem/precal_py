import math

def main():
    a = float(input("First Term: "))
    b = float(input("r1: "))
    d = float(input("r2: "))
    c = float(input("nth Term: "))

    print(a * pow((b / d), (c - 1)))
    main()

main()
