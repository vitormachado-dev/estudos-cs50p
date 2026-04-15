def main():
    x = int(input("O que é x?"))
    print("x ao quadrado é", quadrado(x))

def quadrado(n):
    return pow(n, 2)

main()