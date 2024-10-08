from projeto.models.enum.unidadefederativa import UnidadeFederativa

class Endereco:
    def __init__(self, logradouro:str, numero: str, complemento:str, cep:str, cidade:str, uf : UnidadeFederativa) -> None:
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade
        self.uf = uf


    def __str__(self) -> str:
        return(
        f"Logadouro: {self.logadouro}"
        f"Número: {self.numero}"
        f"Complemento: {self.complemento}"
        f"Cep: {self.cep}"
        f"Cidade: {self.cidade}"
        f"Unidade Federativa: {self.uf}"
        )