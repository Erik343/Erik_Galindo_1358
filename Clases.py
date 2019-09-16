class Comic:
    def __init__(self, genero, empresa,estructura):
        self.__genero = genero
        self.__empresa = empresa
        self.__estructura = estructura

    def get_genero(self):
        return self.__genero

    def set_genero(self, genero):
        self.__genero = genero

    def get_empresa(self):
        return self.__empresa

    def set_empresa(self,empresa):
        self.__empresa = empresa

    def get_estructura(self):
        return self.__estructura

    def set_estructura(self, estructura):
        self.__estructura = estructura


def main():
    c = Comic("accion/romance", "MARVEL", "viñetas, prosopopeyas, paradojas")
    print(f"genero : {c.get_genero()}, empresa: {c.get_empresa()} , estrcutura: {c.get_estructura()}")
main()