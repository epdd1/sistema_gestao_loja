class Produto:
    def __init__(self, nome, preco, estoque, peso_kg):
        self.nome = nome
        if (preco>=0):
            self.preco = preco
        else: self.preco = None
        self.estoque = estoque
        if (peso_kg >= 0):
           self.peso_kg = peso_kg
        else: self.peso_kg = None
    
    def atualizar_peso (self, novo_peso):
        if(novo_peso >= 0):
            self.peso_kg = novo_peso
        else: return f' o peso {novo_peso} é inválido'
    
    def desconto (self, percent):
        if (percent >= 0):
            self.preco *= (1-percent)
        else: return f'O percentual {percent} informado é inválido'
    
    def verificar_estoque_baixo (self):
        if (self.estoque < 5):
            return f'{True} O estoque {self.estoque} tem menos que 5'
        else: return f'{False} O estoque {self.estoque} tem MAIS de 5'

    def __eq__(self, other):
        if (self.nome == other.nome() and self.preco == other.preco()):
            return f'{True} O nome e o preço são os mesmos'
        else: return f'{False} O nome ou o preço são DIFERENTES'
    
    def __str__(self):
        return f'Produto {self.nome} | Preço: {self.preco} | Estoque: {self.estoque}'
        

