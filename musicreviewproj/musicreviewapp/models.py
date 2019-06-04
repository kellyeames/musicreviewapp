from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class GenreType(models.Model):
    typename=models.CharField(max_length=255)
    typedescription=models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.typename
    
    class Meta:
        db_table='genretype'
        verbose_name_plural='genretypes'

class Album(models.Model):
    albumname=models.CharField(max_length=255)
    albumgenretype=models.ForeignKey(GenreType, on_delete=models.DO_NOTHING)
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    albumbandname=models.CharField(max_length=255)
    albumreview=models.CharField(max_length=255)
    albumreviewentrydate=models.DateField()
    albumurl=models.URLField(null=True, blank=True)

    def __str__(self):
        return self.albumname

    class Meta:
        db_table='album'
        verbose_name_plural='albums'

class Review(models.Model):
    reviewtitle=models.CharField(max_length=255)
    reviewdate=models.DateField()
    album=models.ForeignKey(Album, on_delete=models.CASCADE)
    user=models.ManyToManyField(User)
    reviewrating=models.SmallIntegerField()
    reviewtext=models.TextField()

    def __str__(self):
        return self.reviewtitle
    
    class Meta:
        db_table='review'
        verbose_name_plural='reviews'
