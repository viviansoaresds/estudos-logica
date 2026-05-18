# Exercício 1: Cadastro de professores de uma escola com exibição de dados

escola = []
professor1 = {"nome": "Gustavo",
           "sexo": "M",
           "disciplina": "português",
           "idade": 58
           }

professor2 = {"nome": "Leandra",
           "sexo": "F",
           "disciplina": "matemática",
           "idade": 32
           }

professor3 = {"nome": "João",
           "sexo": "M",
           "disciplina": "história",
           "idade": 41
           }

escola.append(professor1)
escola.append(professor2)
escola.append(professor3)

for professor in escola:
    for c, v in professor.items():
        if c == "idade" or c == "disciplina":
            artigo = "A"
        else:
            artigo = "O"
        print(f"{artigo} {c} é {v}")

