from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.urls import reverse


class Position(models.Model):
    name = models.CharField(max_length=255, help_text="Название должности")
    salary = models.IntegerField(null=True, blank=False)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class FitnessUser(models.Model):
    SEX = (
        ("м", "Мужской"),
        ("ж", "Женский"),
        ("н", "Не указано"),
    )

    user = models.OneToOneField(User, on_delete=models.RESTRICT, default=None)
    full_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=1, choices=SEX, blank=True, default="н")
    phone_number = models.CharField(max_length=11, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ["full_name"]

    def __str__(self):
        return "Пользователь " + self.user.username


class Client(models.Model):
    fitness_user = models.OneToOneField(FitnessUser, on_delete=models.RESTRICT)
    has_subscription = models.BooleanField()

    class Meta:
        ordering = ["fitness_user__full_name"]

    def __str__(self):
        return "Клиент " + self.fitness_user.full_name


class Employee(models.Model):
    fitness_user = models.OneToOneField(FitnessUser, on_delete=models.RESTRICT)
    position = models.ForeignKey(Position, on_delete=models.RESTRICT)
    employment_history_book_id = models.CharField(max_length=7, null=True, blank=True)

    class Meta:
        ordering = ["position", "fitness_user__full_name"]

    def __str__(self):
        return f"{self.position} {self.fitness_user.full_name}"


class Trainer(models.Model):
    fitness_employee = models.OneToOneField(Employee, on_delete=models.RESTRICT)
    description = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return f"Тренер {self.fitness_employee.fitness_user.full_name}"

    def get_absolute_url(self):
        return reverse("trainer-detail", args=(str(self.id)))


class Program(models.Model):
    name = models.CharField(max_length=500, null=False, blank=False, unique=True)
    description = models.CharField(max_length=1000, null=True, blank=True)
    cost = models.IntegerField(null=True, blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"Программа {self.name}"

    def get_absolute_url(self):
        return reverse("program-detail", args=(str(self.id)))


class Workout(models.Model):
    workout_name = models.CharField(max_length=500, null=False, blank=False)
    workout_description = models.CharField(max_length=1000, null=True, blank=True)
    program = models.ForeignKey(Program, on_delete=models.RESTRICT)
    trainer = models.ForeignKey(Trainer, on_delete=models.SET_NULL, null=True, blank=True)
    workout_datetime = models.DateTimeField(null=True, blank=True)
    client = models.ManyToManyField(Client, blank=True)

    class Meta:
        ordering = ["workout_datetime", "program", "workout_name"]

    def __str__(self):
        return f"Занятие '{self.workout_name}'. Программа {self.program.name}"


def create_group_links(instance, created, **kwargs):
    if created and instance.position.name == 'Тренер':
        Trainer.objects.create(fitness_employee=instance, description='')


post_save.connect(create_group_links, sender=Employee)
