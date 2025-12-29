def formatar_saldo(valor):
    VERDE = '\033[32m'
    VERMELHO = '\033[31m'
    RESET = '\033[0m'
    
    if valor >= 0:
        return f"{VERDE}R$ {valor:.2f}{RESET}"
    else:
        return f"{VERMELHO}R$ {valor:.2f}{RESET}"

# Teste
print(f"Seu saldo atual é: {formatar_saldo(150.50)}")
print(f"Seu saldo atual é: {formatar_saldo(-50.25)}")