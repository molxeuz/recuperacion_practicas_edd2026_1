
class Node:

  __slots__ = ('__value', '__next')

  def __init__(self, value):
    self.__value = value
    self.__next = None

  @property
  def value(self):
    return self.__value

  @property
  def next(self):
    return self.__next

  @value.setter
  def value(self, new_value):
    if new_value is None:
      raise ValueError("No se permiten objetos vacios(None) en la lista")
    self.__value = new_value

  @next.setter
  def next(self, new_next):
    if new_next is not None and not isinstance(new_next, Node):
      raise TypeError("el parametro next solo se permite del objeto tipo Node ó None")
    self.__next = new_next

  def __str__(self):
    return str(self.__value)



class Linkedlist:

  __slots__ = ('__head', '__tail','__size')

  def __init__(self):
    self.__head = None
    self.__tail = None
    self.__size = 0

  @property
  def head(self):
    return self.__head

  @property
  def tail(self):
    return self.__tail

  @property
  def size(self):
    return self.__size

  def __iter__(self):
    current_node = self.__head
    while current_node is not None:
      yield current_node
      current_node = current_node.next

  def __str__(self):
    result = [str(node.value) for node in self]
    return ' --> '.join(result)

  def prepend(self,new_value):

    new_node = Node(new_value)
    if self.__head is None:
      self.__head = new_node
      self.__tail = new_node
    else:
      new_node.next = self.__head
      self.__head = new_node

    self.__size += 1


  def append(self,new_value):

    new_node = Node(new_value)
    if self.__head is None:
      self.__head = new_node
      self.__tail = new_node
    else:
      self.__tail.next = new_node
      self.__tail = new_node

    self.__size += 1


  def get_by_index(self, index):

    if index < -1 or index > self.__size - 1:
      raise ValueError("El indice esta por fuera de rango")

    if index == -1:
      return self.__tail

    cur_index = 0
    for current_node in self:
      if cur_index == index:
        return current_node
      cur_index += 1

    #sin utilizar el __iter__
    #current_node = self.__head
    #while current_node is not None:
    #  if cur_index == index:
    #    return current_node
    #  cur_index += 1
    #  current_node = current_node.next


  def insert_by_index(self, index, new_value):

    if index < -1 or index > self.__size - 1:
      raise ValueError("El indice esta por fuera de rango")

    if index == 0:
      self.prepend(new_value)
    elif index == -1 or index == self.__size:
      self.append(new_value)
    else:
      new_node = Node(new_value)
      prev_node = self.get_by_index(index-1)
      new_node.next = prev_node.next
      prev_node.next = new_node
      self.__size += 1


  def search_value(self, value):

    for node in self:
      if node.value == value:
        return True

    return False


  def set_new_value(self, value, new_value):

    for node in self:
      if node.value == value:
        node.value = new_value
        return True

    return False


  def popfirst(self):

    if self.__head is None:
      print("No hay elementos en la lista")
      return None
    elif self.__size == 1:
      popped_node = self.__head
      self.__head = None
      self.__tail = None
      self.__size = 0
      return popped_node
    else:
      print("Escenario de mas de 1 elemento")
      popped_node = self.__head
      self.__head = self.__head.next
      self.__size -= 1
      popped_node.next = None
      return popped_node

  def pop(self):

    if self.__head is None:
      print("No hay elementos en la lista")
      return None
    elif self.__size == 1:
      popped_node = self.__head
      self.__head = None
      self.__tail = None
      self.__size = 0
      return popped_node
    else:
      popped_node = self.__tail
      #obtener el penultimo
      #1ra forma new_tail = self.get_by_index(customll.size-2)

      #2da forma
      current_node = self.__head
      for _ in range(self.__size-2):
        current_node = current_node.next
      current_node.next = None
      self.__tail = current_node
      self.__size -= 1
      return popped_node


import random

class NodeD:
  __slots__ = ('__value','__next','__prev')

  def __init__(self,value):
    self.__value = value
    self.__next = None
    self.__prev = None

  def __str__(self):
    return str(self.__value)

  @property
  def next(self):
    return self.__next

  @next.setter
  def next(self,node):
    if node is not None and not isinstance(node,NodeD):
      raise TypeError("next debe ser un objeto tipo nodo ó None")
    self.__next = node

  @property
  def prev(self):
    return self.__prev

  @prev.setter
  def prev(self,node):
    if node is not None and not isinstance(node,NodeD):
      raise TypeError("prev debe ser un objeto tipo nodo ó None")
    self.__prev = node

  @property
  def value(self):
    return self.__value

  @value.setter
  def value(self,newValue):
    if newValue is None:
      raise TypeError("el nuevo valor debe ser diferente de None")
    self.__value = newValue


