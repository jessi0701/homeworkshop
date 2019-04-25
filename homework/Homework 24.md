# Homework 24

1.

```python
from . import views

urlpatterns = [
    path('cbv/', views.CBView.as_view()),
]
```

2.

```python
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

```

