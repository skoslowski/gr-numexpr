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
# 

import numpy as np

from gnuradio import gr, gr_unittest
from gnuradio import blocks

from numexpr_evaluate import numexpr_evaluate


class qa_numexpr_evaluate(gr_unittest.TestCase):

    def test_001_copy(self):
        data = np.random.random(20).view(complex)
        
        src = blocks.vector_source_c(data)
        blk = numexpr_evaluate(expression='in0')
        snk = blocks.vector_sink_c()
        
        tb = gr.top_block()
        tb.connect(src, blk, snk)
        tb.run()
        
        np.testing.assert_allclose(snk.data(), data)

    def test_002_adder(self):
        data = np.random.random(60).view(complex).reshape((3,-1))
        
        src = [blocks.vector_source_c(d) for d in data]
        blk = numexpr_evaluate('in0+in1+in2', in_sig=(np.complex64,) * 3)
        snk = blocks.vector_sink_c()
        
        tb = gr.top_block()
        for i, source in enumerate(src):
            tb.connect((source, 0), (blk, i))
        tb.connect(blk, snk)
        tb.run()
        
        np.testing.assert_allclose(snk.data(), data.sum(0))

    def test_003_real_part(self):
        data = np.random.random(20).view(complex)
        
        src = blocks.vector_source_c(data)
        blk = numexpr_evaluate('real(in0)', out_sig=(np.float32,))
        snk = blocks.vector_sink_f()
        
        tb = gr.top_block()
        tb.connect(src, blk, snk)
        tb.run()
        
        np.testing.assert_allclose(snk.data(), data.real)


if __name__ == '__main__':
    gr_unittest.run(qa_numexpr, "qa_numexpr.xml")
