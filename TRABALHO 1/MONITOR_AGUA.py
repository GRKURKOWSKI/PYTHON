print("--- MONITOR DE ENCHENTE ---")

nivel_agua = 0.0

while nivel_agua >= 0:
    nivel_agua = float(input("\nQual a altura da água em metros? (digite um número negativo para sair): "))
    
    if nivel_agua < 0:
        print("Desligando o monitor. Fiquem seguros, galera!")
    elif nivel_agua < 3:
        print("Tudo de boa. Nível normal e sem perigo.")
    elif nivel_agua >= 3 and nivel_agua <= 5:
        print("Opa, a água tá subindo! Melhor a gente ficar alerta.")
    else:
        print("Água muito alta! Como eu só tenho 10 anos, já vou logo chamando os adultos pra gente sair daqui rápido!")