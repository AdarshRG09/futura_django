from django.db import models

# Create your models here.
class Construction(models.Model):
    construction_category = (
        ('house', 'house'),
        ('villa', 'villa'),
        ('flat', 'flat')
    )
    engineer_name = models.CharField(max_length=20)
    work_type = models.CharField(max_length=20,choices=construction_category)
    email = models.EmailField()
    due_date = models.DateField()
    fund_allocated = models.FloatField()

