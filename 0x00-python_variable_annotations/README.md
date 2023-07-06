# Python Annotations
# Tasks
0. Basic annotations - add
mandatory
Write a type-annotated function add that takes a float a and a float b as arguments and returns their sum as a float.
1. Basic annotations - concat
mandatory
Write a type-annotated function concat that takes a string str1 and a string str2 as arguments and returns a concatenated string
2. Basic annotations - floor
mandatory
Write a type-annotated function floor which takes a float n as argument and returns the floor of the float.
3. Basic annotations - to string
mandatory
Write a type-annotated function to_str that takes a float n as argument and returns the string representation of the float.
4. Define variables
mandatory
Define and annotate the following variables with the specified values:

a, an integer with a value of 1
pi, a float with a value of 3.14
i_understand_annotations, a boolean with a value of True
school, a string with a value of “Holberton”
5. Complex types - list of floats
mandatory
Write a type-annotated function sum_list which takes a list input_list of floats as argument and returns their sum as a float.
6. Complex types - mixed list
mandatory
Write a type-annotated function sum_mixed_list which takes a list mxd_lst of integers and floats and returns their sum as a float.
7. Complex types - string and int/float to tuple
mandatory
Write a type-annotated function to_kv that takes a string k and an int OR float v as arguments and returns a tuple. The first element of the tuple is the string k. The second element is the square of the int/float v and should be annotated as a float.
8. Complex types - functions
mandatory
Write a type-annotated function make_multiplier that takes a float multiplier as argument and returns a function that multiplies a float by multiplier.
9. Let's duck type an iterable object
mandatory
Annotate the below function’s parameters and return values with the appropriate types


![](https://florian-dahlitz.de/media/articles/leverage-the-full-potential-of-type-hints/thumbnail-m.webp)

Python is a dynamically-typed language. That means that variable types are dynamically set at run-time, upon assignment of a value to a variable.

For example, in
```python
def fn(a, b):
    return a + b
```
The types of a and b are not known at build-time, only when a and b are assigned values at run-time.

Hence, calling
```python

def fn(a, b):
    return a + b


fn("a", 1)
```
somewhere in your code will not raise an exception until the code is actually executed and the function is called:

```bash
>>> fn("a", 1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
```
In Python 3, type annotations do not change this. Python is still a dynamically-typed language. Type annotations serve the following purpose:

- Code documentation: thanks to them, a developer reading type-annotated code (his own or someone else’s) will know exactly what type each variables is supposed to be. This helps reduce bugs and exceptions and accelerate the development cycle.
- Linting and validation: code editors and continuous integration (CI) pipelines can be configured to automatically validate type-annotated code at build-time and catch bugs before they make it to production.

## Objectives

- Type annotations in Python 3
- How you can use type annotations to specify function signatures and variable types
- Duck typing
- How to validate your code with mypy

## Study materials

- [Typing module](https://docs.python.org/3/library/typing.html)

- [mypy](https://mypy.readthedocs.io/en/latest/cheat_sheet_py3.html)

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on `Ubuntu 18.04 LTS` using `python3 (version 3.7)`
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- A __README.md file__, at the root of the folder of the project, is mandatory
- Your code should use the `pycodestyle style (version 2.5.)`
- All your files must be executable
- The length of your files will be tested using `wc`
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have a documentation (python3 -c '`print(__import__("my_module").my_function.__doc__)`' and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')`
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
