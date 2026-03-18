print("--- CULTIVATOR 2.0 ---")
print("Vamos compensar nosso impacto plantando algumas árvores!")

meta_arvores = int(input("Qual a sua meta de árvores? "))
plantadas_agora = 0
dias = 0

while plantadas_agora < meta_arvores:
    dias += 1
    novas_mudas = int(input(f"\n[Dia {dias}] Quantas mudas você plantou hoje? "))
    plantadas_agora += novas_mudas
    
    if plantadas_agora >= meta_arvores:
        print(f"Aí sim! Parabéns, você atingiu a meta de reflorestamento em {dias} dia(s)! O planeta agradece.")
    else:
        faltam = meta_arvores - plantadas_agora
        print(f"Boa! Faltam só {faltam} árvores para batermos a meta. Continua o trabalho amanhã!")