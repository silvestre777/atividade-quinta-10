from abc import ABC, abstractmethod
from projeto.models.endereco import Endereco
from projeto.models.enum.sexo import Sexo


class Funcionario(ABC):
    def __init__(self,nome: str, telefone: str, email: str, endereco: Endereco, salario_final: float, sexo: Sexo) -> None:
        self.nome = self._nome_vazio(nome)
        self.telefone = self._telefone_vazio(telefone)
        self.email = self._email_invalido(email)
        self.endereco = endereco
        self.salario_final = salario_final
        self.sexo = sexo

    @abstractmethod
    def calcular_salario(self,salario_final):
        pass

    def _email_invalido(self,email):
        if "@" and "mail.com" not in email:
            raise TypeError("O email deve conter o @ e mail.com")
        return email
    
    def _telefone_vazio(self, telefone):
        if not telefone.stip():
            raise TypeError("O numero não pode ser vazio")
        return telefone
    
    def _nome_vazio(self,nome):
        if not nome.strip():
            raise TypeError("O nome não pode ser vazio")
        return nome

    def __str__(self) -> str:
        return (
            f"Nome: {self.nome}"
            f"\nNome: {self.nome}"
            f"\nTelefone: {self.telefone}"
            f"\nEmail: {self.email}"
            f"\nSalario: {self.salario_final}"
            f"\nSexo: {self.sexo.name}"
            f"\n{self.endereco}"
        )