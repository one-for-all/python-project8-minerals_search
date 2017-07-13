from django.db import models
from django.db.models import CharField
from django.contrib.staticfiles import finders
import json


class Mineral(models.Model):
    name = CharField('name', max_length=255, unique=True)
    image_filename = CharField('image file', max_length=255, blank=True)
    image_caption = CharField('image caption', max_length=255, blank=True)
    category = CharField('category', max_length=255, blank=True)
    formula = CharField('formula', max_length=255, blank=True)
    strunz_classification = CharField('strunz classification',
                                      max_length=255, blank=True)
    crystal_system = CharField('crystal system', max_length=255, blank=True)
    unit_cell = CharField('unit cell', max_length=255, blank=True)
    color = CharField('color', max_length=255, blank=True)
    crystal_symmetry = CharField('crystal symmetry', max_length=255,
                                 blank=True)
    cleavage = CharField('cleavage', max_length=255, blank=True)
    mohs_scale_hardness = CharField('mohs scale hardness', max_length=255,
                                    blank=True)
    luster = CharField('luster', max_length=255, blank=True)
    streak = CharField('streak', max_length=255, blank=True)
    diaphaneity = CharField('diaphaneity', max_length=255, blank=True)
    optical_properties = CharField('optical properties', max_length=255,
                                   blank=True)
    refractive_index = CharField('refractive index', max_length=255,
                                 blank=True)
    crystal_habit = CharField('crystal habit', max_length=255, blank=True)
    specific_gravity = CharField('specific gravity', max_length=255,
                                 blank=True)
    group = CharField('group', max_length=255, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


def initialize():
    with open(finders.find('minerals/data/minerals.json')) as jsonFile:
        minerals = json.load(jsonFile)
        for mineral in minerals:
            mineral = {'_'.join(key.split()): val for key, val in
                       mineral.items()}
            Mineral.objects.update_or_create(**mineral)
