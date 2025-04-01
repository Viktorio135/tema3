from django.db import models


class Breed(models.Model):
    """
    Модель для пород собак
    """

    SIZE_CHOICES = [
        ('Tiny', 'Крошечный'),
        ('Small', 'Маленький'),
        ('Medium', 'Средний'),
        ('Large', 'Крупный'),
    ]

    RATE_CHOICES = [(i, str(i)) for i in range(1, 6)]

    name = models.CharField(verbose_name='название', max_length=200)
    size = models.CharField(
        verbose_name='размер',
        max_length=10,
        choices=SIZE_CHOICES
    )
    friendliness = models.PositiveIntegerField(
        verbose_name='дружелюбность',
        choices=RATE_CHOICES
    )
    trainability = models.PositiveIntegerField(
        verbose_name='обучаемость',
        choices=RATE_CHOICES
    )
    shedding_amount = models.PositiveIntegerField(
        verbose_name='линька',
        choices=RATE_CHOICES
    )
    exercise_needs = models.PositiveIntegerField(
        verbose_name='физ. упражнения',
        choices=RATE_CHOICES
    )

    class Meta:
        verbose_name = 'Порода'
        verbose_name_plural = 'Породы'

    def __str__(self):
        return self.name


class Dog(models.Model):
    """
    Модель для собак
    """

    GENDER_CHOICES = [
        ('M', 'Мальчик'),
        ('F', 'Девочка'),
    ]

    name = models.CharField(verbose_name='имя', max_length=200)
    age = models.PositiveIntegerField(verbose_name='возраст')
    breed = models.ForeignKey(
        Breed,
        verbose_name='порода',
        on_delete=models.CASCADE,
        related_name='dogs'
    )
    gender = models.CharField(
        verbose_name='пол',
        max_length=1,
        choices=GENDER_CHOICES
    )
    color = models.CharField(verbose_name='цвет', max_length=100)
    favorite_food = models.CharField(
        verbose_name='любимая еда',
        max_length=200
    )
    favorite_toy = models.CharField(
        verbose_name='любимая игрушка',
        max_length=200
    )

    class Meta:
        verbose_name = 'Собака'
        verbose_name_plural = 'Собаки'

    def __str__(self):
        return self.name
