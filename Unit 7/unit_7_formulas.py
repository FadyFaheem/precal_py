def circles():
    print("1. Classify")
    menu = input("Mode: ")

    if menu == '1':
        print("A & C are both +, A=C")
        circles()
    elif menu == '0':
        main()
    else:
        circles()
        

def elipses():
    print("1. Classify")
    menu = input("Mode: ")
    
    if menu == '1':
        print("A & C are +, A /= C")
        elipses()
    elif menu == '0':
        main()
    else:
        elipses()


def hypebolas():
    print("1. Classify")
    menu = input("Mode: ")
    if menu == '1':
        print("either A || C is -")
        hypebolas()
    elif menu == '0':
        main()
    else:
        hypebolas()

def parabolas():
    print("1. Classify")
    menu = input("Mode: ")
    if menu == '1':
        print("A || C = 0, one sqr term")
        parabolas()
    elif menu == '0':
        main()
    else:
        parabolas()

def main():
    print("1. Circles\n2. Elipses\n3. Hyperbolas\n4. Parabolas\n0. Exit")

    menu = input("Mode: ")

    if menu == '1':
        circles()
    elif menu == '2':
        elipses()
    elif menu == '3':
        hyperbolas()
    elif menu == '4':
        parabolas()
    elif menu == '0':
        exit()
    else:
        main()


main()
