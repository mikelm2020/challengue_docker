from django.db import models
from apps.hits.managers import HitManager
from django.conf import settings

class Hits(models.Model):
 # STATUS
    ASSIGNED = 1
    FAILLED_ASSIGNED = 2
    COMPLETED = 3
    

    STATUS_CHOICES = [
        (ASSIGNED, "Assigned"),
        (FAILLED_ASSIGNED, "Failled assigned"),
        (COMPLETED, "Completed")
    ]

    assigne = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="assigned_to",
        on_delete=models.CASCADE
    )
    description = models.CharField("Description", max_length=50, blank=True, null=True)
    target_name = models.CharField("Target Name", max_length=50)
    status = models.PositiveIntegerField(choices=STATUS_CHOICES, default=1)
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="created_for",
        on_delete=models.CASCADE
    )

    objects = HitManager()

    class Meta:
        verbose_name = "Hit"
        verbose_name_plural = "Hits"
        

