import math

def side_to_angle():

    print("\n1. Solve")
    print ("2. See possible equations")
    print ("0. Go back to Main Menu\n")
    menu = input("Pick mode:")

    if menu == '1':
        a = input("\nSide 1: ")
        b = input("Side 2: ")
        c = input("Side 3: ")

        top = pow(float(a),2) + pow(float(b),2) - pow(float(c),2)
        bottom = 2 * float(a) * float(b)
        answer = math.degrees(math.acos(float(top) / float(bottom)))
        print("Degrees of Angle 3: " + str(answer))
        side_to_angle()
    elif menu == '2':
        print("""
b^2 + c^2 - a^2
---------------  = cosA
      2bc

a^2 + c^2 - b^2
---------------- = cosB
      2ac

a^2 + b^2 - c^2
---------------- = cosC
      2ab""")
        side_to_angle()
    elif menu == '0':
        main()
    else:
        side_to_angle()

def side_solve():
    print("\n1. Solve")
    print("2. See possible equations")
    print("0. Go back to Main Menu\n")
    side_menu = input("Pick mode: ")

    if side_menu == '1':
        a = input("\nSide 1: ")
        b = input("Side 2: ")
        c = input("Angle 3:")

        answer = math.sqrt(pow(float(a),2) + pow(float(b),2) - 2 * (float(a) * float(b)) * math.cos(math.radians(float(c))))
        print("Angle Length: " + str(answer))

        side_solve()
    elif side_menu == '2':
        print("""
You must input the angle of the side you\'re trying to solve!

a^2 = b^2 + c^2 - 2bc * cosA

b^2 = a^2 + c^2 - 2ac * cosB

c^2 = a^2 + b^2 - 2ab * cosC""")
        side_solve()
    elif side_menu == '0':
        main()
    else:
        side_solve()

def area_triangle():
    print("\n1. Solve")
    print("2. See possible equations")
    print("0. Go back to Main Menu\n")
    area_menu = input("Pick mode: ")

    if area_menu == '1':
        a = input("\nSide 1:")
        b = input("Side 2:")
        c = input("Angle 3:")

        answer = (1 / 2) * float(a) * float(b) * math.sin(math.radians(float(c)))
        print("Area: " + str(answer) + "m^2")
        area_triangle()
    elif area_menu == '2':
        print("""
       1            
area = - * bc * SinA
       2            

       1
area = - * ab * SinC
       2

       1
area = - * ac * SinB
       2""")
        area_triangle()
    elif area_menu == '0':
        main()
    else:
        area_triangle()
        
def minutes_decimals():
    print("\n1. Solve")
    print("2. See example")
    print("0. Go back to Main Menu\n")
    minutes_menu = input("Pick mode: ")

    if minutes_menu == '1':
        a = input("\nDegrees°: ")
        b = input("Minutes\': ")

        c = float(a) + (float(b) / 60)
        d = (float(a) * 60) + float(b)

        print("\nTotal Degrees: " + str(c) + "°")
        print("Total Minutes: " + str(d) + "\'")
        print("Total Seconds: " + str(d * 60) + "sec")
        minutes_decimals()
    elif minutes_menu == '2':
        print("\na°*b\'")
        minutes_decimals()
    elif minutes_menu == '0':
        main()
    else:
        minutes_decimals()

def sin_side():
    print("\n1. Solve")
    print("2. See possible equations")
    print("0. Go back to Main Menu\n")
    sin_menu = input("Pick mode: ")

    if sin_menu == '1':
        a = input("Angle 1: ")
        b = input("Side 2: ")
        c = input("Angle 2: ")

        answer = float(b) * math.sin(math.radians(float(a))) / math.sin(math.radians(float(c)))
        print("Side 1: " + str(answer))
        sin_side()
    elif sin_menu == '2':
        print("""
 a      b
---- = ----
sinA   sinB

 b      c
---- = ----
sinB   sinC

 a      c
---- = ----
sinA   sinC""")
        sin_side()
    elif sin_menu == '0':
        main()
    else:
        sin_side()

def comp_form():
    print("\n1. Solve")
    print("2. See example")
    print("0. Go back to Main Menu\n")
    comp_menu = input("Pick mode: ")

    if comp_menu == '1':
        a = input("\nx1: ")
        b = input("y1: ")
        c = input("x2: ")
        d = input("y2: ")

        e = float(c) - float(a) 
        f = float(d) - float(b)

        print("v1 = " + str(e) + "\nv2 = " + str(f) + "\n<" + str(e) + ", " + str(f) + ">")
        comp_form()
    elif comp_menu == '2':
        print("""
(x1 - x2, y1 - y2) = <v1 , v2>""")
        comp_form()
    elif comp_menu == '0':
        main()
    else:
        comp_form()

def comp_form_multiple():
    print("\n1. Solve")
    print("2. See possible equations")
    print("0. Go back to Main Menu\n")
    compmulti_menu = input("Pick mode: ")

    if compmulti_menu == '1':
        a = input("a: ")
        b = input("x1: ")
        c = input("y1: ")
        d = input("x2: ")
        e = input("b: ")
        f = input("x2: ")
        g = input("y2: ")
        comp_form_multiple()
    elif compmulti_menu == '2':
        print("""
a(x1, y2) - b(x2, y2) = <v1, v2>""")
    elif compmulti_menu == '0':
        main()
    else:
        comp_form_multiple()

    
def main():
    print("\nLaw of Cosines")
    print("1. Side to Degrees (SSS)")
    print("2. Angle Solve (SAS)")
    print("\nLaw of Sines")
    print("3. Area of a Triangle")
    print("4. Minutes, Decimals")
    print("5. Solve for missing side")
    print("\nVectors")
    print("6. Solve for Component Form")
    print("7. Solve for Scalar Multiples Comp Form")
    print("\n0. Exit\n")
    program = input("(Int) Pick mode: ")
    if program == '0':
        exit()
    elif program == '1':
        side_to_angle()
    elif program == '2':
        side_solve()
    elif program == '3':
        area_triangle()
    elif program == '4':
        minutes_decimals()
    elif program == '5':
        sin_side()
    elif program == '6':
        comp_form()
    elif program == '7':
        comp_form_multiple()
    else:
        print("\nYou did not choose a program. Resetting.")
        main()

main()
