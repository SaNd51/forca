import random

def busca(n: str):
    arq = open(n, "r", encoding="utf-8")
    x = random.choice(list(arq))
    return x.rstrip('\n')

def escolhe(op):
    match op:
        case 1:
            return busca("frutas.txt")
        case 2:
            return busca("animais.txt")
        case 3:
            return busca("objetos.txt")
        case _:
            return busca("profissoes.txt")

def posicao(p, v):
    for i in p:
        if i in v:
            print(i, end="")
        elif not i in v:
            print("_", end="")
    print("")

def achou(p, v, a):
    x = []
    for i in p:
        if i in v:
            x.append(i)        
    x = ''.join(x)
    if x == p:
        a = True
        return a

def teste(x):
    palavra = escolhe(x).lower()
    v = []
    a = False
    n = len(palavra)
    while n > 0:
        print(f'Você tem {n} chances')
        t = input("digite uma letra ou a palavra: ")
        v.append(t)
        if t.lower() in set(palavra):
            posicao(palavra, v)
            if achou(palavra, v, a) == True:
                a = True
                print("You Win!")
                break
        elif t.lower() == palavra:
            print("You Win!")
            a = True
            break
        else:
            n -= 1
            print("X")
    if a == False:
        print(f"You Lose!\na palavra secreta era: {palavra}")