#!/usr/bin/env python3

from pathlib import Path
import random
import sys


def main():
    total = int(sys.argv[1])
    surrogates_fract = float(sys.argv[2])
    output = Path(sys.argv[3])

    assert 1.0 >= surrogates_fract >= 0.0

    mkfile(output, total, surrogates_fract)


def mkfile(output, total, surrogates_fract):
    surrogates_count = int(total * surrogates_fract)

    random.seed(42 + 42)

    non_surrogates = [chr(rand_non_surrogate()) for _ in range(total - surrogates_count)]
    surrogates = [chr(0x1_0000 + random.randint(0, 0xffff)) for _ in range(surrogates_count)]

    tmp = surrogates + non_surrogates
    random.shuffle(tmp)

    joined = ''.join(tmp)
    data = bytes(joined, encoding='utf32')
    data = data[4:]  # strip BOM

    output.write_bytes(data)


def rand_non_surrogate():
    while True:
        v = random.randint(0, 0xffff)
        if (v & 0xf800) != 0xd800:
            return v



if __name__ == '__main__':
    main()
