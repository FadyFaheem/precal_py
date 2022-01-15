import math

def solve_squares():
    print("1. Solve")
    print("2. Show Example")
    print("0. Exit")
    ss_menu = input("Pick Mode: ")

    if ss_menu == '1':
        a = input("a: ")
        b = input("b: ")
        c = input("c: ")
        
        a = float(a)
        b = float(b)
        c = float(c)
        
        if b == 0:
            c = c * -1
            print("x = +-sqrt(" + str(c) + ")")
        if a != 1:
            e = a / a
            
            if b % a == 0:
                f = b / a
            else: 
                f = b
                
            h = math.pow((f * .5), 2)

            if c % a == 0:
                g = ((c / a) * -1) + h 
            else:
                g = (c * -1) + (h * a)
        
            i = math.sqrt(h)
            if f < 0:
                if c % a == 0:
                    print("x = " + str(i) + "+-sqrt(" + str(g) + ")")
                else:
                    print("x = " + str(i) + "+-sqrt(" + str(g) + "/" + str(a) + ")")
                    print("After simplifying")
                    g = g * a
                    print("x = " + str(i) + "+-sqrt(" + str(g) + ")/" + str(a))
            else:
                i = i * -1
                if c % a == 0:
                    print("x = " + str(i) + "+-sqrt(" + str(g) + ")")
                else:
                    print("x = " + str(i) + "+-sqrt(" + str(g) + "/" + str(a) + ")")
                    print("After simplifying")
                    g = g * a
                    print("x = " + str(i) + "+-sqrt(" + str(g) + ")/" + str(a))
        if a == 1:
            e = a
            f = b
            g = (c * -1) + (math.pow((f * .5), 2))
            h = math.sqrt(math.pow((f * .5), 2))
            if f > 0:
                h = h * -1
                print("x = " + str(h) + "+-sqrt(" + str(g) + ")")
            else:
                print("x = " + str(h) + "+-sqrt(" + str(g) + ")")
        solve_squares()
    elif ss_menu == '2':
        print("""ax^2 + bx + c = 0""")
        solve_squares()
    elif ss_menu == '0':
        main()
    else:
        solve_squares()

def circlerad_solve():
    print("1. Solve")
    print("2. Show Example")
    print("0. Exit")
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
        print("Radius without sqrt: sqrt(" + str(ans) + ")")
        ans = math.sqrt(ans)
        print("Radius with sqrt: " + str(ans))
        circlerad_solve()
    elif crs_menu == '2':
        print("""(x - h)^2 + (y - k)^2 = r^2""")
        circlerad_solve()
    elif crs_menu == '0':
        main()
    else:
        circlerad_solve()

def x_y_intercepts():
    print("1. Solve")
    print("2. Show Example")
    print("0. Exit")
    xyi_menu = input("Pick Mode: ")

    if xyi_menu == '1':
        a = input("h: ")
        b = input("k: ")
        c = input("r: ")
        a = float(a)
        b = float(b)
        c = float(c)
        #Solve X
        d = c + (math.pow((0 - b), 2) * -1)
        if d == 0:
            print("X = " + str(e))
        else:
            print("Don\'t forget to simplify radical!\nX = " + str(a) + "+-sqrt(" + str(d) + ")")
        #Solve y
        f = c + (math.pow((0 - a), 2) * -1)
        if f == 0:
            print("Y = " + str(b))
        else:
            print("Don\'t forget to simplify radical!\nY = " + str(b) + "+-sqrt(" + str(f) + ")")
        x_y_intercepts()
    elif xyi_menu == '2':
        print("""(x - h)^2 + (0 - k)^2 = r
(0 - h)^2 + (y - k)^2 = r""")
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

    print("0. Exit")

    mode = input("Pick Mode: ")

    if mode == '0':
        exit()
    elif mode == '1':
        solve_squares()
    elif mode == '2':
        circlerad_solve()
    elif mode == '3':
        x_y_intercepts()
    else:
        print("You didn\'t choose a program, Resetting...")
        main()

main()
