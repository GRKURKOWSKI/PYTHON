print("--- MONITOR DE TEMPERATURA ---")

total_dias = int(input("Quantos dias vamos analisar? "))

if total_dias <= 0:
    print("Opa, quantidade inválida! Digita um número maior que zero.")
else:
    soma_temp = 0.0
    dia_atual = 0
    
    while dia_atual < total_dias:
        temp_dia = float(input(f"Qual foi a temperatura do dia {dia_atual + 1}? "))
        soma_temp += temp_dia
        dia_atual += 1
        
    media_final = soma_temp / total_dias
    
    print(f"\nA média de temperatura nesses {total_dias} dias foi de {media_final:.2f}°C")
    
    if media_final > 25:
        print("Tá quente! Média de temperatura acima do esperado.")
    else:
        print("Tranquilo! Média de temperatura dentro da normalidade.")