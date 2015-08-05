title: Python NumExpr OOT Module
brief: A speedy embedded python block powered by NumExpr
tags:
  - python
author:
  - Sebastian Koslowski <sebastian.koslowski@kit.edu>
copyright_owner:
  - Sebastian Koslowski
license:
repo: https://github.com/skoslowski/gr-numexpr
---
This module contains a single block which lets you enter a [NumExpr](https://github.com/pydata/numexpr) expression to be used as work function. The result is a speedy embedded python block.

In addition, any python callable can be passed. It must take one arg per input stream and produce a single array. The numexpr module is not required in this mode.
