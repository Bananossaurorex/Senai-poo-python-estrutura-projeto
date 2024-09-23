from ..models.enum.sexo import Sexo
from ..models.endereco import Endereco

class Pessoa:
    def __init__(self, nome: str,id: int, idade: int, telefone: str, email: str, sexo: Sexo, endereco: Endereco) -> None:
        if idade < 0:
            raise ValueError("Idade não pode ser negativa")
        self.nome = nome
        self.id = id
        self.idade = idade
        self.telefone = telefone
        self.email = email
        self.sexo = sexo
        self.endereco = endereco
    def __str__(self) -> str:
        return  (
                f"--Pessoa--\n"
                f"Nome: {self.nome}"
                f"\nId: {self.id}"
                f"\nData nascimento: {self.idade}"
                f"\nTelefone: {self.telefone}"
                f"\nEmail: {self.email}"
                f"\nSexo: {self.sexo.texto}\n"
                f"\nSexo: {self.sexo.caracter}\n"
                f"\n--Endereço--\n{self.endereco}"
                )
    