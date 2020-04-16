from random import randint

class Aloca:
    def __init__(self, voluntarios, leitores, som):
        self.voluntarios = voluntarios
        self.leitores = leitores
        self.som = som
        self._idx = [0, 0, 0]
        self._max = [len(voluntarios), len(leitores), len(som)]

    def __inc_and_get_idx(self, indice):
        result = self._idx[indice]
        self._idx[indice] += 1
        if self._idx[indice] >= self._max[indice]:
            self._idx[indice] = 0
        return result

    def __pega_item(self, ignorar, lista, indice):
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

    def _base_alocacao(self):
        ignorar = []
        i1 = next(self.pega_voluntario(ignorar))
        ignorar.append(i1)
        i2 = next(self.pega_voluntario(ignorar))
        ignorar.append(i2)
        v1 = next(self.pega_voluntario(ignorar))
        ignorar.append(v1)
        v2 = next(self.pega_voluntario(ignorar))
        ignorar.append(v2)
        s = next(self.pega_som(ignorar))
        ignorar.append(s)
        return {
            'indicadores': [i1, i2],
            'volantes': [v1, v2],
            'operador_som': [s],
            'leitor': []
        }, ignorar

    def monta_quinta(self):
        return self._base_alocacao()[0]

    def monta_domingo(self):
        b, ignorar = self._base_alocacao()
        l = next(self.pega_leitor(ignorar))
        b['leitor'].append(l)
        return b

voluntarios = [ 'Alexandre', 'João', 'Natanael', 'Renato', 'Eduardo', 'Leonardo', 'Ronaldo', 'Ferreira', 'Santos', 'Monticelli', 'Claudio', 'Nelson']
leitores = ['Alexandre', 'Leonardo', 'Ronaldo', 'Renato', 'Eduardo', 'Nelson', 'Monticelli']
som = ['Alexandre', 'Leonardo', 'Eduardo', 'Natanael']
alocacao = Aloca(voluntarios, leitores, som)
