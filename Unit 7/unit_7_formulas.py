def circles():
    print("1. Classify\n2. Formula \n0.Exit")
    menu = input("Mode: ")

    if menu == '1':
        print("A & C are both +, A=C")
        circles()
    if menu == '2':
        print("(x-h)^2 + (y-k)^2 = r^2")
        circles()
    elif menu == '0':
        main()
    else:
        circles()
        

def elipses():
    print("1. Classify\n2. Vert Form\n3. Horz Form\n0.Exit")
    menu = input("Mode: ")
    
    if menu == '1':
        print("A & C are +, A /= C\nBigger number = A")
        elipses()
    if menu == '2':
        print("""(x-h)^2  (y-k)^2
------- + ------- = 1
  b^2       a^2""")
        elipses()
    if menu == '3':
        print("""(x-h)^2  (y-k)^2
------- + ------- = 1
  a^2       b^2""")
        elipses()
    elif menu == '0':
        main()
    else:
        elipses()


def hyperbolas():
    print("1. Classify\n2. Vert Form\n3. Horz Form\n0.Exit")
    menu = input("Mode: ")
    if menu == '1':
        print("A || C = 0, one sqr term")
        hyperbolas()
    if menu == '2':
        print("1. Formula\n2. Tran-Axis & Conj-Axis\n3. Vertices\n4. Co-Vertices")
        vert = input("Mode: ")

        if vert == '1':
            print("""(y-k)^2 (x-h)^2
------ - ------ = 1
   a        b""")
        elif vert == '2':
            print("Tran- y=k\nConj- x=h")
        elif vert == '3':
            print("(h+a,k) & (h-a,k)")
        elif vert == '4':
            print("(h,k+b) & (h,k-b)")
        hyperbolas()
    if menu == '3':
        print("""(x-h)^2 (y-k)^2
------ - ------ = 1
   a        b""")
        hyperbolas()
    elif menu == '0':
        main()
    else:
        hyperbolas()

def parabolas():
    print("1. Classify\n2. Vert Form\n3. Horz Form\n0.Exit")
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
