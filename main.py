def cubicFunction(a,b,c,d):
    u = ((-b**3)/(27*a**3))+((b*c)/(6*a**2))-((d)/(2*a))
    u2 = ((c)/(3*a))-((b**2)/(9*a**2))
    u3 = ((b)/(3*a))
    u4 = (((u)+((u)**2)+((u2)**3)**0.5)**(1/3))
    x = u4+u4-u3
    x = x.real
    return(x)



name = input("What is your name? ")
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
d = int(input("d: "))

l = "Hello"+name.title(), "I will solve", str(a)+"x^3"+str(b)+"x^2+"+str(c)+"x"+str(d)+"=0."
print(l)

print(cubicFunction(a,b,c,d))

quit()