class SupperMapping:
    """
    Этот класс реализует отображение, которое позволяет получать значения
    как по прямым, так и по обратным ключам. При создании экземпляра класса
    можно указать следующие параметры:

    * `mapping`: отображение, которое нужно использовать для инициализации
        экземпляра класса SupperMapping.
    * `default`: значение по умолчанию, которое будет возвращаться методом get,
        если указанный ключ не будет найден в отображении.
    * `default_reverse`: значение по умолчанию, которое будет возвращаться
        методом get, если указанный ключ не будет найден
        из обратного отображения.

    Методы класса SupperMapping:

    * `__contains__`: возвращает `True`, если указанный ключ присутствует
        в отображении или в обратном отображении, и `False` в противном случае.
    * `__getitem__`: возвращает значение по указанному ключу из отображения
        или из обратного отображения. Если ключ не найден,
        генерирует исключение `KeyError`.
    * `get`: возвращает значение по указанному ключу из отображения или
        из обратного отображения. Если ключ не найден, возвращает
        значение по умолчанию, указанное в параметрах
        `default` или `default_reverse`.
    * `_key_in_dict`: вспомогательный метод, который проверяет,
        присутствует ли указанный ключ в указанном словаре. Возвращает кортеж, содержащий ключ и логическое значение, указывающее, присутствует ли ключ в словаре.
    * `_convert_key_type`: статический метод, который преобразует тип указанного ключа к типу ключей указанного словаря. Если преобразование невозможно, генерирует исключение `ValueError`.
    * `_check_
    """

    def __init__(self, mapping, default=None, default_reverse=None):
        """
        Инициализирует экземпляр класса SupperMapping.
        :param mapping: отображение, которое нужно использовать для инициализации экземпляра класса SupperMapping.
        :param default: значение по умолчанию, которое будет возвращаться методом get, если указанный ключ не будет найден в отображении.
        :param default_reverse: значение по умолчанию, которое будет возвращаться методом get, если указанный ключ не будет найден в обратном отображении.
        """
        self._check_default_params(default, default_reverse)
        self.default = default
        self.default_reverse_key = default_reverse
        self._mapping = mapping
        self._reverse_mapping = {
            v: k for k, v in self._mapping.items()
        }

    def __contains__(self, key):
        """
        Возвращает True, если указанный ключ присутствует в отображении
        или в обратном отображении, и False в противном случае.

        :param key: ключ, который нужно проверить на присутствие в отображении.
        :return: логическое значение, указывающее,
            присутствует ли указанный ключ в отображении.
        """
        for target_dict in (self._mapping, self._reverse_mapping):
            _, in_dict = self._key_in_dict(key, target_dict)
            if in_dict:
                return True
        return False

    def __getitem__(self, key):
        """
        Возвращает значение по указанному ключу из отображения
        или из обратного отображения.
        Если ключ не найден, генерирует исключение KeyError.

        :param key: ключ, по которому нужно получить значение.
        :return: значение, соответствующее указанному ключу.
        """
        for target_dict in (self._mapping, self._reverse_mapping):
            key, in_dict = self._key_in_dict(key, target_dict)
            if in_dict:
                return target_dict[key]
        raise KeyError(key)

    def get(self, key, default=None, default_reverse_key=None):
        """
        Возвращает значение по указанному ключу из отображения
        или из обратного отображения.
        Если ключ не найден, возвращает значение по умолчанию,
        указанное в параметрах default или default_reverse.
        Если ни один из этих параметров не указан, возвращает None.
        :param key: ключ, по которому нужно получить значение.
        :param default: значение по умолчанию, которое будет возвращаться,
            если указанный ключ не будет найден в отображении.
        :param default_reverse_key: ключ по умолчанию для поиска значения из
            отображения которое будет возвращаться,
            если указанный ключ не будет найден в отображении.
        :return: значение, соответствующее указанному ключу,
            или значение по умолчанию.
        """
        try:
            return self[key]
        except KeyError:
            pass
        self._check_default_params(default, default_reverse_key)

        if default_reverse_key:
            return self.get(default_reverse_key)
        if default:
            return default
        if self.default_reverse_key:
            return self.get(default_reverse_key)
        return self.default

    def _key_in_dict(self, key, target_dict):
        """
        Проверяет, присутствует ли указанный ключ в указанном словаре.

        :param key: ключ, который нужно проверить на присутствие в словаре.
        :param target_dict: словарь, в котором нужно проверить
            наличие указанного ключа.
        :return: кортеж, содержащий ключ и логическое значение,
            указывающее, присутствует ли ключ в словаре.
        """
        try:
            key = self._convert_key_type(key, target_dict)
        except ValueError:
            return key, False
        return key, True

    @staticmethod
    def _convert_key_type(key, target_dict):
        """
        Преобразует тип указанного ключа к типу ключей указанного словаря.
        Если преобразование невозможно, генерирует исключение ValueError.
        :param key: ключ, тип которого нужно преобразовать.
        :param target_dict: словарь, ключи которого используются
            для определения типа, к которому нужно преобразовать
            указанный ключ.
        :return: преобразованный ключ.
        """
        mapping_key_type = type(next(iter(target_dict.keys())))
        if not isinstance(key, mapping_key_type):
            try:
                key = mapping_key_type(key)
            except Exception as err:
                raise ValueError(f"Invalid key type: {err}")
        return key

    @staticmethod
    def _check_default_params(*args):
        """
        Проверяет, были ли указаны оба параметра default и default_reverse.
        Если оба параметра указаны, генерирует исключение ValueError.
        :param args: список параметров, которые нужно проверить
            на наличие вместе
        :return: None
        """
        if any(args):
            raise ValueError(
                "Cannot specify both "
                "default and default_reverse "
                "arguments together"
            )
