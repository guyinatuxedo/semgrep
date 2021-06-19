# Testcases

This document briefly describes the various code sources I use for basic testing of these semgrep rules. I break them up by function class, with these being the various classes.

* [gets](#gets)
* [fgets](#fgets)
* [strcpy](#strcpy)
* [memcpy](#memcpy)
* [sprintf](sprintf)
* [printf](#printf)

## gets

This class contains the following checks:
* [gets-000](#gets-000)

#### gets-000

This is just source code where `gets` is called.

It should be flagged by these rules:
```
gets_is_called
```

## fgets

This class contains the following checks:
* [fgets-000](#fgets-000)
* [fgets-001](#fgets-001)
* [fgets-002](#fgets-002)
* [fgets-003](#fgets-003)
* [fgets-004](#fgets-004)

#### fgets-000

This is an instance where `fgets` is scanning in more data into a stack buffer, then it can hold, and thus is a buffer overflow.

It should be flagged by these rules:
```
fgets_static_size_overflow
fgets_dst_static
```

### fgets-001

Fgets is scanning in a set amount of bytes into a buffer that is passed in as an arguments.

It shouldn't be flagged by any rules.

### fgets-002

Fgets is scanning in more data to a bss buffer then it can hold, and thus an overflow.

It should be flagged by these rules:
```
fgets_static_size_overflow
fgets_dst_static
```

### fgets-003

Fgets is scanning in data into a buffer that is dynamically allocated.

It shouldn't be flagged by any rules.

### fgets-004

Fgets is scanning in data into a buffer, with a variable size.

It should be flagged by these rules:
```
fgets_variable_write
fgets_dst_static
```
## strcpy

This class contains the following checks:
* [strcpy-000](#strcpy-000)
* [strcpy-001](#strcpy-001)

#### strcpy-000

Strcpy is writing data to a buffer with a static size.

It should be flagged by these rules:
```
strcpy_dst_static
```

#### strcpy-001

Strcpy is writing data to a dynamically allocated buffer.

It shouldn't be flagged by any rules.

## memcpy

This class contains the following checks:
* [memcpy-000](#memcpy-000)
* [memcpy-001](#memcpy-001)
* [memcpy-002](#memcpy-002)
* [memcpy-003](#memcpy-003)
* [memcpy-004](#memcpy-004)

#### memcpy-000

This is an instance where `memcpy` is scanning in more data into a stack buffer, then it can hold, and thus is a buffer overflow.

It should be flagged by these rules:
```
memcpy_static_size_overflow
memcpy_dst_static
```

### memcpy-001

memcpy is scanning in a set amount of bytes into a buffer that is passed in as an arguments.

It shouldn't be flagged by any rules.

### memcpy-002

Fgets is scanning in more data to a bss buffer then it can hold, and thus an overflow.

It should be flagged by these rules:
```
memcpy_static_size_overflow
memcpy_dst_static
```

### memcpy-003

Fgets is scanning in data into a buffer that is dynamically allocated.

It shouldn't be flagged by any rules.

### memcpy-004

memcpy is scanning in data into a buffer, with a variable size.

It should be flagged by these rules:
```
memcpy_variable_write
memcpy_dst_static
```

## sprintf

This class contains the following checks:
* [sprintf-000](#sprintf-000)
* [sprintf-001](#sprintf-001)
* [sprintf-002](#sprintf-002)

#### sprintf-000

This is writing to a string, using the `%s` fmt string.

It should be flagged by these rules:
```
sprintf_s
```

#### sprintf-001

This is writing to a string, using the `%S` fmt string.

It should be flagged by these rules:
```
sprintf_s
```

#### sprintf-002

This is writing to a string with the `%2s` fmt string.

It shouldn't be flagged by any rule.

## printf

This class contains the following checks:
* [printf-000](#printf-000)
* [printf-001](#printf-001)
* [printf-002](#printf-002)

#### printf-000

This is an instance where `printf` gets a single argument, which is a char array. If the user controls it, you have a fmt string.

It should be flagged by these rules:
```
printf_fmt_string
```

#### printf-001

This is just `printf` printing a static string (with `"`) with no fmt strings.

It should not be flagged by any rules.

#### printf-002

This is just `printf` printing a static string (with `'`) with no fmt strings.

It should not be flagged by any rules.
