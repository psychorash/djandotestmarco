from django.db import models

# Create your models here.
class SocialNetWork(models.Model):

    def image_path(self, filename):
       ruta ="SocialNetwork/%s/%s" % (self.settings_name, str(filename))
       return ruta

    name = models.CharField(max_length=300)
    url = models.URLField(max_length=700)
    icon = models.ImageField(upload_to=image_path)
    status = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Red Social"
        verbose_name_plural = "Redes Sociales"