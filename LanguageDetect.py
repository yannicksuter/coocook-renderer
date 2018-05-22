#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pycld2 as cld2

class UnknownLanguage(Exception):
    """Raised if we can not detect the language of a text snippet."""

def detect_language(text):
    t = text.encode("utf-8")
    reliable, index, top_3_choices = cld2.detect(t, bestEffort=False)

    if not reliable:
        reliable, index, top_3_choices = cld2.detect(t, bestEffort=True)
        if not reliable:
            raise UnknownLanguage("Try passing a longer snippet of text")

    return top_3_choices[0]
