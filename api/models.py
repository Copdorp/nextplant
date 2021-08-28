from django.db import models
from django.contrib.auth.models import User


class Plant(models.Model):
    name = models.CharField(max_length=128)
    image = models.ImageField(default=None)
    pot = models.BooleanField(default=False)

    condition = models.CharField(
        max_length=3,
        choices=[('ok', 'Good'), ('reg', 'Regular'), ('bad', 'BAD'), ('aud', 'Audio'), ('ifr', 'iframe')],
    )

    def __str__(self):
        return str(self.name)


class Owner(models.Model):
    name = models.CharField(max_length=128, default=None)
    plants = models.ForeignKey(Plant, related_name="plant_name", on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    email = models.CharField(max_length=250, default=None)

    def __str__(self):
        return self.name


class Message(models.Model):
    user_from = models.ForeignKey(Owner, related_name="sender", on_delete=models.CASCADE)
    user_to = models.ForeignKey(Owner, related_name="receiver",  on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    date = models.DateField(default=None, blank=True, null=True)




