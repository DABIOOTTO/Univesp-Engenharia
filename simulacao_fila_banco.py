"""
Programa 6.7
Livro N.N.C Menezes
Pag. 107
Autor Dábio Otto da Silca
data: 07/01/2021 18:49
"""

ultimo = 10
fila = list(range(1,ultimo+1)) # nesse caso é 11 posições pois é 10+1 = 11 posições
while True:
    print(f"\n Existem {len(fila)} clientes na fila")
    print(f" Fila atual: {fila}")
    print(f" Digite F para dicionar um cliente ao fim da fila")
    print(f" Digite A para realizar o atendimento ou S para sair.")
    operacao = input ("Operação (F , A ou S):")
    if operacao == "A":
        if len (fila) >0:
            atendido = fila.pop(0)
            print(f"Cliente {atendido} atendido")
        else:
            print(f" Fila vazia! Ninguem para atender")
    elif operacao == "F":
        ultimo+=1 #incrementa um novo cliente
        fila.append(ultimo)
    elif operacao == "s":
        break
    else:
        print(f"Operacao invalida! digite apenas F, A ou S")
