class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo o objeto {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite".format(valor))

    def __pode_sacar(self, valor):
        valor_disponivel_para_sacar = self.__saldo + self.__limite
        return valor <= valor_disponivel_para_sacar

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    def extrato(self):
        print("Saldo {} do titular {}".format(self.__saldo, self.__titular))

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, valor):
        self.__limite = valor

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {'BB':'001', 'Caixa':'104', 'Bradesco':'237'}