import random
import itertools

def pares(lista):
    # Gera todos os pares possíveis usando combinations
    todos_pares = list(itertools.combinations(lista, 2))
    
    # Embaralha os pares para garantir que a ordem seja aleatória
    random.shuffle(todos_pares)

    # Lista para armazenar os pares finais
    pares_final = []
    
    # Variável para armazenar o último par
    ultimo_par = None
    
    while todos_pares:
        # Tenta encontrar um par que não repita nenhum elemento do último par
        for i, par in enumerate(todos_pares):
            if not ultimo_par or (par[0] not in ultimo_par and par[1] not in ultimo_par):
                pares_final.append(par)
                ultimo_par = par
                todos_pares.pop(i)
                break
        else:
            # Se não encontrar, reseta o último par para permitir novos pares
            ultimo_par = None

    return pares_final

lista = []

print("Digite a quantidade de jogadores")

numjogador = int(input())
for x in range(numjogador):
    print("digite o nome do jogador")
    jogador = input()
    lista.append(jogador)

print(pares(lista))


# Pares antiga

def paresAntiga(lista) :
    if(len(lista)<=1) :
        return []

    novospares =[(lista[0], x) for x in lista[1:]]

    return novospares + pares(lista[1:])