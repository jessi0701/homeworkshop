# Workshop 31

```python
from django.core.validators import EmailValidator, MinvalueValidator


validators=[EmailValidator(message="이메일이아닙니다.")]
validators=[MinValueValidator(20, message="미성년자는 노노")]
```

