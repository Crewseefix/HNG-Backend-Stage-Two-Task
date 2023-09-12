from django.core.validators import RegexValidator
from django.db import models
from django_countries.fields import CountryField

class Person(models.Model):
    MALE = 'male'
    FEMALE = 'female'
    SEX_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]

    CHRISTIAN = 'christian'
    MUSLIM = 'muslim'
    OTHER = 'other'
    RELIGION_CHOICES = [
        (CHRISTIAN, 'Christian'),
        (MUSLIM, 'Muslim'),
        (OTHER, 'Other'),
    ]
    
    alpha_validator = RegexValidator(r'^[A-Za-z\s]+$', "Only alphabetic characters are allowed")

    name = models.CharField(max_length=255, unique=True, validators=[alpha_validator])
    sex = models.CharField(max_length=10, choices=SEX_CHOICES, null=True, validators=[alpha_validator])
    religion = models.CharField(max_length=10, choices=RELIGION_CHOICES, null=True, validators=[alpha_validator])
    country = CountryField(validators=[alpha_validator])

    def __str__(self):
        return self.name.title()
    
    def save(self, *args, **kwargs):
        if self.name:
            self.name = self.name.lower()
        if self.sex:
            self.sex = self.sex.lower()
        if self.religion:
            self.religion = self.religion.lower()
        super().save(*args, **kwargs)
