# Exercício 3: Gerenciamento de contatos

def adicionar_contato(lista, nome, telefone, email):
    contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email
    }
    for c in lista:
        if c["nome"] == nome:
            print("Contato existente. Tente outro.")
            return
      
    lista.append(contato)
    

def buscar_contato(lista, nome):
    for busca in lista:
        if busca["nome"] == nome:
            return(busca)
    return None

def listar_contatos(lista):
    for listar in lista:
        print(listar["nome"])
        print(listar["telefone"])
        print(listar["email"])

def remover_contato(lista, nome):
    resultado = buscar_contato(lista, nome)
    if resultado == None:
        print("Esse contato não existe.")
    else:
        lista.remove(resultado)

def main():
    contatos = []
    adicionar_contato(contatos, "Vivian", "2796589541", "vivian@gmail.com")
    buscar_contato(contatos, "Vivian")
    listar_contatos(contatos)
    remover_contato(contatos, "Vivian")

if __name__ == "__main__":
    main()