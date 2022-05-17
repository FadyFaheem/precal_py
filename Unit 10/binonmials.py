import math
import string

superscript_map = {
    "0": "⁰", "1": "¹", "2": "²", "3": "³", "4": "⁴", "5": "⁵", "6": "⁶",
    "7": "⁷", "8": "⁸", "9": "⁹"
    }

trans = str.maketrans(
    ''.join(superscript_map.keys()),
    ''.join(superscript_map.values()))

def main():
    a = input("A (leave empty if no number): ")
    b = input("B (leave empty if no number): ")
    c = int(input("Term: "))
    d = int(input("Exponent: "))
    e = (math.factorial(d)) / (math.factorial(c - 1)*math.factorial(d-(c-1)))

    if a == "" and b == "":
        f = (c - 1)
        g = d - f
        print(str(int(e)) + "a" + (str(g)).translate(trans) + "b" + (str(f)).translate(trans))
        main()
    else:
        f = (c - 1)
        g = d - f
    
        if a == "":
            a = 1
        else:
            a = math.pow(int(a), g)
        if b == "":
            b = 1
        else:
            b = math.pow(int(b), f)
    
        h = e * b * a
        print(str(int(h)) + "x" + (str(g)).translate(trans) + "y" + (str(f)).translate(trans))
        main()

main()
