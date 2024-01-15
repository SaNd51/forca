from utils import teste
txt = ['Escolha a opção','1 frutas','2 animais','3 objetos','4 profissões']
print('\n'.join(map(str, txt)))
x = int(input("opção: "))

teste(x)
