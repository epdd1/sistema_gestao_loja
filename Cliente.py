class Cliente:
    def __init__(self, nome, email, pontos_fidelidade = 0):
        self.nome = nome
        self.email = email
        self.pontos_fidelidade = pontos_fidelidade
    
    def adicionar_pontos (self, pontos):
        self.pontos_fidelidade += pontos
    
    def resgatar_pontos (self, pontos):
        if(pontos <= self.pontos_fidelidade):
            self.pontos_fidelidade -= pontos
        else: f'Os pontos não foram resgatados, saldo é: {self.pontos_fidelidade}'
    
    def verificar_vip (self):
        if (self.pontos_fidelidade >= 1000):
            return f' o {self.nome} é vip'
        else: return f'O {self.nome} não é vip'
    
    def __eq__(self, other):
        if (self.email == other):
            return f'{True} Os emais são iguais!'
        else: return f'{False} Os emails são diferentes'

    def __iadd__ (self, pontos):
        if (isinstance(pontos, int)):
            return Cliente(self.pontos_fidelidade + pontos)
        return Cliente(self.pontos_fidelidade + pontos)
    
    def __str__(self):
        return f'Cliente: {self.nome} | Email: {self.email} | Pontos: {self.pontos_fidelidade}'