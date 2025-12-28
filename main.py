from calculator import soma_mes


print('='*50)
print("======= Welcome to Financial Python Program ======")
print('='*50)
print("Here is where you can manage your finances effectively.")
print('='*50)
while True:
    output=input('What operation would you like to perform? ')
    print('1.Budget')
    print('2.Investments')
    print('3.Casino')
    print('4.')
    print('5.EXIT')
    try:
        numero = int(output)
        if numero==1:
            pass
        if numero==2:
            pass
        if numero==3:
            pass
        if numero==4:
            pass
        if numero==5:
            print('='*50)
            print("======== CLOSING Financial Python Program ========")
            print('='*50)
            break
    except (ValueError, TypeError):
        print('='*50)
        print("Erro: Please insire a operation number(1-5).")
        print('='*50)
        
    

    
