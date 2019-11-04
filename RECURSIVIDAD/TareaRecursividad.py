def factorial_numero(numero):
    if numero == 1 or numero == 0:
        return 1
    else:
        numero *= factorial_numero(numero-1)
        return numero


def suma_lista(lista):
    if len(lista) == 0:
        return False
    else:
        return lista.pop() + suma_lista(lista)


def main():
    print(factorial_numero(5))
    print(suma_lista([1,2,3,4,5]))
main()