#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 09:30:21 2021

@author: thangdnsf
"""
import pandas as pd

class TLUclass:
    """
    This is example class, that shows way to init class
    """
    def __init__(self, filename = 'advanced_python.csv': str) -> None:
        self.df = pd.read_csv(filename,sep=';')
        
    def getstudentsbycode(self,studentcode: str):
        """
        a function allow to select a sutdent by student code

        Parameters
        ----------
        studentcode : str
            code of student.

        Returns
        -------
        Data frame
            a student info by student code

        """
        return self.df[self.df['student code']  == studentcode]
    
if __name__ == "__main__":
    pythonclass = TLUclass('advanced_python.csv')
    print(pythonclass.getstudentsbycode('A36708'))