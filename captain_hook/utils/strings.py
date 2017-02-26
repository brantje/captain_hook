from __future__ import absolute_import
import re


def toCamelCase(text):
    word_list = text.split('_')
    return ''.join(word.capitalize() for word in word_list)

def toSnakeCase(text):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
