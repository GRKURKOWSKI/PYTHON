print("--- COLETOR DE MATERIAIS ---")
print("Buscando materiais de construção reaproveitáveis para o app!")

mochila = 0
limite = 15.0

while mochila < limite:
    peso_material = float(input("\nQual o peso do material coletado (em kg)? "))
    
    if peso_material <= 0:
        print("Opa, peso inválido! Digite um número positivo.")
        continue
        
    if peso_material > limite - mochila:
        print(f"Mochila cheia! Esse material é muito pesado e não coube. Fechamos com {mochila} kg no total.")
        break
    else:
        mochila += peso_material
        espaco_livre = limite - mochila
        print(f"Material na conta! Esse pesava {peso_material} kg. Ainda cabem {espaco_livre} kg na nossa mochila.")