import pytest
from meuprojeto.models.pessoa import Pessoa #Caminho Relativo.
from meuprojeto.models.enum.sexo import Sexo #Caminho Absoluto.
from meuprojeto.models.endereco import Endereco
from meuprojeto.models.enum.unidade_federativa import Unidadefederativa


@pytest.fixture
def criar_pessoa():
    pessoa_1 = Pessoa("Silvinho",3,13,"777-888","silvinho@gmail.com",Sexo.FEMININO,
                    Endereco("rua dos senai","2","2 andar","22200022","Bahia",Unidadefederativa.SAO_PAULO)) 
    return pessoa_1

def test_pessoa_atributo_nome(criar_pessoa):
    assert criar_pessoa.nome == "Silvinho"

def test_pessoa_atributo_id(criar_pessoa):
    assert criar_pessoa.id == 3

def test_pessoa_atributo_dataNascimento(criar_pessoa):
    assert criar_pessoa.idade == 13

def test_pessoa_idade_negativa_retorna_mensagem_exececao(criar_pessoa):
    with pytest.raises(ValueError, match = "Idade não pode ser negativa"):
        Pessoa("Silvinho",3,-8,"777-888","silvinho@gmail.com",Sexo.FEMININO,
                    Endereco("rua dos senai","2","2 andar","22200022","Bahia",Unidadefederativa.SAO_PAULO))
