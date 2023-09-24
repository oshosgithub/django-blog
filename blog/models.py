from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    CATEGORY = (
        ('personal', 'personal'),
        ('daily life', 'daily life'),
        ('general', 'general'),
        ('others', 'others'),
        ('not applicable', 'not applicable'),
    )
    category = models.CharField(max_length=100, choices=CATEGORY)
    profile_pic = models.ImageField(null=True, blank=True, upload_to='images/', default='/profile_pic.jpeg')

    def __str__(self):
        return self.title[0:20]

    def title_preview(self):
        return self.title[0:40]

    def content_preview(self):
        return self.content[0:500]
    
