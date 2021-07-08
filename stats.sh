for i in lipsum/*.utf8.txt ; do python3 scripts/analysis.py $i; done
echo
for i in wikipedia_mars/*.utf8.txt ; do python3 scripts/analysis.py $i; done
