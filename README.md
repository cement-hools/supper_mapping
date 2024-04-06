# SupperMapping
SupperMapping - это класс Python, который предоставляет удобный интерфейс для работы со словарями с возможностью обратного отображения.

## Использование
Чтобы создать экземпляр класса SupperMapping, передайте в его конструктор словарь:

```python
mapping = {
    1: 'one',
    2: 'two',
    3: 'three'
}

supper_mapping = SupperMapping(mapping)
```
SupperMapping поддерживает следующие методы:

- __contains__ - проверяет, содержится ли ключ в словаре или в обратном отображении.
- __getitem__ - возвращает значение по ключу из словаря или обратного отображения.
- __get__ - возвращает значение по ключу из словаря или обратного отображения, либо значение по умолчанию, если ключ не найден.

## Примеры использования

```python
mapping_dict = {
            1: 'one',
            2: 'two',
            3: 'three'
        }

digit_mapping = SupperMapping(mapping_dict)

# Проверка наличия ключа
assert 1 in digit_mapping
assert 'one' in digit_mapping
assert 4 not in digit_mapping
assert 'four' not in digit_mapping

# Получение значения по ключу
assert digit_mapping[1] == 'one'
assert digit_mapping['two'] == 2
assert digit_mapping['2'] == 'two'
assert digit_mapping.get('2') == 'two'
assert digit_mapping.get(4) == None

# Получение значения по умолчанию, если ключ не найден
assert digit_mapping.get(4, 'five') == 'five'
assert digit_mapping.get('four', 2) == 2
assert digit_mapping.get('four', default_key=2) == 'two'
```
