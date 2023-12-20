from django.db import models

# Create your models here.


class aboutme(models.Model):
    desc = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.desc}"
class servises(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.title}"

class servises1(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.title}"

class servises2(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.title}"

class servises3(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.title}"

class servises4(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.title}"

class servises5(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.title}"

class more(models.Model):
    num = models.CharField(max_length=100)
    desc = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.desc}"

class more1(models.Model):
    num = models.CharField(max_length=100)
    desc = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.desc}"

class more2(models.Model):
    num = models.CharField(max_length=100)
    desc = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.desc}"

class more3(models.Model):
    num = models.CharField(max_length=100)
    desc = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.desc}"

class Work_samples1(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title}"
class Work_samples(models.Model):
    title = models.CharField(max_length=100)
    img = models.ImageField()

    def __str__(self):
        return f"{self.title}"
class weblog(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.title}"
class ostads(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.title}"