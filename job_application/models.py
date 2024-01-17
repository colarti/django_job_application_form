from django.db import models

class Form(models.Model):
    fname = models.CharField(max_length=80)
    lname = models.CharField(max_length=80)
    email = models.EmailField()
    date = models.DateField()
    occupation = models.CharField(max_length=80)

    def __str__(self):
        return f'{self.fname} {self.lname} - {self.email} <> {self.date} [{self.occupation}]'