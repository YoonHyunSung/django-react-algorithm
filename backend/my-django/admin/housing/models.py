from django.db import models

class Housing(models.Model):
    longitude = models.FloatField()
    latitude = models.FloatField()
    housing_median_age = models.FloatField()
    total_rooms = models.FloatField()
    tatal_bedrooms = models.FloatField()
    population = models.FloatField()
    households = models.FloatField()
    median_income = models.FloatField()
    median_house_value = models.FloatField()
    ocean_prximity = models.TextField()

    class Meta:
        db_table = "housings"

    def __str__(self):
        return f'[{self.pk}] {self.id}'