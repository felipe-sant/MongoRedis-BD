from src.data.mongo.connection import database

def deletarMongo(colecao, filtro):
    try:
        database[colecao].delete_one(filtro)
        return "Documento deletado com sucesso!"
    except Exception as e:
        return "Erro ao deletar documento!"
    
def deletarTodosMongo(colecao):
    try:
        database[colecao].delete_many({})
        return "Documentos deletados com sucesso!"
    except Exception as e:
        return f"Erro ao deletar documentos: {e}"