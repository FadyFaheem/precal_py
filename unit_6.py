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
        c = input("Angle 3: ")

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
        print("Angle 1 is the side you\'re solving for")
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

        e = float(c) - float(a) # X
        f = float(d) - float(b) # Y
        
        g = math.sqrt(pow(e, 2) + pow(f, 2))
        h = pow(e, 2) + pow(f, 2)
        i = 0
        
        if e > 0 and f < 0:
            i = 360
        elif e < 0 and f > 0 or e < 0 and f < 0:
            i = 180
        
        l = round(i + math.degrees(math.atan(f/e)), 0)
        print("v1 = " + str(e) + "\nv2 = " + str(f) + "\n<" + str(e) + ", " + str(f) + ">")
        print("Only use magnituide if whole number!")
        print("Magnitude before sqrt: √" + str(h) + "\nMagnitude: " + str(g))
        print("Degrees: " + str(l) + "°")
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
        print("if a negative is present, don\'t forget it!")
        a = input("a: ")
        b = input("x1: ")
        c = input("y1: ")
        d = input("b: ")
        e = input("x2: ")
        f = input("y2: ")

        g = int(d) * int(e) + int(a) * int(b)
        h = int(d) * int(f) + int(a) * int(c)


        print("v1 = " + str(g) + "\nv2 = " + str(h) + "\n<" + str(g) + ", " + str(h) + ">")
        
        
        comp_form_multiple()
    elif compmulti_menu == '2':
        print("""
a(x1, y2) - b(x2, y2) = <v1, v2>""")
        comp_form_multiple()
    elif compmulti_menu == '0':
        main()
    else:
        comp_form_multiple()

def direc_mag():
    print("\n1. Solve")
    print("2. See possible equations")
    print("0. Go back to Main Menu\n")
    mag_menu = input("Pick mode: ")

    if mag_menu == '1':
        a = input("m1: ")
        b = input("X1: ")
        c = input("Y1: ")
        d = input("m2: ")
        e = input("X2: ")
        f = input("Y2: ")
        
        g = (float(a) *  math.cos(math.radians(float(b)))) + (float(d) * math.cos(math.radians(float(e)))) # X
        h = (float(a) * math.sin(math.radians(float(c)))) + (float(d) * math.sin(math.radians(float(f)))) # Y
        i = math.sqrt(pow(g, 2) + pow(h, 2)) 
        j = math.degrees(math.atan(h/g))
        k = 0 
        
        if h < 0 and g > 0:
            k = 360
        elif h < 0 and g < 0 or h < 0 and g > 0:
            k = 180
        
        l = round(k + j)
        
        print("\nx = " + str(g))
        print("y = " + str(h))
        print("Magnituide: " + str(i))
        print("Degree: " + str(l))
        print("Mag and Dir Form: " + str(round(i, 1)) + "<cos" + str(l) + "°, sin" + str(l) + "°>")
        
        direc_mag()
    elif mag_menu == '2':
        print("""
m * <cosV1, sinV2> = m1 * <cosX1, sinY1> + m2 * <cosX2, sinY1>""")
        direc_mag()
    elif mag_menu == '0':
        main()
    else:
        direc_mag()
    
def singlecomp_form():
    print("\n1. Solve")
    print("2. See example")
    print("0. Go back to Main Menu\n")
    singlecomp_menu = input("Pick mode: ")

    if singlecomp_menu == '1':
        a = input("\nm: ")
        b = input("x1: ")
        c = input("y1: ")
        
        f = float(a) * float(b) # X
        g = float(a) * float(c) # Y
        
        print("<" + str(f) +  ", " + str(g) + ">")
        singlecomp_form()
    elif singlecomp_menu == '2':
        print("""
<m * (x1 - y1)>""")
        singlecomp_form()
    elif singlecomp_menu == '0':
        main()
    else: 
        singlecomp_form()
   
def solve_vec():
    print("\n1. Solve")
    print("2. See example")
    print("0. Go back to Main Menu\n")
    vec_menu = input("Pick mode: ")

    if vec_menu == '1':
        a = input("\nx1: ")
        b = input("y1: ")
        c = input("x2: ")
        d = input("y2: ")

        e = float(c) + float(a) # X
        f = float(d) + float(b) # Y
        
        print("\nX = " + str(e))
        print("Y = " + str(f))
        solve_vec()
    if vec_menu == '2':
        print("""
(X2 - X1,  Y2 - Y1)""")
        solve_vec()
    elif vec_menu == '0':
        main()
    else: 
        solve_vec()
    
    
def main():
    print("\nLaw of Cosines")
    print("1. Side to Degrees (SSS)")
    print("2. Angle Solve (SAS)")
    print("\nLaw of Sines")
    print("3. Area of a Triangle")
    print("4. Minutes, Decimals")
    print("5. Solve for missing side")
    print("\nVectors")
    print("6. Solve for Component Form w/ Mag and Dire")
    print("7. Solve for Scalar Multiples Comp Form")
    print("8. Single Multiple Comp Form")
    print("9. Direction and Magnituide")
    print("10. Solve for Vector")
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
    elif program == '8':
        singlecomp_form()
    elif program == '9':
        direc_mag()
    elif program == '10':
        solve_vec()
    else:
        print("\nYou did not choose a program. Resetting.")
        main()

main()
