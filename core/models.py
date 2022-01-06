from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Person(models.Model):
    last_name = models.TextField()
    first_name = models.TextField()
    courses = models.ManyToManyField("Course", blank=True)

    class Meta:
        verbose_name_plural = "People"

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Course(models.Model):
    name = models.TextField()
    year = models.IntegerField()

    class Meta:
        unique_together = ("name", "year", )

    def __str__(self):
        return self.name + ' (' + str(self.year) + ')'


class Grade(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    grade = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)])
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.person) + ' ' + str(self.course)
