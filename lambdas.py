"""
Utilizando lambdas
Conhecidas por expressões lambdas ou simplesmente lambdas
funções anonimas

"""
nome_completo = lambda nome, sobrenome: nome.strip().title() + " " + sobrenome.strip().title()
print(nome_completo(" ANGELINA ", " JOLIE"))