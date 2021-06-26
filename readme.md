# semgrep

## Usage

To use semgrep:
```
$	semgrep --config=<rules> <directory with source code>
```

For example, to run the `rules/gets/gets_is_called` rules against all source code files in the `example_source` directory:
```
$	semgrep --config=rules/gets/gets_is_called example_source/
running 1 rules...
example_source/gets/gets-000.c
severity:error rule:rules.gets.gets_is_called: gets() is called, buffer overflow time
6:	gets(input);
ran 1 rules on 19 files: 1 findings
```

## Installation

```
sudo pip3 install semgrep
```

# Todo


## Function Addtion:

```
18/28

Check (https://www.gnu.org/software/libc/manual/html_node/Function-Index.html)
	-	b
	-	f
	-	g
	-	m
	-	p
	-	r
	-	s
	-	v
	-	w
	-	x
```

## Feature Implementation:

```
Ghidra Integration
Function fine tuning
Output desing
```

## Evaluation:
```
000/100 CTF Challs
00/20 N-Days
00/20 github
```
