import csv

def ler_dados():
    dct={}
    linha=1
    with open('data.csv', 'r') as ficheiro: #cria a ligaçao dos documentos
        leitor= csv.reader(ficheiro) #permite a leitura do documento
        cabecalho=next(leitor).strip().split(',') #lê a primeira linha do documento
        for linha in leitor: #percorre todas as linhas do documento
            linha_lista=linha
            Tipo=linha_lista[0]
            Categoria=linha_lista[1]
            Subcategoria=linha_lista[2]
            Valor=linha_lista[3]
            Data=linha_lista[4]
            if Tipo not in dct:
                dct[Tipo]={}
            if Categoria not in dct[Tipo]:
                dct[Tipo][Categoria]={}
            if Subcategoria not in dct[Tipo][Categoria]:
                dct[Tipo][Categoria][Subcategoria]=[]
            dct[Tipo][Categoria][Subcategoria].append((Valor, Data))
    return dct
if __name__ == "__main__": 
    ler_dados()