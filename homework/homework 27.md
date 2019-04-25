# homework 27

1.

```python
from django.contrib.auth.decorators import login_required

@login_required
def create(request):
    if request.method == 'POST':
        board_form = BoardForm(request.POST)
```

2.

```python
from django.conf import settings

class Board(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
```

