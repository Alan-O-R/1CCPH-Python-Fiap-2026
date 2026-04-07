def boas_vindas(nome):
    print(f"Ola,{nome}! seja bem-vindo!!")
nome_digitado=input("Digite o seu nome:")
boas_vindas(nome_digitado)

#função com param. com retorno
def soma(numb_a,numb_b):
    soma=numb_a+numb_b
    return soma
resulta_soma= soma(numb_a=5, numb_b=9)
print(resulta_soma)
print(type(nome_digitado))