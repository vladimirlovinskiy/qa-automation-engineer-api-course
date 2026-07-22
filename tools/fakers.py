from faker import Faker


class Fake:
    """
    Класс для генерации тестовых данных через библиотеку Faker
    """

    def __init__(self, faker: Faker):
        """
        Args:
            faker (Faker): Экземпляр класса Faker, который будет использоваться для генерации данных.
        """
        self.faker = faker

    def text(self) -> str:
        """
        Генерирует случайный текст.

        Returns:
            str: Случайный текст.
        """
        return self.faker.text()

    def uuid4(self) -> str:
        """
        Генерирует случайный uuid 4 версии.

        Returns:
            str: Случаный uuid.
        """
        return self.faker.uuid4()

    def email(self) -> str:
        """
        Генерирует случайный email

        Returns:
            str: Случайный email.
        """
        return self.faker.email(domain="company.com")

    def sentence(self) -> str:
        """
        Генерирует случайное предложение.

        Returns:
            str: Случайное предложение.
        """
        return self.faker.sentence()

    def password(self) -> str:
        """
        Генерирует случайный пароль.

        Returns:
            str: Случайный пароль
        """
        return self.faker.password()

    def last_name(self) -> str:
        """
        Генерирует случайную фамилию.

        Returns:
            str: Случайная фамилия.
        """
        return self.faker.last_name()

    def first_name(self) -> str:
        """
        Генерирует случайное имя.

        Returns:
            str: Случайное имя.
        """
        return self.faker.first_name()

    def middle_name(self) -> str:
        """
        Генерирует случайное отчество.

        Returns:
            str: Случайное отчество.
        """
        return self.faker.first_name()

    def estimated_time(self) -> str:
        """
        Генерирует случайный срок обучения.

        Returns:
            str: Случайный срок обучания.
        """
        return f"{self.integer(1,10)} week"

    def integer(self, start: int = 1, end: int = 100) -> int:
        """
        Генерирует случайное число от start до end.

        Args:
            start (int, optional): Случайное число левой границы (включительно). Defaults to 1.
            end (int, optional): Случайное число правой границы (включительно). Defaults to 100.

        Returns:
            int: Случайное число
        """
        return self.faker.random_int(start, end)

    def max_score(self) -> int:
        """
        Генерирует максимальный бал для курса.

        Returns:
            int: Случайный бал.
        """
        return self.integer(50, 100)

    def min_score(self) -> int:
        """
        Генерирует минимальный бал для  курса.

        Returns:
            int: Случайный бал.
        """
        return self.integer(1, 30)


fake = Fake(faker=Faker("ru_RU"))
