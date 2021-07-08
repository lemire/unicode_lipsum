
def detect_format(data):
    try:
      c = data.decode('utf-8')
      return "utf-8"
    except:
      try:
        c = data.decode('utf-16')
        return "utf-16"
      except:
        raise "unknown"

import sys
filename=sys.argv[1]

def processutf8(data):
    asciib = 0
    fourbyte = 0
    threebyte = 0
    twobyte = 0
    utf16size = 0
    for x in data:
        if(x<0b10000000):
            asciib += 1
            utf16size += 1
        elif(x >= 0b11110000):
            fourbyte += 1
            utf16size += 2
        elif(x >= 0b11100000):
            threebyte += 1
            utf16size += 1
        elif(x >= 0b11000000):
            twobyte += 1
            utf16size += 1
    characters = (asciib+twobyte+threebyte+fourbyte) * 1.0
    averageutf8 = 1.0 * len(data) / characters
    averageutf16 = 2.0 * utf16size / characters

    return (averageutf8, averageutf16, asciib/characters*100, twobyte/characters*100, threebyte/characters*100, fourbyte/characters*100)

def form(tup):
    print('%.1f & %.1f      & %.0f  & %.0f  & %.0f  & %.0f \\\\' % tup)


import os

basename, file_extension = os.path.splitext(os.path.basename(filename))
basename, file_extension = os.path.splitext(os.path.basename(basename))
print(basename.split("-")[0].capitalize(), end=" & ")

with open(filename, "rb") as in_file:
    data = in_file.read()
    if(detect_format(data) == "utf-8"):
        form(processutf8(data))
    else:
        print("please process UTF-8")
