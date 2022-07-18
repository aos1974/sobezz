#
# stack.py
# ver.: 0.1
#

from typing import Any

# Классы и функции определяемые в модуле

class Stack(object):
    
    # список элементов - стек
    elements: list = []
    
    # инициализация класса
    def __init__(self) -> None:
        super().__init__()

    # проверка стека на пустоту. Метод возвращает True или False.
    def isEmpty(self) -> bool:
        return self.size() == 0

    # добавляет новые элементы на вершину стека (в порядке перечисления)
    def push(self, *args) -> None:
        for arg in args:
            self.elements.append(arg)
    
    # удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека или None
    def pop(self) -> Any:
        # если Стек пустой - возвращаем None
        if self.isEmpty:
            return None
        return self.elements.pop(self.size-1)
    
    # возвращает верхний элемент стека, но не удаляет его. Стек не меняется.
    def peek(self) -> Any:
        # если Стек пустой - возвращаем None
        if self.isEmpty:
            return None
        return self.elements[self.size-1]
    
    # возвращает количество элементов в стеке
    def size(self) -> int:
        return len(self.elements)
    
# end class Stack
