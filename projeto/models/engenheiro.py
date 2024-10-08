from projeto.models.funcionario import Funcionario
from projeto.models.endereco import Endereco
from projeto.models.enum.sexo import Sexo

class Engenheiro(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, salario_final: float, sexo: Sexo, crea: str) -> None:
        super().__init__(nome, telefone, email, endereco, salario_final, sexo)
        self.crea = crea

    def calcular_salario(self, salario_final):
        return super().calcular_salario(salario_final)