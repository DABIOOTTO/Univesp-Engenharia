"""
Programa de calculo de média aritmética digitada pelo usuário
Autor: Dábio Otto da Silva - Idealizador Gabriel M. Silone
Data: 08/01/2021 19:18
"""
notas = [0,0,0,0,0] # lista de 5 elementos todos em zero
soma = 0
x = 0
while x < 5:
    notas[x] = float(input(f"Nota {x} : ")) # estrutura de repetição para ler as notas e guarda-las
    soma += notas [x]
    x += 1
x = 0 # reiniciamos o valor da variavel para 0
while x < 5: # criada outra estrutura de repetição
    print(f" Nota {x}: {notas[x]:6.2f}")
    x += 1
print(f"Media: {soma / x:5.2f}")
