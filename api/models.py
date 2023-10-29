from django.db import models


class Entity(models.Model):
    registration_number = models.CharField(max_length=255, null=True)
    registration_date = models.IntegerField(null=True)
    application_number = models.IntegerField(null=True)
    application_date = models.IntegerField(null=True)
    actual = models.BooleanField(null=True)
    publication_url = models.URLField(null=True)
    table = models.CharField(max_length=255)

    class Meta:
        get_latest_by = 'registration_date'

    def __str__(self):
        return '%s: %s' % (self.registration_number, self.table)
