from ler_dados import ler_dados

def calculate():
    dados = ler_dados()
    total_positivo = 0
    total_negativo = 0

    # Usamos .items() para "desembrulhar" os níveis
    for tipo, categorias in dados.items():
        for categoria, subcategorias in categorias.items():
            for subcategoria, lista_gastos in subcategorias.items():
                # lista_gastos é a lista de tuplas [(valor, data), ...]
                for valor, data in lista_gastos:
                    if tipo == '+':
                        total_positivo += valor
                    elif tipo == '-':
                        total_negativo += valor
    
    saldo_final = total_positivo - total_negativo
    return total_positivo, total_negativo, saldo_final

if __name__ == "__main__":
    positivo, negativo, saldo = calculate()
    print(f"Total Positivo: {positivo}")
    print(f"Total Negativo: {negativo}")
    print(f"Saldo Final: {saldo:.2f}")