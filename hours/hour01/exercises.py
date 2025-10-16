# ========== ТЕОРИЯ ==========
# Урок 1: Введение в Python и среду
#
# Переменная — это как ящик, в который мы кладём информацию
# Синтаксис: имя_переменной: тип = значение
#
# Основные типы данных:
# 1. int - целые числа (14, 100, -5)
# 2. float - числа с запятой (1.75, 3.14)
# 3. str - текст ("Hello", "Python")
# 4. bool - истина/ложь (True, False)
#
# Пример: name: str = "Ivan"
#         age: int = 14
#         height: float = 1.75
#         active: bool = True


# ========== УПРАЖНЕНИЯ ==========

def exercise_01_hello_world() -> None:
    """
    Задача: Выведи на экран приветствие "Hello, World!"
    
    Результат:
    Hello, World!
    
    ПОДСКАЗКА: Используй функцию print()
    """
    pass


def exercise_02_create_variables() -> None:
    """
    Задача: Создай три переменные:
    - name: str = "Alex"
    - age: int = 14
    - height: float = 1.65
    Затем выведи каждую на новой строке.
    
    Результат:
    Alex
    14
    1.65
    
    ПОДСКАЗКА: Не забудь указать тип переменной с помощью :
    """
    pass


def exercise_03_integer_operations() -> None:
    """
    Задача: Создай переменные length: int = 5 и width: int = 3
    Вычисли площадь (length * width) и выведи результат.
    
    Результат:
    Area: 15
    
    ПОДСКАЗКА: Сначала умножь числа, потом выведи с текстом
    """
    pass


def exercise_04_string_concatenation() -> None:
    """
    Задача: Создай переменные:
    - language: str = "Python"
    - version: int = 14
    
    Выведи: "Programming language Python, version 14"
    
    Результат:
    Programming language Python, version 14
    
    ПОДСКАЗКА: Используй + для объединения текста, и str() для преобразования числа в текст
    """
    pass


def exercise_05_type_showcase() -> None:
    """
    Задача: Создай переменные всех четырёх типов данных:
    - text: str = "Hello"
    - number: int = 100
    - fraction: float = 3.14
    - flag: bool = True
    
    Выведи каждую переменную и её тип на новой строке, используя type().
    
    Результат:
    Hello
    <class 'str'>
    100
    <class 'int'>
    3.14
    <class 'float'>
    True
    <class 'bool'>
    
    ПОДСКАЗКА: Используй функцию type(переменная) для проверки типа переменной
    """
    pass
