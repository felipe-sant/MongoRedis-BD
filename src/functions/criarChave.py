def criarChave(colecao, chave = None):
    if chave is None:
        while True:
            novaChave = input("Digite a chave: ")
            if novaChave == "":
                print("Chave inválida")
                continue
            chave = novaChave
            break
    
    chave = colecao + "@" + chave.replace(" ", "_").lower()
    return chave