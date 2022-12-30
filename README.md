# editai

Simple REPL using OpenAI's edit API.

## usage

```
editai [--input filename] [--temperature float]
```

If filename is `-` it reads from _stdin_. Temperature is anywhere from 0 to 1, 1 by default.

When prompted, enter an instruction to change the input. The application will use the output
from OpenAI as the input for the next instruction.

### special instructions

* `:q` - quit the REPL.
* `:u` - undo the last change to the input.
* `:w filename` - write input to a filename.
