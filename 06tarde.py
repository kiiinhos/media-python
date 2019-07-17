# salario = int(input('Digite seu salario'))
# emprestimo = int(input('Digite o valor desejado'))
# if((salario > 1000) and (emprestimo > 2000 and emprestimo < salario*15)):
#     print('Conseguiu')
# else: 
#     print('Sem chance meu parceiro')
def media(*valores):
    sum = 0
    for n in valores[0]:
        sum += float(n)
    return sum/len(valores[0])

valor = None
lista = []
while True:
    valor = input('quais valores para média? digite sair para parar :')
    if valor == 'sair':
        break
    lista.append(valor)
print('sua média é', media(lista))