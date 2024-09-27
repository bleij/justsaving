from django.db import models
from django.conf import settings


class Task(models.Model):
    STATUS_CHOICES = [
        ('ns', 'Not Started!'),
        ('wip', 'Work In Progress'),
        ('done', 'Completed!'),
    ]

    PRIORITY_CHOICES = [
        ('0', 'Low'),
        ('1', 'Medium'),
        ('2', 'High'),
    ]

    CATEGORY_CHOICES = [
        ('personal', 'Personal'),
        ('work', 'Work'),
    ]

    title = models.CharField(max_length=128)
    description = models.CharField(max_length=1024)
    due_date = models.DateTimeField()
    status = models.CharField(max_length=32, choices=STATUS_CHOICES)
    priority = models.CharField(max_length=32, choices=PRIORITY_CHOICES)
    category = models.CharField(max_length=32, choices=CATEGORY_CHOICES)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='task')

    class Meta:
        app_label = "task"
        db_table = "task_item"
        verbose_name = "task_item"
        verbose_name_plural = "task_items"

    def __str__(self):
        return self.title
