from django.db import models

class Book(models.Model):

    title = models.TextField()
    available = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Request(models.Model):

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    email = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email + ", " + str(self.book) + ", " + str(self.created_at)