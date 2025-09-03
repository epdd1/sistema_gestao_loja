class Pedido:
    def __init__(self, cliente, produto, quantidade, status):
        if isinstance(cliente, Cliente):
            self.cliente = cliente
        else: self.cliente = None
        if isinstance(produto, Produto):
            self.produto = produto
        else: self.produto = None
        self.quantidade = quantidade
        self.status = status
    
    def calcula_preco(self):
        return self.produto.preco * peso_total
    
    def calcular_peso_total(self):
        peso_total = self.produto.peso_kg * self.quantidade
        return peso_total
    
    def atualizar_status (self, novo_status):
        if (self.status == "entregue"):
            return "Seu pedido já foi entregue, não há mudança a ser feita"
        elif(self.status == 'processando' and novo_status == "entregue"):
            self.status = novo_status
        else: self.status = novo_status
    
    def cancelar_pedido(self):
        if (self.status == 'processando'):
            return "Seu pedido foi cancelado com sucesso"
        else: return "Seu pedido não pode ser cancelado"
    
    def __add__ (self, other):
        if (self.produto == other.produto):
            self.quantidade += other.quantidade
        else: return "são clientes diferentes"
    
    def __lt__ (self, other):
        if (self.calcular_peso_total() > other.calcula_peso_total()):
            return f' O peso total do {self.cliente} é maior que o do {other}'
        else: return f' O peso total do {self.cliente} é MENOR que o do {other}'
    
    def __call__(self):
        return f' pedido: {self.produto} {self.quantidade}'