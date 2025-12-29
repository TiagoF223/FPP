from Budget import Budget_module

print('='*50)
print("======= Welcome to Financial Python Program ======")
print('='*50)
print("Here is where you can manage your finances effectively.")
print('='*50)
while True:
    print('1.Budget')
    print('2.Investments')
    print('3.Casino')
    print('4.')
    print('5.EXIT')
    print('='*50)
    output=input('What operation would you like to perform? ')
    try:
        numero = int(output)
        if numero==1:
            Budget_module()
        elif numero==2:
            pass
        elif numero==3:
            pass
        elif numero==4:
            pass
        elif numero==5:
            print('='*50)
            print("======== CLOSING Financial Python Program ========")
            print('='*50)
            break
        else:
            print('='*50)
            print("Erro: Please insire a operation number(1-5).")
            print('='*50)
    except (ValueError, TypeError):
        print('='*50)
        print("Erro: Please insire a operation number(1-5).")
        print('='*50)
        


    
