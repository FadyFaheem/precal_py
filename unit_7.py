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

        e = float(a)
        f = float(b)
        g = float(c)
        if b == '0':
            c = float(c) * -1
            print("\nx = sqrt(" + str(c) + ")")
        elif a != '1':
            e = float(a) / float(a)
            f = float(b) / float(a)
            g = float(c) / float(a)

            print(str(e) + "\n" + str(f) + "\n" + str(g))

        
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
