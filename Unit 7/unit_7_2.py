import math

def st_eq_h():
    print("1.Solve\n2.Show Example\n0.Main Menu")
    steqh_menu = input("Pick Mode:")
    if steqh_menu == '1':
        print("cool")
        # TO-DO Solving
        st_eq_v()
    elif steqh_menu == '2':
        print("""""")
        st_eq_h()
    elif steqh_menu == '0':
        main()
    else:
        st_eq_h()

def st_eq_v():
    print("1.Solve\n2.Show Example\n0.Main Menu")
    steqv_menu = input("Pick Mode:")
    if steqv_menu == '1':
        print("cool")
        # TO-DO Solving
        st_eq_v()
    elif steqv_menu == '2':
        print("""""")
        st_eq_h()
    elif steqv_menu == '0':
        main()
    else:
        st_eq_v()

def main():
    print("Unit 7.2\n1.Standard Eq. Adv(Horizontal)\n2.Standard Eq. Adv(Vertical)\n0.Exit")
    menu = input("Pick Mode: ")
    if menu == '1':
        st_eq_h()
    elif menu == '2':
        st_eq_v()
    elif menu == '0':
        exit()
    else:
        main()
	
main()	