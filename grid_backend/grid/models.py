from django.db import models

class Card(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField()
    type = models.TextField(null=True, blank=True)
    frame_type = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    atk = models.IntegerField(null=True, blank=True)
    defense = models.IntegerField(null=True, blank=True, db_column='def')  # Map to 'def' column
    level = models.IntegerField(null=True, blank=True)
    race = models.TextField(null=True, blank=True)
    attribute = models.TextField(null=True, blank=True)
    archetype = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'yugioh_cards'
