# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 10:34:32 2017

@author: Jrahman
"""

from ManipulateData import ManipulateData

manipulate = ManipulateData();

manipulate.columnSplit("pos_MIPS_complexes.txt", "positives")
manipulate.columnSplit("L_neg.txt", "negatives");
