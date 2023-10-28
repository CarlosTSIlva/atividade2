

def frase_invert(frase_escrita):
    frase = frase_escrita.split()    
    trocar_palavras = [palavra[::-1] for palavra in frase[::-1]]

    string_formatada = " ".join(trocar_palavras)

    print(string_formatada)



if __name__ == '__main__':
    frase = input("Digite a frase:")
    frase_invert(frase)

