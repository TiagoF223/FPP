#ver cada gasto de acordo com as categorias
from ler_dados import ler_dados
from calculator import soma_mes

dados = ler_dados()
    positivo_mes = 0
    negativo_mes = 0
    
    for tipo, categorias in dados.items():
        for categoria, subcategorias in categorias.items():
            for subcategoria, lista_gastos in subcategorias.items():
                for valor, data in lista_gastos:
                    num_mes=data.split('/')
                    if tipo == '+' and mes==num_mes[1]:
                        positivo_mes += valor
                    elif tipo == '-' and mes==num_mes[1]:
                        negativo_mes += valor-