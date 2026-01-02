#saldo geral e mensal
#distribuição por categoria
#maximo por categoria
#comparação mensal
#exportação de relatórios de orçamento

import gastos  #categorias_anuais() e categorias_mensais(mes)
import calculator  #somatorio() e soma_mes(mes)
GREEN = '\033[32m'  #atribui cor verde para positivo
RED = '\033[31m'    #atribui cor vermelho para negativo
RESET = '\033[0m'   #retorna a cor para o padrão

def Budget_module():
    print('='*50)
    print("============ Welcome to Budget Program ===========")
    print('='*50)

    while True:
        print('1.Annual Expenses')
        print('2.Mounthly Expenses')
        print('3.Category Distribution')
        print('4.')
        print('5.EXIT')
        print('='*50)
        output=input('What operation would you like to perform? ')
        try:
            numero = int(output)

            if numero==1:
                total_pos, total_neg, saldo = calculator.somatorio()

                GREEN = '\033[32m'  #atribui cor verde para positivo
                RED = '\033[31m'    #atribui cor vermelho para negativo
                RESET = '\033[0m'   #retorna a cor para o padrão
                print('='*50)
                print(f"Total Positive: {GREEN} {total_pos:.2f}€{RESET}")
                print(f"Total Negative: {RED} {total_neg:.2f}€{RESET}")
                if saldo >= 0:
                    print(f"Your Annual Balance: {GREEN} {saldo:.2f}€{RESET}")
                else:
                    print(f"Your Annual Balance: {RED} {saldo:.2f}€{RESET}")
                print('='*50)
                print(" Here is your annual financial summary.\n Whould you like to perform another operation?\n If so, please select an option from the menu below.")
                print('='*50)
            elif numero==2:
                while True:
                    mes=input("Enter the month number (e.g., '01' for January, '02' for February): ")
                    if mes in ['01','02','03','04','05','06','07','08','09','10','11','12']:
                        
                        print("Invalid month. Please enter a valid month number (01-12).")
                        total_pos, total_neg, saldo = calculator.soma_mes(mes)
                        GREEN = '\033[32m'  #atribui cor verde para positivo
                        RED = '\033[31m'    #atribui cor vermelho para negativo
                        RESET = '\033[0m'   #retorna a cor para o padrão
                        print('='*50)
                        print(f"Total Positive: {GREEN} {total_pos:.2f}€{RESET}")
                        print(f"Total Negative: {RED} {total_neg:.2f}€{RESET}")
                        if saldo >= 0:
                            print(f"Your Monthly Balance: {GREEN} {saldo:.2f}€{RESET}")
                        else:
                            print(f"Your Monthly Balance: {RED} {saldo:.2f}€{RESET}")
                        print('='*50)
                        print(" Here is your monthly financial summary.\n Whould you like to perform another operation?\n If so, please select an option from the menu below.")
                        print('='*50)
                        break
                    else:
                        print("Invalid month. Please enter a valid month number (01-12).")
            elif numero==3:
                gastos.categorias_anuais()
                print('='*50)
                print(" Here is your monthly financial summary.\n Whould you like to perform another operation?\n If so, please select an option from the menu below.")
                print('='*50)
            elif numero==4:
                while True:
                    mes=input("Enter the month number (e.g., '01' for January, '02' for February): ")
                    if mes in ['01','02','03','04','05','06','07','08','09','10','11','12']:
                        gastos.categorias_mensais(mes)
                        print('='*50)
                        print(" Here is your monthly financial summary.\n Whould you like to perform another operation?\n If so, please select an option from the menu below.")
                        print('='*50)
                        break
                    else:
                        print("Invalid month. Please enter a valid month number (01-12).")
                pass
            elif numero==5:
                print('='*50)
                print("======== CLOSING Budget Program ========")
                print('='*50)
                break
            else:
                print('='*50)
                print("Erro: Please insire a operation number(1-5).")
                print('='*50)
        except (ValueError, TypeError):
            print('='*50)
            print("Erro: Please insire a operation number(1-5)!")
            print('='*50)

if __name__ == "__main__":
    Budget_module()
    