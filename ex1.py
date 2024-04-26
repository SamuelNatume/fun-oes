def pegar_maior(ListaValores):
    maior = 0
    for num in ListaValores:
        if num > maior:
            maior = num 
    return maior 
lista = [7,10,5]
maior_valor = pegar_maior(lista)
print(f"O maior valor é: {maior_valor}")