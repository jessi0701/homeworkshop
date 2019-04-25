# Workshop 30

```python
from dajngo.db import models

class Hashtag(models.Model):
    content = models.CharField(max_length=100)
    
class Post(models.Model):
    title = models.TextField()
    content = models.TextField()
    hashtags = models.ManyToManyField(Hashtag, blank=True)
```

