from django.db import models


class Resource(models.Model):
    """
    Личная карточка сотрудника.
    """

    TRAINEE = 1
    PROBATION = 2
    JUNIOR = 3
    MIDDLE_MINUS = 4
    MIDDLE = 5
    MIDDLE_PLUS = 6
    SENIOR = 7

    GRADES = (
        (TRAINEE, "trainee"),
        (PROBATION, "probation"),
        (JUNIOR, "junior"),
        (MIDDLE_MINUS, "middle-"),
        (MIDDLE, "middle"),
        (MIDDLE_PLUS, "middle+"),
        (SENIOR, "senior"),
    )

    grade = models.PositiveIntegerField(choices=GRADES, null=True)
    name = models.CharField(max_length=100, null=False)
    position = models.CharField(max_length=100, null=True, blank=True)
    daily_hours = models.PositiveIntegerField(null=False)
    hire_date = models.DateField(null=False)
    dismiss_date = models.DateField(null=True, blank=True, default=None)
