#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2015 <+YOU OR YOUR COMPANY+>.
#
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.

import numpy
try:
    import numexpr
except ImportError:
    numexpr = None

from gnuradio import gr


class numexpr_evaluate(gr.sync_block):
    """
    Let's you run any NumExpr as a GR block. NumExpr are optimal; generic
    callables can also be used
    """
    def __init__(
            self, expression='in0',
            in_sig=(numpy.complex64,), out_sig=(numpy.complex64,),
            nthreads=None
    ):
        """
        Args:
        expression: either a NumExpr string (in0, in1, ... are the inputs) or
                    a callable (in0, in1 as args) to be used in work()
        in_sig: a list of numpy dtype as input signature
        out_sig: a list of numpy dtype as output signature
        nthreads: how many threads NumExpr should use
        """
        gr.sync_block.__init__(self, "numexpr_evaluate", in_sig, out_sig)
        self._expression = None
        if numexpr and nthreads:
            numexpr.set_num_threads(nthreads)
        self.expression = expression

    @property
    def expression(self):
        return self._expression

    @expression.setter
    def expression(self, value):
        self._expression = value
        if numexpr:
            self.work = self.__class__.work
        elif callable(value):
            self.work = work_callable
        else:
            raise ValueError("Can't import 'numexpr'. You can only pass a"
                             "callable as 'expression' in this mode.")

    def work_numexpr(self, input_items, output_items):
        local_dict = dict(
            ('in'+str(i), items) for i, items in enumerate(input_items)
        )
        output_items[0][:] = numexpr.evaluate(self.expression, local_dict)
        return len(output_items[0])

    def work_callable(self, input_items, output_items):
        output_items[0][:] = self.expression(*input_items)
        return len(output_items[0])

    work = work_numexpr