class DoublyLinkedList:

  def __init__(self):
    self.__head = None
    self.__tail = None
    self.__size = 0

  @property
  def head(self):
    return self.__head

  @property
  def tail(self):
    return self.__tail

  @property
  def size(self):
    return self.__size

  @head.setter
  def head(self,node):
    if node is not None and not isinstance(node,NodeD):
      raise TypeError("Head debe ser un objeto tipo nodo ó None")
    self.__head = node

  @tail.setter
  def tail(self,node):
    if node is not None and not isinstance(node,NodeD):
      raise TypeError("Tail debe ser un objeto tipo nodo ó None")
    self.__tail = node

  @size.setter
  def size(self,num):
    #if num is not isinstance(num,int):
    #  raise TypeError("Size debe ser un objeto tipo numerico")
    self.__size = num


  def __str__(self):
    result = [str(nodo.value) for nodo in self]
    return ' <--> '.join(result)

  def print(self):
    for nodo in self:
      print(str(nodo.value))

  def __iter__(self):
    current = self.__head
    while current is not None:
      yield current
      current = current.next

  def prepend(self, value): # Adicionar al principio

    newnode = NodeD(value)
    if self.__head is None:
      self.__head = newnode
      self.__tail = newnode
    else:
      newnode.next = self.__head #enlazo nuevo nodo
      self.__head.prev = newnode #Nueva linea para enlazar como previo el nodo nuevo
      self.__head = newnode
    self.__size += 1

  def append(self,value): # Adicionar al final
    newnode = NodeD(value)
    if self.__head is None:
      self.__head = newnode
      self.__tail = newnode
    else:
      self.__tail.next = newnode #enlazo nuevo nodo
      newnode.prev = self.__tail #asigno el previo del nuevo nodo
      self.__tail = newnode

    self.__size += 1

  def getbyindex(self, index):
    if index < 0 or index > self.__size:
      return "Error, indice fuera de rango"

    cont = 0
    for currentNode in self:
      if cont == index:
        return currentNode
      cont += 1

  def insertinindex(self, value, index):

    if index == 0:
      self.prepend(value)
    elif index == -1 or index == self.__size:
      self.append(value)
    else:
      prevNode = self.getbyindex(index-1)
      nextNode = prevNode.next
      newNode = NodeD(value)
      newNode.next = nextNode #Enlazo el next del nuevo nodo, que es el next del previo
      newNode.prev = prevNode # Enlazo el previo del nuevo nodo
      nextNode.prev = newNode # Enlazo el previo del next original
      prevNode.next = newNode
      self.__size +=1

  def searchbyvalue(self, valuetosearch):
    for currentNode in self:
      if currentNode.value == valuetosearch:
        return True

    return False

  def setnewvalue(self, valuetochange, newvalue):
    for currentNode in self:
      if currentNode.value == valuetochange:
        currentNode.value = newvalue
        return True

    return False

  def popfirst(self):
    tempNode = self.__head
    if self.__head is None:
      return "Lista vacia, no hay elementos a eliminar"
    elif self.__size == 1:
      self.__head = None
      self.__tail = None
      self.__size = 0
    else:
      self.__head = self.__head.next
      self.__head.prev = None
      self.__size -= 1

    tempNode.next = None  #limpiar la referencia al segundo nodo, ahora nueva cabeza
    return tempNode


  def pop(self):

    if self.__head is None:
      print("No hay elementos en la lista")
      return None
    elif self.__size == 1:
      popped_node = self.__head
      self.__head = None
      self.__tail = None
      self.__size = 0
      return popped_node
    else:
      popped_node = self.__tail
      prev_tail_node = self.__tail.prev

      self.__tail = prev_tail_node
      self.__tail.next = None
      self.__size -= 1
      popped_node.prev = None
      return popped_node


  def generate(self, num, min, max):
    for _ in range(num):
      self.append(random.randint(min,max))

