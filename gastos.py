#ver cada gasto de acordo com as categorias
from ler_dados import ler_dados
from calculator import soma_mes

def categorias_anuais():
    dados = ler_dados()
    print('='*50)
    for tipo, categorias in dados.items():
        for categoria, subcategorias in categorias.items():
            print(f"Category: {categoria}")
            positivo_total = 0
            negativo_total = 0
            for subcategoria, lista_gastos in subcategorias.items():
                for valor, data in lista_gastos:
                    if tipo == '+':
                        positivo_total += valor
                    elif tipo == '-':
                        negativo_total += valor
            total=positivo_total - negativo_total
            GREEN = '\033[32m'  #atribui cor verde para positivo
            RED = '\033[31m'    #atribui cor vermelho para negativo
            RESET = '\033[0m'   #retorna a cor para o padrão
            if total >= 0:
                print(f"Total: {GREEN} {total:.2f}€{RESET}")
            else:
                print(f"Total: {RED} {total:.2f}€{RESET}")
            print('='*50)
#categorias_anuais()

def categorias_mensais(mes):
    print(f"Calculating every category for month: {mes}")
    dados = ler_dados()
    for tipo, categorias in dados.items():
        for categoria, subcategorias in categorias.items():
            print(f"Category: {categoria}")
            positivo_mes = 0
            negativo_mes = 0
            for subcategoria, lista_gastos in subcategorias.items():
                for valor, data in lista_gastos:
                    num_mes=data.split('/')
                    if tipo == '+' and mes==num_mes[1]:
                        positivo_mes += valor
                    elif tipo == '-' and mes==num_mes[1]:
                        negativo_mes += valor

            total=positivo_mes - negativo_mes
            GREEN = '\033[32m'  #atribui cor verde para positivo
            RED = '\033[31m'    #atribui cor vermelho para negativo
            RESET = '\033[0m'   #retorna a cor para o padrão
            if total >= 0:
                print(f"Total: {GREEN} {total:.2f}€{RESET}")
            else:
                print(f"Total: {RED} {total:.2f}€{RESET}")
            print('='*50)
categorias_mensais('02')

