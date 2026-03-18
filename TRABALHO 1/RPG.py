print("--- BEM VINDO AO RPG EPICO ---")
print("Prepare-se! Kvothe encontrou um monstro no caminho!")

vida_heroi = 100
vida_monstro = 100
rodada = 1

while vida_heroi > 0 and vida_monstro > 0:
    print(f"\n--- Rodada {rodada} ---")
    
    ataque_meu = int(input("Qual a força do seu ataque? (1 a 20): "))
    if ataque_meu < 1 or ataque_meu > 20:
        print("Ixi, valor errado! Digite um número de 1 a 20.")
        continue
        
    ataque_bicho = int(input("Qual a força do ataque do monstro? (1 a 20): "))
    if ataque_bicho < 1 or ataque_bicho > 20:
        print("Ixi, valor errado! Digite um número de 1 a 20.")
        continue
        
    vida_monstro -= ataque_meu
    vida_heroi -= ataque_bicho
    
    print(f"Você atacou! A vida do monstro caiu para {vida_monstro}.")
    print(f"O monstro revidou! Sua vida agora é {vida_heroi}.")
    
    if vida_heroi <= 0:
        print("Deu ruim... Você foi derrotado pelo monstro! :(")
    elif vida_monstro <= 0:
        print("VAMOS! Você derrotou o monstro! GG!")
        
    rodada += 1