class EmptyLinkedList(Exception):
    ...
    
class LastElementInArray(Exception):
    ...

class EmptyObjectInMethod(Exception):
    ...
    
class WrongIndex(Exception):
    ...
    
class Item:
    #class constructor
    def __init__(self, data:object = None, next:object = None, prev:object = None) -> None:
        self.data = data
        self.next = next
        self.prev = prev
        
    #Initializing all getters and setters
    def get_data(self) -> object:
        return self.data
    
    def set_data(self, data: object):
        self.data = data
        
    def get_next(self) -> object:
        return self.next
    
    def set_next(self, next: object):
        self.next = next
        
    def get_prev(self) -> object:
        return self.prev
    
    def set_prev(self, prev: object):
        self.prev = prev

    def remove(self) -> None:
        if self.next != None:
            self.next.set_prev(self.prev)
            self.prev.set_next(self.next)
        else:
            raise LastElementInArray
        
    def __str__(self):
        return str(self.data)

class MyList:
    def __init__(self):
        self.head = Item(None, None, None)
        self.tail = self.head

    def get_tail(self):
        return self.tail
    
    def get_head(self):
        return self.head

    # метод добавления элемента в конец списка
    def append(self, x: object) -> None:
        
        #Create a new Item obj
        itemToAppend = Item(x, None, None)
        itemToAppend.set_prev(self.tail)
        
        self.tail.set_next(itemToAppend)
        self.tail = itemToAppend

    # метод удаления элемента из конца списка (не забываем про пустой список!)
    def pop(self) -> object:
        #if list isEmpty then we raise Exception
        if self.head.get_next() == None:
            raise EmptyLinkedList
        
        #else we just copy data to return it and move our tail to prev location
        else:
            data = self.tail.get_data()
            prev = self.tail.get_prev()
            
            prev.set_next(None)
            self.tail = prev
            
            return data
        
    # метод добавления элемента в начало списка (помним про указатель tail!)
    def pushFirst(self, x: object) -> None:
        itemToAppend = Item(x, self.head.get_next(), self.head)
        
        if self.head.get_next() == None:
            self.tail = itemToAppend
        else:
            prevHeadNext = self.head.get_next()
            prevHeadNext.set_prev(itemToAppend)
        
        self.head.set_next(itemToAppend)
        
    # метод удаления элемента из начала списка (опять не забываем про пустой список!)
    def popFirst(self):
        if self.head.get_next() == None:
            raise EmptyLinkedList
        
        item = self.head.get_next()
        data = item.get_data()
        
        if item.get_next() != None:
            item.remove()
        else:
            self.tail = self.head
            self.head.set_next(None)
            
        return data

    # метод определения длины списка
    def __len__(self):
        cnt = 0
        item = self.head
        
        while item.get_next() != None:
            cnt += 1
            item = item.get_next()
            
        return cnt

    # метод конструирования строкового представления списка
    def __str__(self):
        retString = "["
        item = self.head.get_next()
        while item != None:
            retString += str(item.get_data())
            if item.get_next() != None:
                retString += ", "
            item = item.get_next()
            
        return retString + "]"

    # реализуйте метод, добавляющий новый элемент со значением x после p. Помните об указателе tail!
    def addAfter(self, p: object, x: object) -> None:
        if p is None:
            raise EmptyObjectInMethod
        
        next = p.get_next()
        newItem = Item(x, prev=p)
        p.set_next(newItem)
        
        if next is None:
            self.tail = newItem            
            
        else:
            next.set_prev(newItem)
            newItem.set_next(next)
            
    # реализуйте метод удаления элемента p. Также помните об указателе tail! Он не должен "съехать"
    def remove(self, p: object) -> None:
        if p is None or p == self.head:
            raise Exception
        
        deletion = p
        
        if deletion.get_next() != None:
            deletion.remove()
        else:
            deletion.get_prev().set_next(None)
            self.tail = deletion.get_prev()
            if self.head.get_next() is None:
                self.tail = self.head

    # реализуйте метод поиска элемента в списке
    def find(self, x: object) -> object:
        pointer = self.head.get_next()
        data = pointer.get_data()
        
        while data != x:
            if pointer is None:
                return None
            
            pointer = pointer.get_next()
            if pointer is None:
                return None
            
            data = pointer.get_data()
        
        return pointer

    # реализуйте перегрузку индексации на чтение
    def __getitem__(self, idx: int) -> object:
        lenList = len(self)
        if idx < 0 or idx >= lenList:
            raise WrongIndex
        
        pointer = self.head.get_next()
        index = 0
        
        while idx != index:
            pointer = pointer.get_next()
            index += 1
            
        return pointer.get_data()

    # реализуйте перегрузку индексации на запись
    def __setitem__(self, idx: int, x: object) -> object:
        lenList = len(self)
        if idx < 0 or idx >= lenList:
            raise WrongIndex
        
        pointer = self.head.get_next()
        index = 0
        
        while idx != index:
            pointer = pointer.get_next()
            index += 1
            
        pointer.set_data(x)
        
    # реализуйте перегрузку метода in (может можно воспользоваться уже реализованным find?)
    def __contains__(self, x: object) -> bool:
        for i in self:
            if x == i:
                return True
        return False

    # реализуйте сложение двух списков (попробуйте использовать уже написанные методы для упрощения кода)
    def __add__(self, secondList: object) -> object:
        
        newList = MyList()
        
        for i in self:
            newList.append(i)
            
        for i in secondList:
            newList.append(i)
        
        return newList

    # реализуйте метод конкатенации двух списков. Второй список не забудьте "обнулить"
    def concat(self, lst: object) -> None:
        self.tail.set_next(lst.get_head().get_next())
        lst.get_head().get_next().set_prev(self.tail)
        self.tail = lst.get_tail()
        lst.get_head().set_next(None)
        lst.tail = lst.get_head()

    def __iter__(self):
        return MyListIterator(self.head.get_next())


class MyListIterator:
    def __init__(self, item):
        self.currentItem = item

    def __next__(self):
        if self.currentItem is None:
            raise StopIteration
        
        data = self.currentItem.get_data()
        self.currentItem = self.currentItem.get_next()
        return data


if __name__ == "__main__":
    A = MyList()
    A.append(1)
    A.pushFirst(3)
    A.append(5)
    A.append(1)
    A.pushFirst(5)
    print(A)
    print(A.popFirst())
    print(A.pop())
    print(A)
    print(len(A))
    if (1 in A):
        print("True")
    else:
        print("False")
    if (2 in A):
        print("True")
    else:
        print("False")
    for i in range(6,10):
        A.append(i)
    A[0] = 0
    A[4] = -1
    for i in range(len(A)):
        print(A[i])
    for i in A:
        print(i)
    A.remove(A.find(-1))
    print(A)
    B = MyList()
    for i in range(6):
        B.append(i)
    A = A + B
    A.append(100)
    B[0] = 100
    print(A)
    print(B)
    A.concat(B)
    A.append(100)
    print(A)
    print(B)