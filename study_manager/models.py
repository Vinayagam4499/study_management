from django.db import models


class Study(models.Model):
    PHASE_CHOICES = [
        ('Phase I', 'Phase I'),
        ('Phase II', 'Phase II'),
        ('Phase III', 'Phase III'),
        ('Phase IV', 'Phase IV'),
    ]

    study_name = models.CharField(max_length=200)
    study_phase = models.CharField(max_length=50, choices=PHASE_CHOICES)
    sponsor_name = models.CharField(max_length=200)
    study_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.study_name

    class Meta:
        db_table = 'study'
        verbose_name_plural = 'Studies'