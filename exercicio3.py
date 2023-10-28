

def ordenar_numeros(a, b, c):
    list_ordenada = [a, b, c]
    list_ordenada.sort()
    return list_ordenada

if __name__ == '__main__':
    numero1 = int(input("Digite o numero1:"))
    numero2 = int(input("Digite o numero2:"))
    numero3 = int(input("Digite o numero3:"))
    ordenacao = ordenar_numeros(numero1, numero2, numero3)

    print(f"O menor numero é {ordenacao[0]}")