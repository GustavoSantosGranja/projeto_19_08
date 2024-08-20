from datetime import date

# Classe Endereço
class Endereco:
    def __init__(self, logradouro="", numero="", endereco_Comercial=False):
        # Inicializar os atributos com valores padrão
        self.logradouro = logradouro
        self.numero = numero
        self.endereco_Comercial = endereco_Comercial

# Classe Pessoa
class Pessoa: 
    def __init__(self, nome="", rendimento=0.0, endereco=None):
        self.nome = nome
        self.rendimento = rendimento
        self.endereco = endereco 
    
    def calcular_imposto(self, rendimento):
        pass
        
# Classe Pessoa Fisica
class PessoaFisica(Pessoa):
    def __init__(self, nome="", rendimento=0.0, endereco=None, cpf="", dataNascimento=None):
        if endereco is None:
            # Se nenhum endereço for fornecido, cria um objeto de endereço padrão
            endereco = Endereco()
        
        if dataNascimento is None:
            dataNascimento = date.today()

        super().__init__(nome, rendimento, endereco)

        # Atributos próprios da classe
        self.cpf = cpf
        self.dataNascimento = dataNascimento
    
    def calcular_imposto(self, rendimento: float) -> float:
        # Sem imposto para rendimentos até 1500
        if rendimento <= 1500:
            return 0
        # 2% de imposto para rendimento entre 1500 e 3500
        elif 1500 < rendimento <= 3500:
            return (rendimento / 100) * 2
        # 3.5% de imposto para rendimentos entre 3500 e 6000
        elif 3500 < rendimento <= 6000:
            return (rendimento / 100) * 3.5
        # 5% de impostos para rendimentos acima de 6000
        else: 
            return rendimento * 5
        
# Classe Pessoa Juridica
class PessoaJuridica(Pessoa):
        def __init__(self, nome="", rendimento=0.0, endereco=None, cnpj=""):
            if endereco is None:
            # Se nenhum endereço for fornecido, cria um objeto de endereço padrão
                endereco = Endereco()
        
            super().__init__(nome, rendimento, endereco)

        def calcular_imposto(self, rendimento: float) -> float:
        # Sem imposto para rendimentos até 1500
            if rendimento <= 1500:
                return 0
        # 2% de imposto para rendimento entre 1500 e 3500
            elif 1500 < rendimento <= 3500:
                return (rendimento / 100) * 2
        # 3.5% de imposto para rendimentos entre 3500 e 6000
            elif 3500 < rendimento <= 6000:
                return (rendimento / 100) * 3.5
        # 5% de impostos para rendimentos acima de 6000
            else: 
                return rendimento * 5
