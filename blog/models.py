from django.db import models

# Create your models here.
class post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20)
    heading1 = models.CharField(max_length=30)
    h1content = models.CharField(max_length=1000)
    heading2 = models.CharField(max_length=30)
    h2content = models.CharField(max_length=1000)
    Timestamp = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='shop/images', default='')
    
    def __str__(self):
        return self.title + '(' + str(self.post_id) + ')'
        