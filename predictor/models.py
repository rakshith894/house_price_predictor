from django.db import models

class Prediction(models.Model):
    area = models.FloatField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    age = models.IntegerField()
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prediction: {self.price}"
