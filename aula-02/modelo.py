class Filme:
    def __init__(self, nome, ano, duracao):
        self.__nome = nome.capitalize()
        self.ano = ano
        self.duracao = duracao
        self.__likes = 0

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def likes(self):
        return self.__likes

    def dar_like(self):
        self.__likes += 1


class Serie:
    def __init__(self, nome, ano, temporadas):
        self.__nome = nome.capitalize()
        self.ano = ano
        self.temporadas = temporadas
        self.__likes = 0

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def likes(self):
        return self.__likes

    def dar_like(self):
        self.__likes += 1


# A herança não herdará os atributos privados (que foram precedidos pelo __), assim, eles poderão
# ser acessados apenas através dos métodos getters e setters.
class Teste(Serie):
    pass


vingadores = Filme('Vingadores', 2018, 160)
vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()
print(
    f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duração: {vingadores.duracao} minutos - Likes: {vingadores.likes}')

atlanta = Serie('Atlanta', 2018, 2)
print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} - Temporadas: {atlanta.temporadas} - Likes: {atlanta.likes}')
