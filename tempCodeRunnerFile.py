class Cachorro:
    def __init__(self, raca, sexo, cor, idade, altura_do_latido):
        self.raca = raca
        self.sexo = sexo
        self.cor = cor
        self.idade = idade
        self.altura_do_latido = altura_do_latido
        self.quantidade_de_patas = 4
        self.olhos = 2

    def latir(self):
        print(f"O {self.raca} deu um latido {self.altura_do_latido}")

    def informacoes(self):
        #self.olhos = self.perderUmOlho(self.olhos)

        print(f"Raça: {self.raca}")
        print(f"Sexo: {self.sexo}")
        print(f"Cor: {self.cor}")
        print(f"Idade: {self.idade}")
        print(f"Patas: {self.quantidade_de_patas}")
        print(f"Olhos: {self.olhos}")

    def perderUmOlho(self, olhos):
        return olhos - 1


if __name__ == "__main__":
    raca = "poodle"
    poodle = Cachorro(
        raca=raca,
        sexo="Masculino",
        cor="Branco",
        idade=2,
        altura_do_latido="Médio",
    )
    salsicha = Cachorro(
        raca=raca,
        sexo="Masculino",
        cor="Marrom",
        idade=5,
        altura_do_latido="Alto",
    )

    salsicha.informacoes()
