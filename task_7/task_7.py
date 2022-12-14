import re


def WordSearch(length: int, s: str, subs: str) -> list[int]:
    result = []
    strings = split(s, length)
    for i in strings:
        if len(re.findall('\\b' + subs + '\\b', i)) > 0:
            result.append(1)
        else:
            result.append(0)
    return result


def split(long_string: str, length: int) -> list[str]:
    resulted_strings = []
    splitted_strings = long_string.split(" ")
    if len(splitted_strings) == 0:
        splitted_strings.append(long_string)
    size = len(splitted_strings)
    i = 0
    while i < size:
        if splitted_strings[i] == " " or splitted_strings[i] == "":
            i += 1
            continue
        if len(splitted_strings[i]) == length:
            resulted_strings.append(splitted_strings[i])
            i += 1
            continue
        if len(splitted_strings[i]) < length:
            concat_str = splitted_strings[i]
            delta = 0
            while i + delta < size - 1 and len(concat_str) + len(splitted_strings[i + delta + 1]) < length:
                i += 1
                concat_str = concat_str + " " + splitted_strings[i]
            resulted_strings.append(concat_str)
            if delta == 0:
                i += 1
            continue
        if len(splitted_strings[i]) > length:
            delta = 0
            while delta < len(splitted_strings[i]):
                resulted_strings.append(splitted_strings[i][delta:length + delta])
                delta += length
        i += 1
    return resulted_strings
