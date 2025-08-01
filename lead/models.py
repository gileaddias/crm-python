from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Lead(models.Model):

    LOW = 'low'
    MEDIUM = 'medium'
    HIGH = 'high'

    CHOICES_PRIORITY = (

        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'high'),
    )

    NEW = 'new'
    CONTACTED = 'contacted'
    WON = 'won'
    LOST = 'lost'

    CHOICES_STATUS = (
    
    (NEW, 'new'),
    (CONTACTED, 'contacted'),
    (WON, 'won'),
    (LOST, 'lost'),

    )

    name = models.CharField(max_length=255)
    email = models.EmailField()
    description = models.TextField(blank=True, null=True)
    priority = models.CharField(max_length=10, choices= CHOICES_PRIORITY, default=MEDIUM)
    status = models.CharField(max_length=10, choices= CHOICES_STATUS, default=NEW)
    creaty_by = models.ForeignKey(User, related_name='leads', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)



    #TimeLine

    def __str__(self):
        return self.name