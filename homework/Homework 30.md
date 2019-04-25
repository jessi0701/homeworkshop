# Homework 30

```python
class Post(models.Model):
    content = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='like_post_set',blank=True)
```

