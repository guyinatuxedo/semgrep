## Rules to Write

Rule Types:

* [Function is Called Check](#Function is Called Check)
* [Static Size Overflow Check](#Static Size Overflow Check)
* [Dst is Static Size Check](#Dst is Static Size Check)
* [Ambiguous Write Size Check](#Variable Write Size Check)
* [Sprintf "%s" Check](#Sprintf "%s" Check)
* [Fmt String Check](#Fmt String Check)

#### Function is Called Check

This check effectively will just check if the function is called.

#### Static Size Overflow Check

This check if it can get the size of the dst (if it has a static size), and the size that it can write. If it can, it will check to see if it can write more bytes than the dst buffer can hold.

#### Dst is Static Size Check

This is a check to see if the dst buffer has a static size.

#### Variable Write Size Check

This is a check to see if the size of the write is variable.

#### Sprintf "%s" Check

This is a check to see if `sprintf` (or equivalent) has a `%s` format string.

#### Fmt String Check

This is a check for a typical fmt string exploit (one you can use `%n` with).


## Functions

* [gets](#gets)
* [fgets](#fgets)
* [strcpy](#strcpy)
* [memcpy](#memcpy)
* [sprintf](#sprintf)
* [printf](#printf)
* [memset](#memset)
* [scanf](#scanf)

#### gets

Cheks:
```
gets_is_called	:	Function is called
```

#### fgets

Checks:
```
fgets_static_size_overflow	:	Static Size Overflow Check
fgets_dst_static			:	Dst is Static Size Check
fgets_variable_write		:	Variable Write Size Check
```

#### strcpy

Checks:
```
strcpy_dst_static			:	Dst is Static Size Check
```

#### memcpy

Checks:
```
memcpy_static_size_overflow	:	Static Size Overflow Check
memcpy_dst_static			:	Dst is Static Size Check
memcpy_variable_write		:	Variable Write Size Check
```

#### bcopy

Checks:
```
bcopy_static_size_overflow	:	Static Size Overflow Check
bcopy_dst_static			:	Dst is Static Size Check
bcopy_variable_write		:	Variable Write Size Check
```

#### sprintf

Checks:
```
sprintf_s	:	Sprintf "%s" Check
```

Functions:
```
sprintf
asprintf
```

#### printf

Checks:
```
printf_fmt_string	:	Fmt String Check
```

#### memset

Checks:
```
memset_dst_static			:	Dst is Static Size Check
memset_variable_write		:	Variable Write Size Check
memset_static_size_overflow	:	Static Size Overflow Check
```

Functions:
```
memset
```

#### scanf

Checks:
```
scanf_s		:	Fmt String Check
```