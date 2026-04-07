from random import randint
numero_maquina= randint(0,2)
sua_escolha=int(input("Digite o numero 0 para pedra,1 para papel ou 2 para tesoura:"))
if numero_maquina==0:
    print("A escolha da maquinaa é Pedra")
elif numero_maquina==1:
    print("A escolha da maquina é papel")
elif numero_maquina==2:
    print("A escolha da maquina é tesoura")

if sua_escolha==0:
    print("A sua escolha é Pedra")
elif sua_escolha==1:
    print("A sua escolha é papel")
elif sua_escolha==2:
    print("A sua escolha é tesoura")
if sua_escolha==numero_maquina:
    print("empate")
elif sua_escolha==0 and numero_maquina==2 or sua_escolha==1 and numero_maquina==0 or sua_escolha==2 and numero_maquina==1:
    print("voce ganhou!!")
else:
    print("Voce perdeu")