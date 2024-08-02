from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='Sarlavha:')
    description = models.TextField(verbose_name='Tafsif:')
    image = models.ImageField(upload_to='blog/', verbose_name='Rasm:')  # new required

    def __str__(self):
        return self.title

    @property
    def get_image_url(self):
        if not self.image:
            url = ''
        else:
            url = self.image.url
        return url

    class Meta:
        ordering = ['title']

# terminal
# python manage.py makemigrations
# python manage.py migrate

# CREATE TABLE Blog (
# id integer AUTOINCREMENT NOT NULL,
# title TEXT,
# description TEXT
# PRIMARY KEY(id));
