'''
get_size() -->regresa el tamaño
insert(value) --> inserta un valor simepre al final
find_from_head(value) --> busca de la cabeza hacia la derecha
fing_from_tail(value) --> busca de tail(cola ) hacia la izquierda
remove_from_head(value)-->
remove_from_tail(value)-->
insert_between(value.predecesor,sucesor)--> despues y antes
transversal() -->desde head a tail
reverse() --> tail a head
'''

class NodoDoble:
    def __init__(self,value,siguiente,previo):
        self.data = value
        self.next = siguiente
        self.prev = previo

class ListaDoblmenteEnlazada:
    def __init__(self):
        self.__head = NodoDoble(None,None,None)
        self.__tail = NodoDoble(None,None,None)
        self.__head.next = self.__tail
        self.__tail.prev = self.__head
        self.__size=0

    def get_size(self):
        return self.__size

    def insert(self,value):
        '''inserta al final'''
        if self.__size ==0:
            nuevo= NodoDoble(value,self.__tail,self.__head) # head.next = nuevo --> tail.prevo = nuevo
            self.__head.next = nuevo #al insertar un elemento en lista
            self.__tail.prev = nuevo
        else:
            nuevo = NodoDoble(value,self.__tail,self.__tail.prev)
            self.__size += 1 # head y tail nunca tendran valor unicamente sirven de pivote
            self.__tail.prev.next = nuevo
            self.__tail.prev = nuevo
        self.__size +=1

    def transversal(self):
        curr_Node = self.__head
        while curr_Node.next != None:
            print(curr_Node.data,"->",end="")
            curr_Node = curr_Node.next
        print("")

    def reserve_transversal(self):
        curr_Node = self.__tail
        while curr_Node.prev != None:
            print(curr_Node.data,"->",end="")
            curr_Node = curr_Node.prev
        print("")

    def find_from_head(self,value):
        curr_Node = self.__head
        encontrado = None
        while curr_Node.next != None:
            curr_Node=curr_Node.next
        if curr_Node.data == value:
            encontrado = curr_Node
        curr_Node = curr_Node.next
        return encontrado

    def fid_from_tail(self,value):
        curr_Node = self.__tail
        encontrado = None
        while curr_Node.prev != value:
            curr_Node = curr_Node.prev.tail
        if curr_Node.data == value:
            encontrado = curr_Node.prev
        curr_Node= curr_Node.prev
        return encontrado

    def is_empty(self):
        return self.get_size() ==0


    def remove_from_tail(self):
        if self.__size==0:
            print("lista vacia")
        else:
            self.__head = self.__head.next
            self.__tail.prev.next= None
        self.__size -=1

    def remove_from_head(self,value):
        result = self.find_from_head(value)
        if result!= None:
            result.prev.next = result.next
            result.next.prev = result.prev
            result = None
        self.__size-=1

    def insert_between(self,value,predecesor,sucesor):
        nuevo = NodoDoble(value,sucesor,predecesor)
        sucesor.prev = nuevo
        predecesor.next = nuevo
        self.__size +=1

def main():
    Ldl = ListaDoblmenteEnlazada() #instacia de la clase
    print(f"tamaño = {Ldl.get_size()}") #obteniendo el tamaño de la lista
    Ldl.insert(10)
    Ldl.insert(20)
    Ldl.insert(30)
    Ldl.insert(40)
    Ldl.insert(50)
    print(f"tamaño = {Ldl.get_size()}") #obteniendo el tamaño de la lista
    Ldl.transversal()
    Ldl.reserve_transversal()
    print(Ldl.is_empty())
    print(Ldl.transversal())
    print(Ldl.get_size())
    result = Ldl.find_from_head(30)
    if result != None:
        print(f"dato {result.data}")
    else:
        print("dato no encontrado")
    Ldl.remove_from_head(30)
    Ldl.transversal()
    result2 = Ldl.find_from_head(30)
    Ldl.insert_between(35,result2,result2.next)

main()