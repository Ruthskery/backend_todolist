from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Todo(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)  # Links Todo to a User
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.description
