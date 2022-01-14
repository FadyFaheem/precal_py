import math

def solve_squares():
    print("\n1. Solve")
    print("2. Show Example")
    print("0. Exit\n")
    ss_menu = input("Pick Mode: ")

    if ss_menu == '1':
        a = input("\na: ")
        b = input("b: ")
        c = input("c: ")

        a = float(a)
        b = float(b)
        c = float(c)

        if b == '0':
            c = float(c) * -1
            print("\nx = sqrt(" + str(c) + ")")
        elif a == 1 or a == -1:
            e = a
            f = b
            g = c * -1
            
            h = pow((f * 0.5), 2)
            j = math.sqrt(h)
            
            i = g + h
            
            print("\naDon\'t forget to simplify the radical!")
            print("X = " + str(j) + "+-sqrt(" + str(i) + ")")
        elif a != '1':
            e = a / a

            if b % a == 0:
                f = b / a
            else:
                f = float(b)

            h = pow(f * 0.5, 2)
            
            if c % a == 0:
                g = ((c * -1) / a)  + h 
            else:
                g = (float(c) * -1) + (h * a)

            i = math.sqrt(h) * -1

            if c % a != 0:
                i = i * -1
                g = g * a
                print("\nbaDon\'t forget to simplify the radical!")
                print("X = " + str(i) + "+-sqrt(" + str(g) + ")/" + str(a) + "")
            else:
                print("\ncDon\'t forget to simplify the radical!")
                print("X = " + str(i) + "+-sqrt(" + str(g) + ")")

        
        solve_squares()
    elif ss_menu == '2':
        print("""
ax^2 + bx + c = 0""")
        solve_squares()
    elif ss_menu == '0':
        main()
    else:
        solve_squares()
    

def main():
    #  Modes
    print("1. Solving for squares")

    print("\n0. Exit")

    mode = input("\nPick Mode: ")

    if mode == '0':
        exit()
    elif mode == '1':
        solve_squares()
    else:
        print("\nYou didn\'t choose a program, Resetting...\n")
        main()

main()
