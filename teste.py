"""
Teste amigo
"""
temp = float(input("Qual a temperatura? ")) #convertendo para float, a temp pode ser um número real

if temp  >= 10 and temp <= 20:
    print(f"Frio pois a temperatura é {temp}")
elif temp > 20:
    print(f"calor pois a temperatura é {temp}")
else:
    print(f"congelante pois a temperatura é {temp}")





