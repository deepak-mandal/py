#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 19:44:56 2020

@author: deepak
"""


#print all key-value pairs in the dictionary
capitals={'USA':'New York', 'France':'Paris', 'Japan':'Tokyo', 'India':'New Delhi'}
for country in capitals.keys():
    print('The capitals of {} is {}.'.format(country, capitals.get(country)))