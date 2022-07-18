#
# balance.py
# ver.: 0.1
#

from stack import Stack

# Глобальные переменные программы

BRACKETS = ['(', '[', '{', ')', ']', '}']
OPEN_BRACKETS = ['(', '[', '{']
CLOSE_BRACKETS = [')', ']', '}']
ROUND_BRACKETS = ['(', ')']
SQUARE_BRACKETS = ['[', ']']
FIGURE_BRACKETS = ['{', '}']

BALLANCED = "Сбалансированно"
NOT_BALLANCED = "Несбалансированно"

# Классы и функции определяемые в модуле

# проверяем что на вход передана скобка
def is_baracket(s: str) -> bool:
    if len(s) == 0:
        return False
    return s[0] in BRACKETS
# end is_bracket()

# открывающая скобка
def open_bracket(b : str) -> bool:
    return b[0] in OPEN_BRACKETS

# закрывающая скобка
def close_bracket(b : str) -> bool:
    return b[0] in CLOSE_BRACKETS

# проверка что скобки из одной пары
def same_brackets(openb : str, closeb : str) -> bool:
    if openb in ROUND_BRACKETS and closeb in ROUND_BRACKETS:
        return True
    elif openb in SQUARE_BRACKETS and closeb in SQUARE_BRACKETS:
        return True
    elif openb in FIGURE_BRACKETS and closeb in FIGURE_BRACKETS:
        return True
    else:
        return False

# Главная функция программы
def main():
    
    answer = NOT_BALLANCED
    
    stack = Stack()
    brackets = list(str(input("Введите последовательность скобок: ")).strip())
    
    if len(brackets) == 0:
        return answer
    
    for bracket in brackets:
        if is_baracket(bracket):
            if open_bracket(bracket):
                stack.push(bracket)
            else:
                if stack.isEmpty():
                    return answer
                if same_brackets(stack.peek(), bracket):
                    stack.pop()
                else:
                    return answer
    
    return answer
# end main()

# Основная программа

if __name__ == "__main__":
    print(main())
    