# 1
def gestor_tren_escenario_1():
    tren = DoublyLinkedList()
    tren.append("V1")
    actual = tren.head

    nuevo = NodeD("V2")
    siguiente = actual.next
    nuevo.prev = actual
    nuevo.next = siguiente
    actual.next = nuevo
    if siguiente:
        siguiente.prev = nuevo
    else:
        tren.tail = nuevo
    tren.size += 1

    actual = actual.next

    nuevo = NodeD("V3")
    siguiente = actual.next
    nuevo.prev = actual
    nuevo.next = siguiente
    actual.next = nuevo
    if siguiente:
        siguiente.prev = nuevo
    else:
        tren.tail = nuevo
    tren.size += 1
    if actual.next:
        actual = actual.next
    if actual.prev:
        actual = actual.prev

    prev = actual.prev
    next_node = actual.next

    if prev is None and next_node is None:
        tren.head = None
        tren.tail = None
        actual = None
    else:
        if prev:
            prev.next = next_node
        else:
            tren.head = next_node
        if next_node:
            next_node.prev = prev
        else:
            tren.tail = prev
        if next_node:
            actual = next_node
        else:
            actual = prev
        tren.size -= 1
    print("Escenario 1: ",tren)

def gestor_tren_escenario_2():
    tren = DoublyLinkedList()
    tren.append("A")
    tren.append("B")
    tren.append("C")

    actual = tren.head.next
    nodo = actual

    if nodo.prev:
        nodo.prev.next = nodo.next
    if nodo.next:
        nodo.next.prev = nodo.prev
    else:
        tren.tail = nodo.prev
    nodo.prev = None
    nodo.next = tren.head
    tren.head.prev = nodo
    tren.head = nodo
    print("Escenario 2: ",tren)

print("\nPrimer punto:")
gestor_tren_escenario_1()
gestor_tren_escenario_2()

# 2
def fusionar_segmentos(lista):
    current = lista.head
    suma = 0
    nueva_head = None
    nueva_tail = None

    current = current.next
    while current:
        if current.value != 0:
            suma += current.value
        else:
            nuevo = Node(suma)
            if nueva_head is None:
                nueva_head = nuevo
                nueva_tail = nuevo
            else:
                nueva_tail.next = nuevo
                nueva_tail = nuevo
            suma = 0
        current = current.next
    lista._Linkedlist__head = nueva_head
    lista._Linkedlist__tail = nueva_tail

l1 = Linkedlist()
l1.append(0)
l1.append(3)
l1.append(1)
l1.append(0)
l1.append(4)
l1.append(5)
l1.append(2)
l1.append(0)

print("\nSegundo punto:")

fusionar_segmentos(l1)
print("Escenario 1: ",l1)

l2 = Linkedlist()
l2.append(0)
l2.append(10)
l2.append(0)

fusionar_segmentos(l2)
print("Escenario 2: ",l2)

# 3
def eliminar_duplicados(lista):
    actual = lista.head
    while actual:
        buscar = actual.next
        duplicado = False
        while buscar:
            if buscar.value == actual.value:
                duplicado = True
                break
            buscar = buscar.next
        siguiente = actual.next
        if duplicado:
            prev = actual.prev
            next_node = actual.next
            if prev:
                prev.next = next_node
            else:
                lista.head = next_node
            if next_node:
                next_node.prev = prev
            else:
                lista.tail = prev
            lista.size -= 1
        actual = siguiente

dll1 = DoublyLinkedList()
dll1.append(1)
dll1.append(2)
dll1.append(3)
dll1.append(2)
dll1.append(4)
dll1.append(3)

print("\nTercer punto:")

eliminar_duplicados(dll1)
print("Escenario 1: ",dll1)

dll2 = DoublyLinkedList()
dll2.append(5)
dll2.append(5)
dll2.append(5)

eliminar_duplicados(dll2)
print("Escenario 2: ",dll2)

# 4
def rotar(dll):
    actual = dll.head
    max_nodo = actual
    while actual:
        if actual.value > max_nodo.value:
            max_nodo = actual
        actual = actual.next
    while dll.head != max_nodo:
        ultimo = dll.tail
        nuevo_tail = ultimo.prev

        nuevo_tail.next = None
        dll.tail = nuevo_tail

        ultimo.prev = None
        ultimo.next = dll.head
        dll.head.prev = ultimo
        dll.head = ultimo

dll1 = DoublyLinkedList()
dll1.append(3)
dll1.append(1)
dll1.append(5)
dll1.append(2)

print("\nCuarto punto:")

rotar(dll1)
print("Escenario 1: ",dll1)

dll2 = DoublyLinkedList()
dll2.append(9)
dll2.append(2)
dll2.append(7)

rotar(dll2)
print("Escenario 2: ",dll2,"\n")