import re


def normalize(s):
    s = s.lower()
    s = re.sub(r"\(.*\)","",s)
    s = re.sub(r"\[.*\]","",s)
    s = re.sub(r"and|the|of","", s)
    s = s.rstrip('.')
    return set(s.split(None))