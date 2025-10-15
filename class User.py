class User:
    def __init__(
            self,
            first_name: str | None = None,
            last_name: str | None = None,
            username: str | None = None,
    ):
        if not first_name and not last_name and not username:
            raise ValueError('Необходимо указать параметры пользователя')

        self.first_name = first_name
        self.last_name = last_name
        self.username = username

    @classmethod
    def with_name(cls, first_name, last_name):
        return User(first_name, last_name)

    @classmethod
    def with_username(cls, username):
        if not cls.is_username_allowed(username):
            raise ValueError('Некорректное имя пользователя')
        return User(username=username)

    @staticmethod
    def is_username_allowed(username: str):
        if username.startswith('admin'):
            return False
        else:
            return True

    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        elif self.username:
            return f'@{self.username}'


stas = User.with_name('Стас', 'Басов')
print(stas.full_name)
