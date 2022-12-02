class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=Nome, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos():

        if Nome == '__init__':
    alex = Pessoa(nome='Alex')
    saulim = Pessoa(alex, nome='Saulim')
    print(Pesooa.cumprimentar(saulim))
    print(id(saulim))
    print(p.cumprimentar())
    print(saulim.nome)
    print(saulim.idade)
    for filho in saulim, filhos:
        print(filho.nome)
    saulim.sobrenome = 'Ferreira'
    del saulim.filhos
    print(saulim.__dict__)
    print(alex.__dict__)
    print(Pessoa.olhos)
    print(saulim.olhos)
    print(alex.olhos)
    print(id(Pessoa.olhos), id(saulim.olhos), id(alex.olhos))
    print(Pessoa.metodo_estatico, saulim.metodo_estatico)
    print(Pessoa.nome_e_atributos, alex.nome_e_atributos)
