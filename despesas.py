# fazer controlo de despesas anuais e mensais
# mes que gastou mais e menos
# categorias que gastou mais e menos
import ler_dados
from calculator import soma_mes

def controlo_despesas():
    months={"01":"January", "02":"February", "03":"March", "04":"April",
         "05":"May", "06":"June", "07":"July", "08":"August",
         "09":"September", "10":"October", "11":"November", "12":"December"}
    maior_gasto = 0
    mes_maior_gasto = ''
    for i in range(1,13):
        positivo_mes, negativo_mes, saldo_mes = soma_mes(f"{i:02d}")
        if negativo_mes > maior_gasto:
            maior_gasto = negativo_mes
            mes_maior_gasto = f"{i:02d}" #mes com maior gasto
        else: 
            continue

    print("="*50)
    print(f"The month with the highest expenses is {months[mes_maior_gasto]} with a total expense of {maior_gasto:.2f}€.")
    print("="*50)

if __name__ == "__main__":
    controlo_despesas()

