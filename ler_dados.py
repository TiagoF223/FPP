import csv

def ler_dados():
    dct = {}
    with open('data.csv', 'r', encoding='utf-8') as ficheiro:
        leitor = csv.DictReader(ficheiro)
        
        for linha in leitor:
            # Extração limpa pelo nome da coluna
            t = linha['Tipo']
            c = linha['Categoria']
            s = linha['Subcategoria']
            v = float(linha['Valor'])
            d = linha['Data']
            
            # 1. Garantir o nível do TIPO (+ ou -)
            if t not in dct:
                dct[t] = {}
            
            # 2. Garantir o nível da CATEGORIA (Alimentação, etc)
            if c not in dct[t]:
                dct[t][c] = {}
                
            # 3. Garantir o nível da SUBCATEGORIA (Restaurante, etc)
            if s not in dct[t][c]:
                dct[t][c][s] = [] # Criamos uma lista para aceitar vários gastos
            
            # 4. Adicionar os dados finais (Valor e Data)
            dct[t][c][s].append((v, d))
            
    print(dct)

if __name__ == "__main__": 
    ler_dados()