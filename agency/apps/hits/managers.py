from django.db import models
from django.db.models import Q


class HitManager(models.Manager):
    def create_hit(self, assigne, description, target_name, status, creator):
        pass

    def hits_of_hitmen(self, hitman):
        return self.filter(Q(assigne=hitman) | Q(creator=hitman))
