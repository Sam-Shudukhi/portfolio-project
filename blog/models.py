from django.db import models

# Create your models here.
class Blog(models.Model):
# title
    title = models.CharField(max_length=100, unique=True)
# publicate date
    pub_date = models.DateTimeField()
# body
    body = models.TextField()
# image
    image = models.ImageField(upload_to='images/')

# func to view a summary of blog post body (1st 100 chars)
    def summary(self):
        return self.body[:100]

# show only date with no time
    def pub_date_only(self):
        return self.pub_date.strftime('%b %e, %Y')

# show titles in admin panel instead of blog objects
    def __str__(self):
        return self.title
