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
    print("2. Example")
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

def main():
    print("\nLaw of Cosines")
    print("1. Side to Degrees")
    print("2. Angle Solve")
    print("\nLaw of Sines")
    print("3. Area of a Triangle")
    print("4. Minutes, Decimals")
    print("5. Solve for missing side")
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
    else:
        print("\nYou did not choose a program. Resetting.")
        main()

main()
