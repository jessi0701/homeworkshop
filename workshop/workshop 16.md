```sqlite
1.
ALTER TABLE bands ADD members INTEGER
UPDATE bands SET members=4 WHERE id=1;
UPDATE bands SET members=5 WHERE id=2;
UPDATE bands SET members=9 WHERE id=3;
```

```sqlite
2.
UPDATE band SET members=5 WHERE id=3;
```

```sqlite
3.
DELECT FROM bands WHERE id=2;
```

