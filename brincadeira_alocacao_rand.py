"""
Código criado para tentar resolver a uma thread da lista de email Python-Brasil
URL da Thread: https://groups.google.com/forum/#!topic/python-brasil/jcKuMQcm-uM

Author do Código: Marcos Thomaz da Silva <marcosthomazs@gmail.com>
Currículo Lattes: http://lattes.cnpq.br/1710397494828508

Código ajustado em 16/04/2020 adicionando pesos para garantir uma melhor seleção,
juntamente com um método pseudoaleatório para permitir maior variação.
Adicionados parametros nos métodos monta_quinta e monta_domingo, para que seja
possível mudar a quantidade de pessoas em dadas funções sem o acréscimo de
linhas, e os nomes das pessoas agora saem em ordem alfabética.
"""
from random import choice

class Aloca:
    """
    Classe responsável por gerenciar a alocação dos responsáveis
    """
    def __init__(self, voluntarios, leitores, som):
        self._data = [voluntarios, leitores, som]
        self._idx = [0, 0, 0]
        self._max = [len(voluntarios), len(leitores), len(som)]
        md = lambda x : dict(zip(x, [0]*len(x)))
        self._height = [md(voluntarios), md(leitores), md(som)]

    def __pega_item(self, ignorar, indice):
        """
        Método responsável por obter um determinado indivíduo. Como a obtenção
        e validação do individuo era equivalente,indiferente da função exercida,
        foi criado este método como apoio.Foi ajustado para selecionar e validar
        o item usando uma lista de itens a ignorar, um controle de pesos que é
        incrementado cada vez que a pessoa é selecionada, e ainda um método
        pseudoaleatório para dar certa variação na seleção.
        Com a refatoração, houve a redução de um método, onde foi unificado o
        funcionamento de ambos em um só. 
        """
        w = self._idx[indice]
        weights = self._height[indice]
        data = self._data[indice]
        sublist = list(
            filter(lambda x: weights[x] == w and x not in ignorar, data))
        inicio = w
        while len(sublist) == 0:            
            w += 1
            if (w - inicio) > 2:
                raise Exception('Solução não encontrada!')
            sublist = list(
                filter(lambda x: weights[x] == w and x not in ignorar, data))
        self._idx[indice] = w
        item  = choice(sublist)
        self._height[indice][item] += 1
        return item

    def pega_voluntario(self, ignorar=[]):
        yield self.__pega_item(ignorar, 0)

    def pega_leitor(self, ignorar=[]):
        yield self.__pega_item(ignorar, 1)

    def pega_som(self, ignorar=[]):
        yield self.__pega_item(ignorar, 2)

    def _base_alocacao(self, ignorar=[]):
        """
        Como as alocações de quinta e de domingo diferem apenas na presença do
        leitor, foi criado este método que monta uma alocação básica,equivalente
        a de quinta, e retorna a lista de itens a ignorar. Inicia alocando pela
        equipe de SOM que é menor, para permitir uma maior variedade de pares.
        Aqui poderia haver um estudo em algum tipo de 'base histórica' para
        aumentar ainda mais a variedade de equipes.
        """
        qtd_som = 1
        qtd_ind = 2
        qtd_vol = 2

        som = []
        ind = []
        vol = []

        for i in range(qtd_som):
            som.append(next(self.pega_som(ignorar)))
            ignorar.append(som[-1])

        for i in range(qtd_ind):
            ind.append(next(self.pega_voluntario(ignorar)))
            ignorar.append(ind[-1])

        for i in range(qtd_vol):
            vol.append(next(self.pega_voluntario(ignorar)))
            ignorar.append(vol[-1])

        return {
            'indicadores': sorted(ind), 'volantes': sorted(vol),
            'operador_som': sorted(som), 'leitor': []
        }, ignorar

    def monta_quinta(self):
        """
        Método que monta a alocação de quinta. Basicamente a mesma alocação
        gerada pelo método básico
        """
        ignorar = []
        return self._base_alocacao(ignorar)[0]

    def monta_domingo(self):
        """
        Método que monta a alocação de domingo, que basicamente insere a
        presença do leitor na lista de funções. Como os leitores são
        'menos presentes', temos o início da alocação a partir deles,
        permitindo uma variedade maior de grupos
        """

        qtd_leit = 1
        leit = []
        ignorar = []
        for i in range(qtd_leit):
            leit.append(next(self.pega_leitor(ignorar)))
            ignorar.append(leit[-1])

        b, i = self._base_alocacao(ignorar)
        b['leitor'] = sorted(leit)
        return b


def aloca(alocacao):
    print(alocacao.monta_quinta())
    print(alocacao.monta_domingo())

if __name__ == '__main__':
    """
    Monta um exemplo com base nas especificações do problema
    """
    voluntarios = [
        'Alexandre', 'João', 'Natanael', 'Renato', 'Eduardo', 'Leonardo',
        'Ronaldo', 'Ferreira', 'Santos', 'Monticelli', 'Claudio', 'Nelson'
    ]
    leitores = [
        'Alexandre', 'Leonardo', 'Ronaldo', 'Renato', 'Eduardo', 'Nelson',
        'Monticelli'
    ]
    som = ['Alexandre', 'Leonardo', 'Eduardo', 'Natanael']
    alocacao = Aloca(voluntarios, leitores, som)
    for i in range(4):
        aloca(alocacao)
