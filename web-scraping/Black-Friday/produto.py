class Produto:
    def __init__(self, nome, preco, preco_anterior, link):
        self.nome = nome
        self.preco = preco
        self.preco_anterior = preco_anterior
        self.link = link
    
    def serialize(self):
        return {
            "nome" : self.nome,
            "preco" : self.preco,
            "preco_anterior" : self.preco_anterior,
            "link" : self.link
        }
     
    def from_json(self, json_):
        self.nome = json_["nome"]
        self.preco = json_["preco"]
        self.preco_anterior = json_["preco_anterior"]
        self.link = json_["link"]