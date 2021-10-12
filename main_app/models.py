from django.db import models

# Create your models here.

class Card(models.Model):
    CARD_TYPE = (
        ('land', 'Land'),
        ('creature', 'Creature'),
        ('enchantment', 'Enchantment'),
        ('artifact', 'Artifact'),
        ('instant', 'Instant'),
        ('sorcery', 'Sorcery')
    )
    
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=250)
    text = models.CharField(max_length=500)
    card_type = models.CharField(max_length=100, choices = CARD_TYPE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Deck(models.Model):
    title = models.CharField(max_length=150)
    cards = models.ManyToManyField(Card)

    def __str__(self):
        return self.title
