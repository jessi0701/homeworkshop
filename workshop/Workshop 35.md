# Workshop 35

```python
from django.views.decorators.http import require_http_methods
@require_http_methods(["GET","POST"])

def create(reqeust):
    if request.method == 'POST':
        board_form = BoardForm(request.POST)
        if board_form.is_valid():
            board = board_form.save()
            return redirect(board)
    else:
        board_form = BoardForm()
    context = {} .....
    
 
```

```python
from django.views.decorators.http import require_POST
@require_POST

def ...
```

