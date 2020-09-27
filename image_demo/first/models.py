from django.db import models


class Book(models.Model):
    title = models.CharField(max_length = 32, blank = False)
    cover = models.ImageField(blank = True, null = True)
