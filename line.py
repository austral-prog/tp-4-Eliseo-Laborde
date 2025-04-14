def line():
    A=float(input("Ingrese el coeficiente A: "))
    B=float(input("Ingrese el coeficiente B: "))
    X1=float(input("Ingrese el coeficiente X1: "))
    X2=float(input("Ingrese el coeficiente X2: "))
    P1=A*X1+B
    P2=A*X2+B
    dist=((X2-X1)**2 + (P2-P1)**2)**0.5
    print(f"El coeficiente A de su ecuación de la recta es: {A}\nEl coeficiente B de su ecuación de la recta es: {B}\nEl coeficiente X1 de su ecuación de la recta es: {X1}\nEl coeficiente X2 de su ecuación de la recta es: {X2}\n")
    print(f"Para la siguiente ecuación:\n\tY = {A}X + {B}\n")
    print(f"Dados los siguientes puntos:\n\tP1 ({X1}, {P1})\n\tP2 ({X2}, {P2})\n\nLa distancia entre ellos es: {dist}")
