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
