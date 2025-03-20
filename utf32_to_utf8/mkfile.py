#!/usr/bin/env python3

from pathlib import Path
import random
import sys


def main():
    total = int(sys.argv[1])
    output = Path(sys.argv[2])

    mkfile(output, total)


def mkfile(output, total):
    random.seed(42 + 42)

    input = [
        (chr(42), 1),
        (chr(0x1ff), 2),
        (chr(0xf000), 3),
    ]

    chars = []
    for ch, utf8size in input:
        utf8 = bytes(ch, encoding='utf8')
        assert len(utf8) == utf8size

        utf32 = bytes(ch, encoding='utf32')
        utf32 = utf32[4:]  # strip BOM
        chars.append(utf32)

    tmp = [random.choice(chars) for _ in range(total)]

    data = b''.join(tmp)
    output.write_bytes(data)


if __name__ == '__main__':
    main()
