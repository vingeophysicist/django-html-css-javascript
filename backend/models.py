from django.db import models
from django.core.exceptions import ValidationError


class StringListMixin:
    def clean_list_field(self, field_name):
        field = getattr(self, field_name, None)
        if field:
            for item in field:
                if not isinstance(item, str):
                    raise ValidationError(f"All elements in '{field_name}' must be strings for {self.__class__.__name__}.")

    def save_list_field(self, field_name):
        field = getattr(self, field_name, None)
        if field:
            setattr(self, field_name, [str(item) for item in field])


class Survey(models.Model, StringListMixin):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    desc = models.TextField()
    nq = models.PositiveIntegerField()
    qs = models.JSONField(default=list)
    
    def clean(self):
        super().clean()
        self.clean_list_field('qs')

    def save(self, *args, **kwargs):
        self.save_list_field('qs')
        super().save(*args, **kwargs)
    
    
class Question(models.Model, StringListMixin):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=10, choices=[('rate', 'rate'), ('free', 'free')])
    title = models.CharField(max_length=255)
    description = models.TextField()
    options = models.JSONField(blank=True, default=list)
    
    def clean(self):
        super().clean()
        self.clean_list_field('options')
    
    def save(self, *args, **kwargs):
        self.save_list_field('options')
        super().save(*args, **kwargs)
