#
# UTF-32 files having the given percentage of characters
# producing surrogate pairs when converted to UTF-16.
#


ALL=64k_000perc_surrogates.utf32.txt \
    64k_005perc_surrogates.utf32.txt \
    64k_025perc_surrogates.utf32.txt \
    64k_033perc_surrogates.utf32.txt \
    64k_050perc_surrogates.utf32.txt \
    64k_075perc_surrogates.utf32.txt \
    64k_095perc_surrogates.utf32.txt \
    256k_000perc_surrogates.utf32.txt \
    256k_005perc_surrogates.utf32.txt \
    256k_025perc_surrogates.utf32.txt \
    256k_033perc_surrogates.utf32.txt \
    256k_050perc_surrogates.utf32.txt \
    256k_075perc_surrogates.utf32.txt \
    256k_095perc_surrogates.utf32.txt

all: $(ALL)

64k_000perc_surrogates.utf32.txt: mkfile.py
	./mkfile.py 65536 0.00 $@

64k_005perc_surrogates.utf32.txt: mkfile.py
	./mkfile.py 65536 0.05 $@

64k_025perc_surrogates.utf32.txt: mkfile.py
	./mkfile.py 65536 0.25 $@

64k_033perc_surrogates.utf32.txt: mkfile.py
	./mkfile.py 65536 0.33 $@

64k_050perc_surrogates.utf32.txt: mkfile.py
	./mkfile.py 65536 0.50 $@

64k_075perc_surrogates.utf32.txt: mkfile.py
	./mkfile.py 65536 0.75 $@

64k_095perc_surrogates.utf32.txt: mkfile.py
	./mkfile.py 65536 0.95 $@

256k_000perc_surrogates.utf32.txt: mkfile.py
	./mkfile.py 262144 0.00 $@

256k_005perc_surrogates.utf32.txt: mkfile.py
	./mkfile.py 262144 0.05 $@

256k_025perc_surrogates.utf32.txt: mkfile.py
	./mkfile.py 262144 0.25 $@

256k_033perc_surrogates.utf32.txt: mkfile.py
	./mkfile.py 262144 0.33 $@

256k_050perc_surrogates.utf32.txt: mkfile.py
	./mkfile.py 262144 0.50 $@

256k_075perc_surrogates.utf32.txt: mkfile.py
	./mkfile.py 262144 0.75 $@

256k_095perc_surrogates.utf32.txt: mkfile.py
	./mkfile.py 262144 0.95 $@
