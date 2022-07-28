def Hanoi(n,A,B,C):
    if n == 1:
        """
        Nuestro estado base está pensando que en algún
        momento tendremos todo ordenado en B, y que 
        el disco más pequeño para dicho instante se
        encontrará en A
        """
        print(f"move from {A} to {B}")
    else:
        """
        En esta primera parte de recursión. Lo que hace es cambiar
        el orden de las letras y restar 1 cada vez hasta llega a n=1. 
        Cuando el número n inició como par, resultará que el primer 
        movimiento será de A a C. Cuando n es impar será de A a B. 
        """
        Hanoi(n-1, A,C,B)
        """
        Después de hacer un primer grupo de recursión hasta llegar 
        al caso base n=1 y hacer el primer movimiento. Recién podrá 
        entrar a Hanoi(1,A,B,C). Como estuvo cambiando el orden de 
        B y C. Obviamente si el primero movimiento fue de A a B.
        En este segundo paso será de A a C (o viceversa).
        En estos dos movimientos ya nos habremos quitado los discos
        mas pequeños. En el primer movimiento nos quitamos el disco 
        más pequeño y luego el segundo más pequeño.
        """
        Hanoi(1,A,B,C)
        """
        En la primera función del ELSE, la cual es Hanoi(n-1, A,C,B).
        El n era 2 (n=2), ya que cuando entró a la función, justo
        se hizo 1 y pudo resolver el caso base.
        Entonces ahora que entraremos a Hanoi(n-1,C,B,A) el n es 2.
        Al restarle 1, entraremos al caso base, y dependiendo de si
        n es par o impar, moveremos de B a C o viseversa. 
        Lo importante es que en el tercer movimiento ponemos al
        disco más pequeño sobre el segundo más pequeño.
        """
        Hanoi(n-1,C,B,A)
        """
        Lo siguiente que viene es la recursividad de los n que
        se estuvieron aguantando debido a que en las primeras 
        veces no se llegó a terminar el ELSE por completo. 
        Lo cual empesaría a retroceder ahora desde n=3. Como 
        no cumpliría para el caso base, entraría nuevamente
        a la primera función del ELSE que es Hanoi(n-1, A,C,B),
        obviamente respetando el orden en que hayan quedado 
        las letras en ese momento. 
        La recursividad continua hasta que se resuelve el problema.
        """

Hanoi(4, 'A', 'B', 'C')