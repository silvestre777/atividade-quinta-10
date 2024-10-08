import pytest
from projeto.models.endereco import Endereco
from projeto.models.medico import Medico
from projeto.models.enum.sexo import Sexo
from projeto.models.enum.unidadefederativa import UnidadeFederativa

@pytest.fixture
def criar_medico():
    return Medico("Silvao","987654321","revoada@gmail.com",
                  Endereco("Rua da casa","177","casa","2224401","Salvador",UnidadeFederativa.BAHIA),
                  2000.01,Sexo.MASCULINO,"6554632")

def test_nome_valido(criar_medico):
    assert criar_medico.nome == "Silvao"

def test_alterar_nome(criar_medico):
    criar_medico.nome = "Claudio"
    assert criar_medico.nome == "Claudio" 

def test_nome_vazio_invalido():
        with pytest.raises(TypeError, match="O nome não pode ser vazio"):
            Medico("","987654321","revoada@gmail.com",
                  Endereco("Rua da casa","177","casa","2224401","Salvador",UnidadeFederativa.BAHIA),
                  2000.01,Sexo.MASCULINO,"6554632")

def test_email_invalido_():
        with pytest.raises(TypeError, match= "O email deve conter o @ e mail.com"):
             Medico("Silvao","987654321","revoadagmail.co",
                  Endereco("Rua da casa","177","casa","2224401","Salvador",UnidadeFederativa.BAHIA),
                  2000.01,Sexo.MASCULINO,"6554632")