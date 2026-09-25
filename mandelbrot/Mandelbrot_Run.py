#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 21:43:21 2026

@author: User
"""

from Mandelbrot_Set import Mandelbrot_Set

if __name__=="__main__":
    mand = Mandelbrot_Set( -2.025, 0.6, -1.125, 1.125, (1/512))
    mand.calc()
    mand.display()
