# Cálculo para verificar quantos dias faltam para o aniversário.

import datetime

def dias_aniversario(dia, mes):
    hoje = datetime.date.today()
    aniversario = datetime.date(hoje.year, mes, dia)
    
    if aniversario < hoje:
        aniversario = datetime.date(hoje.year + 1, mes, dia)
    
    dias = aniversario - hoje
    return dias.days

dia = int(input("Digite o dia do seu aniversário: "))
mes = int(input("Digite o mês do seu aniversário: "))

resultado = dias_aniversario(dia, mes)
print(f"Faltam {resultado} para o seu aniversário.")