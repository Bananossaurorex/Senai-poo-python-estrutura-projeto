from models.enum.unidade_federativa import Unidadefederativa
class Endereco:
    def __init__(self, logradouro: str, numero:  str, complemento: str, cep: str, cidade: str, unidade_federativa:Unidadefederativa) -> None:
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade
        self.unidade_federativa = unidade_federativa
    
    def __str__(self) -> str:
        return(
        f"Logadouro: {self.logradouro}"
        f"\nNúmero: {self.numero}"
        f"\nComplemento: {self.complemento}"
        f"\nCep: {self.cep}"
        f"\nCidade: {self.cidade}"  
        f"\nUnidade Federativa: {self.unidade_federativa}" 
        )