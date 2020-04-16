"""
Código criado para tentar resolver a uma thread da lista de email Python-Brasil
Link da Thread: https://groups.google.com/forum/#!topic/python-brasil/jcKuMQcm-uM

Author do Código: Marcos Thomaz da Silva <marcosthomazs@gmail.com>
Currículo Lattes: http://lattes.cnpq.br/1710397494828508
"""
from random import randint

class Aloca:
    """
    Classe responsável por gerenciar a alocação dos responsáveis
    """
    def __init__(self, voluntarios, leitores, som):
        self.voluntarios = voluntarios
        self.leitores = leitores
        self.som = som
        self._idx = [0, 0, 0]
        self._max = [len(voluntarios), len(leitores), len(som)]

    def __inc_and_get_idx(self, indice):
        """
        Método responsável por obter um novo valor do índice. Poderia ser feito apenas o incremento,
        validando as dimensões da lista, porém, foi pego um valor pseudo-aleatório para possibilitar que
        sejam selecionadas equipes distintas
        """
        return randint(0, self._max[indice]-1)

    def __pega_item(self, ignorar, lista, indice):
        """
        Método responsável por obter um determinado indivíduo. Como a obtenção e validação do
        individuo era equivalente, indiferente da função exercida, foi criado este método como apoio.
        """
        idx = self.__inc_and_get_idx(indice)
        i = lista[idx]
        while i in ignorar:
            idx = self.__inc_and_get_idx(indice)
            i = lista[idx]
        return i            

    def pega_voluntario(self, ignorar=[]):
        yield self.__pega_item(ignorar, self.voluntarios, 0)

    def pega_leitor(self, ignorar=[]):
        yield self.__pega_item(ignorar, self.leitores, 1)

    def pega_som(self, ignorar=[]):
        yield self.__pega_item(ignorar, self.som, 2)

    def _base_alocacao(self, ignorar=[]):
        """
        Como as alocações de quinta e de domingo diferem apenas na presença do leitor, foi
        criado este método que monta uma alocação básica, equivalente a de quinta, e retorna
        a lista de itens a ignorar. Inicia alocando pela equipe de SOM que é menor, para
        permitir uma maior variedade de pares.
        Aqui poderia haver um estudo em algum tipo de 'base histórica' para aumentar ainda mais
        a variedade de equipes.
        """
        s = next(self.pega_som(ignorar))
        ignorar.append(s)
        i1 = next(self.pega_voluntario(ignorar))
        ignorar.append(i1)
        i2 = next(self.pega_voluntario(ignorar))
        ignorar.append(i2)
        v1 = next(self.pega_voluntario(ignorar))
        ignorar.append(v1)
        v2 = next(self.pega_voluntario(ignorar))
        ignorar.append(v2)
        return {
            'indicadores': [i1, i2],
            'volantes': [v1, v2],
            'operador_som': [s],
            'leitor': []
        }, ignorar

    def monta_quinta(self):
        """
        Método que monta a alocação de quinta. Basicamente a mesma alocação gerada pelo
        método básico
        """
        return self._base_alocacao()[0]

    def monta_domingo(self):
        """
        Método que monta a alocação de domingo, que basicamente insere a presença do leitor
        na lista de funções. Como os leitores são 'menos presentes', temos o início da alocação
        a partir deles, permitindo uma variedade maior de grupos
        """
        ignorar = []
        l = next(self.pega_leitor(ignorar))
        ignorar.append(l)
        b, ignorar = self._base_alocacao(ignorar)
        b['leitor'].append(l)
        return b


if __name__ == '__main__':
    """
    Monta um exemplo com base nas especificações do problema
    """
    voluntarios = [ 'Alexandre', 'João', 'Natanael', 'Renato', 'Eduardo', 'Leonardo', 'Ronaldo', 'Ferreira', 'Santos', 'Monticelli', 'Claudio', 'Nelson']
    leitores = ['Alexandre', 'Leonardo', 'Ronaldo', 'Renato', 'Eduardo', 'Nelson', 'Monticelli']
    som = ['Alexandre', 'Leonardo', 'Eduardo', 'Natanael']
    alocacao = Aloca(voluntarios, leitores, som)
    print(alocacao.monta_quinta())
    print(alocacao.monta_domingo())
    print(alocacao.monta_quinta())
    print(alocacao.monta_domingo())
    
