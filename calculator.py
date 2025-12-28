from ler_dados import ler_dados

def somatorio(): #somatorio do saldo total
    dados = ler_dados()
    total_positivo = 0
    total_negativo = 0

    for tipo, categorias in dados.items():
        for categoria, subcategorias in categorias.items():
            for subcategoria, lista_gastos in subcategorias.items():
                for valor, data in lista_gastos:
                    if tipo == '+':
                        total_positivo += valor
                    elif tipo == '-':
                        total_negativo += valor
    
    saldo_final = total_positivo - total_negativo
    return total_positivo, total_negativo, saldo_final

def soma_mes(mes): #somatorio do saldo mensal
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
                        negativo_mes += valor
    
    saldo_mes = positivo_mes - negativo_mes
    return positivo_mes, negativo_mes, saldo_mes






if __name__ == "__main__":
    positivo, negativo, saldo = soma_mes('11')
    print(f"Total Positivo: {positivo:.2f}")
    print(f"Total Negativo: {negativo:.2f}")
    print(f"Saldo Final: {saldo:.2f}")
    