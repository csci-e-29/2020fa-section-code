from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=130)
    email = models.EmailField(blank=True)
    job_title = models.CharField(max_length=30, blank=True)
    bio = models.TextField(blank=True)


class HarvardID(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE, primary_key=True,)
    harvard_id = models.CharField(max_length=8)


class TeachingAssistants(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    state = models.CharField(max_length=2)
