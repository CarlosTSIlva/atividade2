

def calcule_area(a, b, c):
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** (1 / 2)

    return area

def verifica_triangulo(a, b, c):
    if a < b + c and b < a + c and c < a + b:
        return True
    else:
        return False


if __name__ == '__main__':
    ladoa = int(input("Digite o ladoA:"))
    ladob = int(input("Digite o ladoB:"))
    ladoc = int(input("Digite o ladoC:"))
    if verifica_triangulo(ladoa, ladob, ladoc):
        print(f"O triângulo de lados {ladoa}, {ladob} e {ladoc} existe e tem área {calcule_area(ladoa, ladob, ladoc)}")
    else:   
        print(f"O triângulo de lados {ladoa}, {ladob} e {ladoc} não existe.")

