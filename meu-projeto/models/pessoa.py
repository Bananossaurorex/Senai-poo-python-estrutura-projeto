from models.enum.sexo import Sexo
from models.endereco import Endereco
class Pessoa:
    def __init__(self, id: int, nome: str, dataNascimento: str, telefone: str, email: str, sexo: Sexo, endereco: Endereco) -> None:
        self.id = id
        self.nome = nome
        self.dataNascimento = dataNascimento
        self.telefone = telefone
        self.email = email
        self.sexo = sexo
        self.endereco = endereco
    def __str__(self) -> str:
        return  (
                f"--Pessoa--\n"
                f"Nome: {self.nome}"
                f"\nId: {self.id}"
                f"\nData nascimento: {self.dataNascimento}"
                f"\nTelefone: {self.telefone}"
                f"\nEmail: {self.email}"
                f"\nSexo: {self.sexo}\n"
                f"\n--Endereço--\n{self.endereco}"
                )
    