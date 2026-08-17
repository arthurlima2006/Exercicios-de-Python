'''
Docstring para equacao03
Três amigos somaram suas idades. 
João tem o dobro da idade de Pedro. 
Carlos tem a mesma idade de Pedro. 
A soma das idades é 60 anos. Qual é a idade de cada um?
'''

# Definição do problema:
# Idade de Pedro = P
# Idade de João = 2 * P
# Idade de Carlos = P
# A soma das idades é 60: P + 2P + P = 60

# Resolvendo a equação:
# 4P = 60
# P = 60 / 4
# P = 15

# -------------------------------------------------------

# Definição das idades
idade_pedro = 15
idade_joao = 30
idade_carlos = 15

# Soma das idades
soma_idades = idade_pedro + idade_joao + idade_carlos

print(f"Se a idade de Pedro é {idade_pedro} e João tem o dobro da sua idade, logo João tem {idade_joao} anos. E se Carlos tem a mesma idade que Pedro, podemos ter certeza de que Carlos tem {idade_carlos} anos. Calculando tudo, temos o resultado da soma das idades já dita que é {soma_idades}. ")