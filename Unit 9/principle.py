import math
from decimal import Decimal


def main():
    a = float(input("P: "))
    b = float(input("R: "))
    c = float(input("N: "))
    d = float(input("T: "))
    
    return Decimal(((a * ( 1 + (b / c))) ** (c * d)))

main()
