from sympy import *
init_printing(use_unicode=True)

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
    equ_1 = input("equation 1 -->").split()
    equ_2 = input("equation 2 -->").split()
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

elif "interest" in options:
    t = float(input("what is the period? "))
    p = float(input("what is the principal sum? "))
    r = float(input("what is the rate per annuam "))
    type_interest = input("compound or simple: ")
    if "compound" in type_interest:
        end_val=p*(1+r/100)**t
    elif "simple" in type_interest:
        end_val=((p*r*t)/100)+p
    print(f"ans is :${end_val:.2f}")
