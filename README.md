# editai

Simple REPL using OpenAI's edit API.

## installation

```
python setup.py install
```
or
```
pip install .
```

```
cp .env.example .env
vim .env
```

Set your OpenAI API Key in the `.env` file.

## usage

```
editai [--input filename] [--temperature float]
```

If filename is `-` it reads from _stdin_. Temperature is anywhere from 0 to 1, 1 by default.

When prompted, enter an instruction to change the input. The application will use the output
from OpenAI as the input for the next instruction.

### special instructions

* `:d` - delete the current input, setting it to "".
* `:q` - quit the REPL.
* `:t float` - set the temperature for the next request. Must be value from 0 to 1.
* `:u` - undo the last change to the input.
* `:w filename` - write input to a filename.

If you press Enter, submitting nothing, the current input is displayed.

### sample session

```
editai --temperature 0.2

>>> Write a function in python that calculates fibonacci
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(9))

>>> add documentation
def fibonacci(n):
    """
    Returns the nth number in the fibonacci sequence
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(9))

>>> :d

>>> write a function in javascript that calculate fibonacci
function fibonacci(n) {
    if (n < 2) {
        return n;
    }
    return fibonacci(n - 1) + fibonacci(n - 2);
}

console.log(fibonacci(5));

>>> :w fib.js
>>> :q

$ cat fib.js
function fibonacci(n) {
    if (n < 2) {
        return n;
    }
    return fibonacci(n - 1) + fibonacci(n - 2);
}

console.log(fibonacci(5));
```
