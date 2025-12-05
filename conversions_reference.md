# Data Conversions Reference Sheet

**Note:** This sheet has some gaps that my be filled in the future.

**Hierarchy:**

- int
- bin
- hex
- ascii
- bytes


## Convert To Int

### from bin
```python
>>> 0b11111111
255
>>> 0b101
5
```

### from bin string
Note that `'0b'` is optional.
```python
>>> int('11111111', 2)
255
>>> int('0b101', 2)   
5
```

### from hex
```python
>>> 0xff
255
>>> 0x43
67
```

### from hex string
Note that `'0x'` is optional.
```python
>>> int('ff', 16)
255
>>> int('0x43', 16)
67
```

### from ascii
```python
>>> ord('A')
65
>>> ord('z')
122
>>> ord('?')
63
```

### from bytes
```python
>>> int.from_bytes(b'\x00')
0
>>> int.from_bytes(b'\xff')
255
>>> int.from_bytes(b'\x03\xe8')
1000
>>> int.from_bytes(b'ABC')
4276803
```


## Convert To Bin

### from int
```python
>>> bin(255)
'0b11111111'
>>> bin(5)
'0b101'
```


## Convert To Hex

### from int
```python
>>> hex(255)
'0xff'
>>> hex(67)
'0x43'
```

### from bytes
```python
>>> b'\xff'.hex()
'ff'
>>> b'\x0a\xbc'.hex()
'0abc'
>>> b'ABC'.hex() 
'414243'
```


## Convert To Ascii

### from int
```python
>>> chr(65)
'A'
>>> chr(122)
'z'
>>> chr(63)
'?'
```

### from bytes
```python
>>> b'ABC'.decode('utf-8')
'ABC'
>>> b'123'.decode('utf-8')
'123'
>>> b'Hello world!'.decode('utf-8')
'Hello world!'
```


## Convert To Bytes

### from hex
```python
>>> bytes.fromhex('ff') 
b'\xff'
>>> bytes.fromhex('03e8')
b'\x03\xe8'
```

### from ascii
```python
>>> 'ABC'.encode('utf-8')
b'ABC'
>>> '123'.encode('utf-8')
b'123'
>>> 'Hello world!'.encode('utf-8')
b'Hello world!'
```