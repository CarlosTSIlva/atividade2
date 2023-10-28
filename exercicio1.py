

def print_hi(dias):
    anos = dias // 365
    meses = (dias % 365) // 30
    dias = (dias % 365) % 30

    print(f"Você tem exatamente {anos} anos, {meses} meses e {dias} dias.")


if __name__ == '__main__':
    numeroDias = int(input("Digite o número de dias:"))
    print_hi(numeroDias)

