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


calculator(int(equation[0]),int(equation[1]),int(equation[2]))