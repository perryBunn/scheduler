from datetime import datetime
from django.db import models

from .validators import validate_no_space


class Floor(models.Model):
    """Describes the shift requirements for a certain unit.
    """
    name: str = models.CharField(max_length=30)
    short_name: str = models.CharField(max_length=5, default=str(name)[:2],
                                       validators=[validate_no_space])
    beds: int = models.IntegerField()
    imc_beds: int = models.IntegerField()
    required_charge: int = models.IntegerField(default=1)
    required_nurses: int = models.IntegerField()
    required_techs: int = models.IntegerField()
    nurse_ratio: int = models.IntegerField()
    imc_ratio: int = models.IntegerField()
    tech_ratio: int = models.IntegerField()
    schedule_start: datetime = models.DateField(default=datetime.today())
    schedule_length: int = models.IntegerField(default=6)
    work_periods: list = None

    def __str__(self):
        return self.name

    def make_period(self):
        self.work_periods = []
        period =
        self.work_periods.append(period)



class Holiday(models.Model):
    """Represents the holiday that a person might have off.
    """
    name: str = models.CharField(max_length=30)
    date: datetime = models.DateField()
    worker_off: bool = models.BooleanField()

    def __str__(self):
        return self.name


class Person(models.Model):
    """Information necessary to describe the persons work time.
    """
    NURSE_ABREVIATION = "NU"
    TECH_ABREVIATION = "TE"
    WORKER_OPTIONS = [
        (NURSE_ABREVIATION, "Nurse"),
        (TECH_ABREVIATION, "Technician")
    ]
    DAY = "Day"
    NIGHT = "Night"
    HYBRID = "Hybrid"
    SHIFT_OPTIONS = [
        (DAY, DAY),
        (NIGHT, NIGHT),
        (HYBRID, HYBRID)
    ]

    worker: str = models.CharField(choices=WORKER_OPTIONS, max_length=30)
    first_name: str = models.CharField(max_length=30)
    last_name: str = models.CharField(max_length=30)
    shift: str = models.CharField(choices=SHIFT_OPTIONS, max_length=30)
    holidays: dict = models.ManyToManyField(Holiday)
    hours: int = models.IntegerField()
    shift_length: int = models.IntegerField()

    def __str__(self):
        return str(abs(hash((self.first_name, self.last_name))))

