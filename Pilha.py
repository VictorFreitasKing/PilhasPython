class Pilha():
    def __init__(self):
        self.__topo = None
        self.__tamanho = 0
        self.__iterando = None

    class Nó():
        def __init__(self, conteúdo):
            self.conteúdo = conteúdo
            self.próximo = None

    def __len__(self):
        return self.__tamanho

    def insert(self, x):
        novo = self.Nó(x)

        # se a pilha está vazia
        if self.__topo is None:
            self.__topo = novo  # Atualiza o topo

        else:  # se a pilha não está vazia

            # o próximo do novo aponta para o topo atual
            novo.próximo = self.__topo

            # o novo torna-se o topo
            self.__topo = novo

        self.__iterando = None
        self.__tamanho += 1

    def append (self, x):
        self.insert(x)

    def __delitem__(self):

        # se existem elementos na pilha, caso contrário, IndexError
        if len(self) > 0:

            # o topo passa a ser o valor seguinte
            self.__topo = self.__topo.próximo

            # decrementa o tamanho
            self.__tamanho -= 1

            self.__iterando = None

        else:
            raise IndexError("A pilha não tem elementos")

    def __next__(self):
        if self.__iterando is None:
            self.__iterando = self.__topo
        else:
            self.__iterando = self.__iterando.próximo

        if self.__iterando is not None:
            return self.__iterando.conteúdo

        raise StopIteration

    def __iter__(self):
        return self

    def __str__(self):
        retorno = '>'
        temp = self.__topo
        for i, e in enumerate(self):
            retorno += e.__repr__()

            if i < len(self) - 1:
                retorno += ', '

        retorno += '.'

        return retorno

    def __repr__(self):
        return self.__str__()

    def pop (self):
        temp = self.__topo.conteúdo
        self.__delitem__()
        return temp
