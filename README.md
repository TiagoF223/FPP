# FPP
Financial Python Project
1. Estrutura de Dados e Lógica Inicial
[ ] Leitura Robusta: Ler o data.csv usando o módulo csv e saltar o cabeçalho.

[ ] Conversão de Tipos: Converter a coluna "Valor" de String para float e a coluna "Dia" para int.

[ ] Dicionário de Categorias: Criar um dicionário que soma automaticamente os valores por categoria (se a categoria não existir, o código deve criá-la na hora).

[ ] Cálculo de Saldo: Criar uma variável que soma se o "Tipo" for + e subtrai se for -.

2. Funcionalidades de Filtragem (Manipulação de Strings)
[ ] Filtro por Mês: Pedir ao utilizador um mês (ex: "01") e mostrar apenas as transações desse período.

[ ] Detector de Maior Gasto: Percorrer os dados e imprimir qual foi a subcategoria onde gastaste mais dinheiro.

3. Interatividade (Menu do Utilizador)
[ ] Menu Principal: Criar um ciclo while que permite ao utilizador escolher entre:

Ver Saldo Atual.

Ver Gastos por Categoria.

Adicionar Nova Transação.

Sair.

[ ] Escrita de Dados: Ao escolher "Adicionar", o programa deve pedir os dados e usar o modo append ('a') para escrever uma nova linha real no teu data.csv.

4. Segurança e Profissionalismo (Bases Avançadas)
[ ] Tratamento de Erros: Usar try...except para evitar que o programa feche se o ficheiro data.csv estiver aberto no Excel ou se faltar alguma coluna.

[ ] Gerador de Relatório: Criar uma função que exporta um resumo final para um ficheiro resumo_anual.txt.