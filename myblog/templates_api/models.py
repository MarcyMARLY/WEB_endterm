from django.db import models

# Create your models here.
class Blog(models.Model):
    title  = models.CharField(max_length = 200)
    body = models.CharField(max_length = 200)
    created_at = models.CharField(max_length = 200)

    def to_json(self):
        return{
            'id': self.id,
            'title':self.title,
            'body':self.body,
            'created_at':self.created_at
        }
