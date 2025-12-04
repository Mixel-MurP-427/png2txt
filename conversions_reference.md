# Data Conversions Reference Sheet

## Ascii

### `chr`
Convert int to ascii.
```python
>>> chr(65)
'A'
>>> chr(122)
'z'
>>> chr(63)
'?'
```

### `ord`
convert ascii to int.
```python
>>> ord('A')
65
>>> ord('z')
122
>>> ord('?')
63
```

## Binary

### bin
```python
>>> 0b11111111
255
>>> 0b101
5
```

### `bin()`
Convert int to bin string.
```python
>>> bin(255)
'0b11111111'
>>> bin(5)
'0b101'
```

### `int(str, 2)`
Convert bin string to int. Note that `'0b'` is optional.
```python
>>> int('11111111', 2)
255
>>> int('0b101', 2)   
5
```


## Hexadecimal

### hex
```python
>>> 0xff
255
>>> 0x43
67
```

### `hex()`
Convert int to hex string.
```python
>>> hex(255)
'0xff'
>>> hex(67)
'0x43'
```

### `int(str, 16)`
Convert hex string to int. Note that `'0x'` is optional.
```python
>>> int('ff', 16)
255
>>> int('0x43', 16)
67
```


## Bytes



bytes

int.from_bytes

big endian vs little endian

bytes.fromhex

.hex

.encode('utf-8')