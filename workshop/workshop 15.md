```sqlite
1.
CREATE TABLE bands(
	id INTEGER,
	name TEXT,
	debut INTEGER);
INSERT INTO bands 
VAULES (1,"Queen",1973);
INSERT INTO bands 
VAULES (2,"Coldplay",1998);	
INSERT INTO bands 
VAULES (3,"MCR",2001);	
```

```sqlite
2.
SELECT id,name FROM bands; 
```

```sqlite
3.
SELECT name FROM bands WHERE debut<2000;
```

