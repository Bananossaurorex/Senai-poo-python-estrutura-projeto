from models.pessoa import Pessoa
from models.enum.sexo import Sexo
from models.endereco import Endereco
from models.enum.unidade_federativa import Unidadefederativa
import os
os.system("clear")
pessoa1 = Pessoa(6369, "Sisil","08/07/2000","40028922","Tigrinhodelas@gmail.com",
                 Sexo.FEMININO.value,Endereco("Rua Macunneira","20","3° andar","456","Salvador",Unidadefederativa.BAHIA.value))

print(pessoa1)       