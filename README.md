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
# Проверка наличия ключа в словаре
assert 1 in supper_mapping
assert 'one' in supper_mapping
assert 4 not in supper_mapping
assert 'four' not in supper_mapping

# Получение значения по ключу
assert supper_mapping[1] == 'one'
assert supper_mapping['two'] == 2
assert supper_mapping.get('2') == 'two'

# Получение ключа по значению
assert supper_mapping.reverse_get('one') == 1
assert supper_mapping.reverse_get(2) == 'two'

# Получение значения по умолчанию, если ключ не найден
assert supper_mapping.get(4, 'default') == 'default'
assert supper_mapping.get('four', 'default_reverse') == 'default_reverse'

# Получение ключа по умолчанию, если значение не найдено
assert supper_mapping.reverse_get(4, 'default') == 'default'
assert supper_mapping.reverse_get('four', 'default_reverse') == 'default_reverse'
```
