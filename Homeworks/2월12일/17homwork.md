# Python 활용 SQL

```
학습해야 할 내용
- Model
```

1. Django에서 선언한 Model을 실제 DB에 반영하는 과정을 무엇이라고 하는가?

`migrate`

2. 모델의 필드를 정의할 때 CharField는 필수로 들어가야하는 인자가 존재한다. 무엇인가?

`max_length=정수`

3. Django에서 동작하는 모든 명령을 대화식 Python 쉘에서 시험할 수 있는 명령어를 작성하세요.

```shell
> python manage.py shell
```

4. Post라는 이름의 모델은 CharField로 정해진 title과 CharField로 정해진 content가 필드로 정의 되어있다. 제목은 자신의 이름, 내용은 자신의 이메일 정보가 들어간 Post를 만드는 코드를 작성하세요.

> models.py

```python
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=100)
```

> workspace

```shell
> python manage.py makemigrations
> python manage.py shell
>>> from .models import Post
>>> me = Post(title="한동훈",content="pok_winter@naver.com")
>>> me.save()
>>> me.object.get(pk=1).title
'한동훈'
>>> me.object.get(pk=1).content
'pok_winter@naver.com'
```