from django.db import models
from django.utils import timezone
class Problem(models.Model):
    Author          = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    Title           = models.CharField(max_length=35)
    description     = models.TextField()
    date_posted     = models.DateField(default=timezone.now)
    Organisation    = models.CharField(max_length=25)
    Location        = models.CharField(max_length=25)
    upvotes         = models.IntegerField(default=0)
    def __str__(self):
        return self.Title
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("select")

