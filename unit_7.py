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
                print("\nnon-Simplified Radical")
                print("X = " + str(i) + "+-sqrt(" + str(g) + "/" + str(a) + ")")
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

def circlerad_solve():
    print("\n1. Solve")
    print("2. Show Example")
    print("0. Exit\n")
    crs_menu = input("Pick Mode: ")

    if crs_menu == '1':
        print("Circle Side")
        a = input("x: ")
        b = input("y: ")
        print("Circle Center")
        c = input("h: ")
        d = input("k: ")

        a = float(a)
        b = float(b)
        c = float(c)
        d = float(d)

        ans = pow((a - c), 2) + pow((b - d), 2)
        print("\nRadius without sqrt: sqrt(" + str(ans) + ")")
        ans = math.sqrt(ans)
        print("Radius with sqrt: " + str(ans))
        
        
        circlerad_solve()
    elif crs_menu == '2':
        print("""
(x - h)^2 + (y - k)^2 = r^2""")
        circlerad_solve()
    elif crs_menu == '0':
        main()
    else:
        circlerad_solve()

def x_y_intercepts():
    print("\n1. Solve")
    print("2. Show Example")
    print("0. Exit\n")
    xyi_menu = input("Pick Mode: ")

    if xyi_menu == '1':
        print("hello")
        x_y_intercept()
    elif xyi_menu == '2':
        print("""
""")
        x_y_intercepts()
    elif xyi_menu == '0':
        main()
    else:
        x_y_intercepts()
    
def main():
    #  Modes
    print("Unit 7.1")
    print("1. Solving for squares")
    print("2. Solve for Circle radius")
    print("3. Solve for circle x,y intercepts")

    print("\n0. Exit")

    mode = input("\nPick Mode: ")

    if mode == '0':
        exit()
    elif mode == '1':
        solve_squares()
    elif mode == '2':
        circlerad_solve()
    elif mode == '3':
        x_y_intercepts()
    else:
        print("\nYou didn\'t choose a program, Resetting...\n")
        main()

main()
