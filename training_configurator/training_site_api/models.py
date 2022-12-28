from django.db import models
#from datetime import datetime
#from django.contrib.auth.models import User
#from django.urls import reverse
from accounts.models import User


class UserSettings(models.Model):
    """Настройки шага измерений упражнения"""
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    """Шаги к тренировкам"""
    weigth_step = models.PositiveSmallIntegerField("Шаг веса", default=5,)
    repeat_step = models.PositiveSmallIntegerField("Повторы", default=2, )
    cardio_duration_step = models.PositiveSmallIntegerField("Шаг длительности", default=60,)

    """Шаги к паузам"""
    sets_pause = models.PositiveSmallIntegerField("Отдых между подходами", default=90)
    repeat_pause = models.PositiveSmallIntegerField("Отдых между упражнениями", default=150)
    rest_duration_step = models.PositiveSmallIntegerField("Шаг длительности", default=1)

    @property
    def get_weigth_step(self):
        return self.weigth_step

    @property
    def get_repeat_step(self):
        return self.repeat_step
        
    @property
    def get_cardio_duration_step(self):
        return self.cardio_duration_step
    
    @property
    def get_sets_pause(self):
        return self.sets_pause
    
    @property
    def get_repeat_pause(self):
        return self.repeat_pause
        
    @property
    def get_rest_duration_step(self):
        return self.rest_duration_step

    class Meta:
        verbose_name = "Настройки шага измерений упражнения"
        verbose_name_plural = "Настройки шагов измерений упражнений"


class Person(models.Model):
    """Пользователь"""
    vorname = models.CharField("Имя", max_length=50, null=True)
    lastname = models.CharField("Фамилия", max_length=50, null=True)
    user_weigth = models.PositiveSmallIntegerField("Вес", default=70)
    user_heigth = models.PositiveSmallIntegerField("Рост", default=175)
    profile_image = models.ImageField("Картинка профиля", blank=True, null=True)
    user = models.OneToOneField(User, null=True, on_delete=models.SET_NULL)
    user_settings = models.OneToOneField(UserSettings, null=True, on_delete=models.SET_NULL)

    #user_measurements = models.OneToOneField(UserMeasurements, on_delete=models.CASCADE)
    #imt = models.FloatField("Индекс массы тела", blank=True)
    #birthdate = models.DateField("День рождения", auto_now=False, auto_now_add=False)

    def __str__(self):
        return str(self.vorname + " "+ self.lastname)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class UserMeasurements(models.Model):
    """Измерения параметров пользователя"""
    
    name = models.CharField("Параметр измерений", max_length=200, default="")
    mesurement_date = models.DateField("Дата измерения", auto_now=True, )
    length = models.PositiveSmallIntegerField("Длина (см)", default=0,)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Измерение параметра пользователя"
        verbose_name_plural = "Измерения параметров пользователя"


class TrainingTask(models.Model):
    """Упражнение"""
    TYPE_CHOICES = (
        ('STRENGHT','Силовые'),
        ('CARDIO','Кардио'),
    )
    MUSCLEGROUP_CHOICES = (
        ('BICEPS','Бицепс'),
        ('CHEST','Грудь'),
        ('LEGS','Ноги'),
        ('SHOULDERS','Плечи'),
        ('ABS','Пресс'),
        ('HANDS','Руки'),
        ('BACK','Спина'),
        ('TRICEPS','Трицепс'),
        ('NECK','Шея'),
    )
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    name = models.CharField("Название упражнения", max_length=200)
    task_type = models.CharField(max_length=9,
                           choices=TYPE_CHOICES,
                           default='STRENGHT',
                           verbose_name="Тип упражнения"
                           )
    musclegroup_type = models.CharField(max_length=10,
                           choices=MUSCLEGROUP_CHOICES,
                           default='BICEPS',
                           verbose_name="Группа мышц"
                           )            
    description = models.TextField("Описание упражнения")
    duration = models.TimeField("Длительность(мин.)", default="00:01:00")
    distance = models.PositiveSmallIntegerField("Дистанция", blank=True, null=True)
    weigth = models.PositiveSmallIntegerField("Поднимаемый вес", blank=True, null=True, default=0)
    reps_quantity = models.PositiveSmallIntegerField("Количество повторений", blank=True, default=1)
    task_settings = models.ForeignKey(UserSettings, null=True, on_delete=models.PROTECT)

    #parent = models.ForeignKey('self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True, related_name="children")
    #distance = models.PositiveSmallIntegerField("Дистанция", blank=True, null=True)
    #avg_speed = models.PositiveSmallIntegerField("Средняя скорость (м/с)", blank=True, null=True)
    #max_speed = models.PositiveSmallIntegerField("Максимальная скорость (м/с)", blank=True, null=True)

    def __str__(self):
        return self.name

    """def get_absolute_url(self):
        return reverse('trainingtask-detail', kwargs={'pk' : self.pk})"""
    
    """def get_kkal(self):
        return self.kkal_quantity"""

    @property
    def get_task_type(self):
        return self.task_type

    @property
    def get_task_musclegroup(self):
        return self.musclegroup_type
    
    @property
    def get_reps_quantity(self):
        return self.musclegroup_type

    @property
    def get_distance(self):
        return self.distance

    @property
    def get_weigth(self):
        return self.weigth

    class Meta:
        ordering = ['name']
        verbose_name = "Упражнение"
        verbose_name_plural = "Упражнения"


'''class Day(models.Model):
    """День"""

    """def get_daily_kkal(self):
        for training in self.trainings:
            self.kkal_quantity += training.get_kkal()
        return self.kkal_quantity"""
        
    def __str__(self):
        return str(self.date)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    date = models.DateField("Дата", auto_now=False, auto_now_add=False)
    max_temperature = models.SmallIntegerField("Максимальная температура дня", blank=True, default=0)
    min_temperature = models.SmallIntegerField("Минимальная температура дня", blank=True, default=0)
    min_temperature = models.PositiveSmallIntegerField("Влажность воздуха", blank=True, default=0)
    wind_speed = models.PositiveSmallIntegerField("Скорость ветра (м/с)", blank=True, default=0)

    #weeks_day = models.CharField("День недели", max_length=20)
    #kkal_quantity = models.PositiveSmallIntegerField("Килокалории за день", default=0)
    #duration = models.ForeignKey(Training.duration, on_delete=models.CASCADE,verbose_name="Длительность тренировки")
    #trainings = models.ManyToManyField(TrainingTask, verbose_name="Тренировки", blank=True, )

    class Meta:
        verbose_name = "День недели"
        verbose_name_plural = "Дни недели"'''


'''class Training(models.Model):
    """Тренировка"""
    """def get_kkal(self):
        for task in self.tasks:
            self.kkal_quantity += task.get_kkal()
        return self.kkal_quantity"""

    def __str__(self):
        return self.name

    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    name = models.CharField("Название тренировки", max_length=200)
    training_date = models.ManyToManyField(Day, verbose_name="Дата", blank=True,)
    tasks = models.ManyToManyField(TrainingTask, verbose_name="Упражнения")

    #kkal_quantity = models.PositiveSmallIntegerField("Килокалории", default=0)
    #description = models.TextField("Описание тренировки")
    #begin_time = models.TimeField("Начало тренировки", blank=True)

    class Meta:
        ordering = ['name']
        verbose_name = "Тренировка"
        verbose_name_plural = "Тренировки"'''