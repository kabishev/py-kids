import sys
from io import StringIO
from typing import Callable

from hours.hour01.exercises import (
    exercise_01_hello_world,
    exercise_02_create_variables,
    exercise_03_integer_operations,
    exercise_04_string_concatenation,
    exercise_05_type_showcase,
)


def capture_output(func: Callable[[], None]) -> str:
    """Захватывает вывод функции"""
    old_stdout: object = sys.stdout
    sys.stdout = StringIO()
    func()
    output: str = sys.stdout.getvalue()
    sys.stdout = old_stdout
    return output


def test_01_hello_world() -> None:
    """Проверяет что exercise_01 выводит приветствие"""
    output: str = capture_output(exercise_01_hello_world)
    assert "Hello, World!" in output, f"Ожидалось 'Hello, World!' в выводе, получено: {output}"


def test_02_create_variables() -> None:
    """Проверяет что exercise_02 создаёт три переменные и выводит их"""
    output: str = capture_output(exercise_02_create_variables)
    
    # Проверяем что все значения выведены
    assert "Alex" in output, f"Ожидалось 'Alex' в выводе"
    assert "14" in output, f"Ожидалось '14' в выводе"
    assert "1.65" in output, f"Ожидалось '1.65' в выводе"


def test_03_integer_operations() -> None:
    """Проверяет что exercise_03 вычисляет и выводит площадь"""
    output: str = capture_output(exercise_03_integer_operations)
    
    # Проверяем результат вычисления
    assert "Area" in output, f"Ожидалось 'Area' в выводе"
    assert "15" in output, f"Ожидалось '15' (результат умножения 5*3) в выводе"


def test_04_string_concatenation() -> None:
    """Проверяет что exercise_04 объединяет строки и числа корректно"""
    output: str = capture_output(exercise_04_string_concatenation)
    
    # Проверяем все компоненты результата
    assert "Programming language" in output, f"Ожидалось 'Programming language' в выводе"
    assert "Python" in output, f"Ожидалось 'Python' в выводе"
    assert "version" in output, f"Ожидалось 'version' в выводе"
    assert "14" in output, f"Ожидалось '14' в выводе"


def test_05_type_showcase() -> None:
    """Проверяет что exercise_05 выводит переменные всех четырёх типов и их типы"""
    output: str = capture_output(exercise_05_type_showcase)
    
    # Проверяем каждый тип данных
    assert "Hello" in output, f"Ожидалось 'Hello' (str) в выводе"
    assert "100" in output, f"Ожидалось '100' (int) в выводе"
    assert "3.14" in output, f"Ожидалось '3.14' (float) в выводе"
    assert "True" in output, f"Ожидалось 'True' (bool) в выводе"
    
    # Проверяем что используется type() - проверяем на наличие <class в выводе
    assert "<class" in output, f"Ожидалось использование type() в выводе"
    assert "'str'" in output, f"Ожидалось <class 'str'> в выводе"
    assert "'int'" in output, f"Ожидалось <class 'int'> в выводе"
    assert "'float'" in output, f"Ожидалось <class 'float'> в выводе"
    assert "'bool'" in output, f"Ожидалось <class 'bool'> в выводе"
