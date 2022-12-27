from datetime import datetime
from django.db import models
from django.urls import reverse

from calendarapp.models import EventAbstract
from accounts.models import User
from training_site_api.models import TrainingTask

class EventManager(models.Manager):
    """ Event manager """

    def get_all_events(self, user):
        events = Event.objects.filter(user=user, is_active=True, is_deleted=False)
        return events

    def get_running_events(self, user):
        running_events = Event.objects.filter(
            user=user,
            is_active=True,
            is_deleted=False,
            end_time__gte=datetime.now().date(),
        ).order_by("start_time")
        return running_events
    


class Event(EventAbstract):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="events")
    title = models.CharField("Название тренировки", max_length=200, unique=True)
    description = models.TextField("Описание тренировки", blank=True)
    start_time = models.DateTimeField("Время начала")
    end_time = models.DateTimeField("Время окончания")
    tasks = models.ManyToManyField(TrainingTask, verbose_name="Упражнения")

    objects = EventManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("calendarapp:event-detail", args=(self.id,))

    @property
    def get_html_url(self):
        url = reverse("calendarapp:event-detail", args=(self.id,))
        return f'<a href="{url}"> {self.name} </a>'
    
    @property
    def get_training_reps(self):
        return self.tasks.count()
    
    @property
    def get_summary_weight(self):
        summ = 0
        for task in self.tasks:
            summ += (task.get_weigth * task.get_reps_quantity)
        return summ

    @property
    def get_summ_distance(self):
        sum = 0
        for task in self.tasks:
            summ += (task.get_distance * task.get_reps_quantity)
        return summ

    @property
    def get_max_weight(self):
        max = 0
        for task in self.tasks:
            if max < task.get_weigth:
                max = task.get_weigth 
        return max

    class Meta:
        verbose_name = "Тренировка"
        verbose_name_plural = "Тренировки"
    """ 

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="events")
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    objects = EventManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("calendarapp:event-detail", args=(self.id,))

    @property
    def get_html_url(self):
        url = reverse("calendarapp:event-detail", args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'
    
    """
