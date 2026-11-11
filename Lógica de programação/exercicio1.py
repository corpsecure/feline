#atividade 1

frutas=[]

for i in range (1,6):
    i=input("Que fruta deseja adicionar?")
    frutas.append(i)

print(frutas)

#atividade 2

numeros=[10, 20, 30, 40, 50]
print(numeros)
numeros.sort(reverse=True)
print(numeros)

#atividade 3

alunos=["felipe", "vinicius", "joao"]
print(alunos)
for i in range (1, 3):
    i=input("Que alunos deseja adicionar?")
    alunos.append(i)
    
print(alunos)

#atividade 4

linguagens=["Python", "Java", "C++", "PHP"]
linguagens.insert(1, "Javascript")
print(linguagens)

#atividade 5

lista=[1, 2, 3, 4, 5, 6]
print(lista)
lista.pop(5)
print(lista)

#atividade 6

cores=["azul", "verde", "vermelho", "verde", "amarelo"]
cores.remove("verde")
print(cores)

#atividade 7

animais=[]
for i in range (1, 6):
    i=input("Insira os animais que deseja colocar na lista")
    animais.append(i)

del animais [2]
print(animais)

sorteio=[]

while True:
    pergunta=input("Deseja inserir um nome para o sorteio?\n"
    "S para Sim e N para Não")

    if pergunta=="S":
        nome=input("Insira o nome para o sorteio:\n")
        sorteio.append(nome)

    else:
        break

print(sorteio)

import random
sorteado=random.choice(sorteio)
print("O sorteado é:", sorteado)