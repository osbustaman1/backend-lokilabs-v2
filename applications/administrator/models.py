from django.db import models
from model_utils.models import TimeStampedModel

from remunerations.choices import YES_NO_OPTIONS

# Create your models here.

class HtmlMailTemplates(TimeStampedModel):

    ht_id = models.AutoField("Key", primary_key=True)
    ht_name = models.CharField("Nombre tipo correo", max_length=255)
    ht_subject = models.CharField("Subject", max_length=255, null=True, blank=True)
    ht_html = models.TextField("HTML", null=True, blank=True)
    ht_active = models.CharField(
        "Variable activa", choices=YES_NO_OPTIONS, max_length=1, default="Y")

    def __str__(self):
        return f"{self.ht_id} - {self.ht_name}"

    def save(self, *args, **kwargs):
        super(HtmlMailTemplates, self).save(*args, **kwargs)

    class Meta:
        db_table = "adm_HtmlMailTemplates"
        ordering = ['ht_id']