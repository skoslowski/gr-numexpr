gr-numexpr
----------

This module contains a single block which lets you enter a [NumExpr](https://github.com/pydata/numexpr) expression to be used as work function. The result is a speedy embedded python block.

In addition, any python callable can be passed. It must take one arg per input stream and produce a single array. The numexpr module is not required in this mode.
