import pytest
from projeto.models.engenheiro import Engenheiro
from projeto.models.endereco import Endereco
from projeto.models.enum.sexo import Sexo
from projeto.models.enum.unidadefederativa import UnidadeFederativa


@pytest.fixture
def criar_engenheiro():
    engenheiro = Engenheiro("Silvestre", "71", "silvestre.ferreira@gmail.com",
                            Endereco("Rua A", "788", "casa", "4111", "Salvador", UnidadeFederativa.BAHIA), 7000, Sexo.MASCULINO, "111")
    return engenheiro

def test_nome_engenheiro(criar_engenheiro):
    assert criar_engenheiro.nome == "Silvestre"

def test_nome_vazio_do_engenheiro():
    with pytest.raises(TypeError,match = "O nome não pode ser vazio"):
        Engenheiro("", "71", "silvestre.ferreira@gmail.com",
                            Endereco("Rua A", "788", "casa", "4111", "Salvador", UnidadeFederativa.BAHIA), 7000, Sexo.MASCULINO, "111")

def test_email_engenheiro():
    with pytest.raises(TypeError,match = "O email deve conter o @ e mail.com"):
        Engenheiro("Silvestre", "71", "silvestre.ferreiragmail.c",
                            Endereco("Rua A", "788", "casa", "4111", "Salvador", UnidadeFederativa.BAHIA), 7000, Sexo.MASCULINO, "111")