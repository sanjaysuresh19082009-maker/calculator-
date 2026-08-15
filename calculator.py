from sympy import *
init_printing(use_unicode=True)

while True:
    intro = print("select your mode")
    options = input("calculate, simultaneous ,interest : ")

    if "calculate" in options:
        equation = input("what is the equation?").split()

        def calculator(x,y,z):
            if y =="-":
                return print(x-z)
            elif y=="+":
                return print(x+z)
            elif y=="/":
                return print(x/z)
            elif y == "x" or "*":
                return print(x*z)


        calculator(int(equation[0]),(equation[1]),int(equation[2]))

    elif "simultaneous" in options:
        unknowns = int(input("how many unknowns?: "))
        if unknowns == 2:
            equ_1 = input("equation 1 --> ").split()
            equ_2 = input("equation 2 --> ").split()
            a,b,e = int(equ_1[0]),int(equ_1[3]),int(equ_1[6])
            c,d,f = int(equ_2[0]),int(equ_2[3]),int(equ_2[6])
            #AX = B
            A = Matrix([[a,b],[c,d]])
            B = Matrix([[e],[f]])
            #X=inverse of A times B
            X=A**-1*B
            x,y=X
            print(f"x is {x}")
            print(f"y is {y}")
        elif unknowns == 3:
            equ_1 = input("equation 1 --> ").split()
            equ_2 = input("equation 2 --> ").split()
            equ_3 = input("equation 3 --> ").split()
            a,b,c,k = int(equ_1[0]),int(equ_1[3]),int(equ_1[6]),int(equ_1[9])
            d,e,f,m = int(equ_2[0]),int(equ_2[3]),int(equ_2[6]),int(equ_2[9])
            g,h,i,n = int(equ_3[0]),int(equ_3[3]),int(equ_3[6]),int(equ_3[9])
            A = Matrix([[a,b,c],[d,e,f],[g,h,i]])
            B = Matrix([[k],[m],[n]])
            X = A**-1*B
            x,y,z = X 
            print(f"x is {x}")
            print(f"y is {y}")
            print(f"z is {z}")

    elif "interest" in options:
        t = float(input("what is the period?(years) "))
        p = float(input("what is the principal sum? "))
        r = float(input("what is the rate per annuam "))
        type_interest = input("compound or simple: ")
        if "compound" in type_interest:
            end_val=p*(1+r/100)**t
        elif "simple" in type_interest:
            end_val=((p*r*t)/100)+p
        print(f"ans is :${end_val:.2f} after {t} years")
