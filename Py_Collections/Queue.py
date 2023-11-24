class MyQueue:
    # конструктор, инициализирующий все необходимые поля необходимыми значениями
    def __init__(self):
        self.mas = [None] * 10
        self.head = 0
        self.tail = -1

    # метод добавления элемента в очередь
    def enqueue(self, x: object) -> bool:
        if self.tail == 9 and self.head == 0:
            return False
        
        elif self.tail == 9 and self.head != 0:
            self.tail = 0
            
        else:
            self.tail += 1
        
        self.mas[self.tail] = x
        
        return True

    # метод удаления элемента из очереди
    def dequeue(self) -> None:
        
        if self.isEmpty():
            return None
        
        retArg = self.mas[self.head]
        self.mas[self.head] = None
        
        if self.head == 9:
            self.head = 0
        else:
            self.head += 1
            
        return retArg

    # метод для определения, пуста ли очередь
    def isEmpty(self) -> bool:
        if self.tail == self.head-1 and self.mas[self.head] is None:
            return True
        
        return False

# Этот код менять не нужно. При корректной реализации класса MyQueue он должен выдать корректный результат
# Раскомментируйте этот код, когда перестанете получать сообщения об ошибках
if __name__ == "__main__":
    A = MyQueue()
    print(A.isEmpty())
    A.enqueue(1)
    A.enqueue(2)
    print(A.dequeue())
    A.enqueue(3)
    print(A.dequeue())
    A.enqueue(4)
    A.enqueue(5)
    print(A.isEmpty())
    A.enqueue(6)
    print(A.dequeue())
    print(A.dequeue())
    print(A.dequeue())
    print(A.dequeue())
    print(A.isEmpty())
    A.enqueue(10)
    A.enqueue(11)
    A.enqueue(12)
    A.enqueue(13)
    A.enqueue(14)
    A.enqueue(15)
    A.enqueue(16)
    print(A.dequeue())
    print(A.dequeue())
    print(A.dequeue())
    print(A.dequeue())
    print(A.dequeue())
    print(A.dequeue())
    print(A.dequeue())
