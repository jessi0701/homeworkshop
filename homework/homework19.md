```python
1.
CSRF 공격(Cross Site Request Forgery)은 웹 어플리케이션 취약점 중 하나로 인터넷 사용자(희생자)가 자신의 의지와는 무관하게 공격자가 의도한 행위(수정, 삭제, 등록 등)를 특정 웹사이트에 요청하게 만드는 공격입니다.


```

```python
2.
title = request.POST.get("title")
```

```python
3.
<input type="text" name="title" value="{{post.title}}"/>
<input type="text" name="content" value="{{post.content}}"/>
```

