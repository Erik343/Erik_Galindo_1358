class Array:
    def __init__(self, n):
        self.__data = []
        for i in range(n):
            self.__data.append(None)

    def to_string(self):
        print(self.__data)
    def get_length(self):
        return len(self.__data)

    def set_item(self, index,value):
        if index >=0 and index < len(self.__data):
            self.__data[index] = value
        else:
            print("error de longitud")

    def get_item(self, index):
        if index >=0 and index < len(self.__data):
            return self.__data[index]
        else:
            print("fuera de rango")

    def clearing(self, valor):
        for index in range(len(self.__data)):
            self.__data[index] = valor

def main():
    arreglo = Array(10) #define el tamaño del arreglo
    arreglo.to_string() #imorime el contenido del arreglo
    print(arreglo.get_length()) #imprime el tamaño de mi arreglo
    arreglo.set_item(1,10)#indice y que valor le vas a poner en ese indice
    arreglo.to_string()
    #arreglo.set_item(12,10)
    print(f"el elemnto 1 del arreglo es: {arreglo.get_item(30)}")
    arreglo.clearing(5) #te inicializatodo el arreglo con el valor que indiques
    arreglo.to_string()
main()

'''
Array2D(filas,columnas)
get_num_rows() --> regresa una fila
get_num_cols() --> regresa columnas
clearing(value)
set_item(r,c,valor)
get_item(r,c)
'''