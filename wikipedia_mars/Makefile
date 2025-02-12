# https://en.wikipedia.org/wiki/List_of_Wikipedias
# pip install html2text
%.utf8.txt: %.html
	html2text $^ > $@

%.utf16.txt: %.utf8.txt
	iconv -f UTF-8 -t UTF-16LE $^ > $@

%.utf16be.txt: %.utf8.txt
	iconv -f UTF-8 -t UTF-16BE $^ > $@

%.utf32.txt: %.utf8.txt
	iconv -f UTF-8 -t UTF-32LE $^ > $@

%.utf32be.txt: %.utf8.txt
	iconv -f UTF-8 -t UTF-32LE $^ > $@

%.latin1.txt: %.utf8.txt
	iconv -c -f UTF-8 -t ISO-8859-1 $^ > $@

%.utflatin8.txt: %.latin1.txt
	iconv -f ISO-8859-1 -t UTF-8 $^ > $@

%.utflatin16.txt: %.latin1.txt
	iconv -f ISO-8859-1 -t UTF-16LE $^ > $@

%.utflatin16be.txt: %.latin1.txt
	iconv -f ISO-8859-1 -t UTF-16BE $^ > $@

%.utflatin32.txt: %.latin1.txt
	iconv -f ISO-8859-1 -t UTF-32LE $^ > $@

%.utflatin32be.txt: %.latin1.txt
	iconv -f ISO-8859-1 -t UTF-32BE $^ > $@

HTML=english.html \
     french.html \
     persan.html \
     esperanto.html \
     german.html \
     arabic.html \
     czech.html \
     greek.html \
     hindi.html \
     hebrew.html \
     portuguese.html \
     russian.html \
     thai.html \
     turkish.html \
     vietnamese.html \
     japanese.html \
     korean.html \
     chinese.html

TXT=$(HTML:html=utf8.txt)
TXT16=$(HTML:html=utf16.txt) $(HTML:html=utf16be.txt)
TXT32=$(HTML:html=utf32.txt) $(HTML:html=utf32be.txt)

LATIN1=esperanto.html \
       french.html \
       german.html \
       portuguese.html

LATIN1UTF=$(LATIN1:html=latin1.txt) \
          $(LATIN1:html=utflatin8.txt) \
          $(LATIN1:html=utflatin16.txt) \
          $(LATIN1:html=utflatin16be.txt) \
          $(LATIN1:html=utflatin32.txt) \
          $(LATIN1:html=utflatin32be.txt)

.PHONY: all
all: $(HTML) $(TXT) $(TXT16) $(TXT32) $(LATIN1UTF)

english.html:
	wget -O $@ https://en.wikipedia.org/wiki/Mars

french.html:
	wget -O $@ "https://fr.wikipedia.org/wiki/Mars_(plan%C3%A8te)"

persan.html:
	wget -O $@ https://fa.wikipedia.org/wiki/%D9%85%D8%B1%DB%8C%D8%AE

esperanto.html:
	wget -O $@ "https://eo.wikipedia.org/wiki/Marso_(planedo)"

german.html:
	wget -O $@ "https://de.wikipedia.org/wiki/Mars_(Planet)"

arabic.html:
	wget -O $@ https://ar.wikipedia.org/wiki/%D8%A7%D9%84%D9%85%D8%B1%D9%8A%D8%AE

czech.html:
	wget -O $@ "https://cs.wikipedia.org/wiki/Mars_(planeta)"

greek.html:
	wget -O $@ "https://el.wikipedia.org/wiki/%CE%86%CF%81%CE%B7%CF%82_(%CF%80%CE%BB%CE%B1%CE%BD%CE%AE%CF%84%CE%B7%CF%82)"

hindi.html:
	wget -O $@ https://hi.wikipedia.org/wiki/%E0%A4%AE%E0%A4%82%E0%A4%97%E0%A4%B2_%E0%A4%97%E0%A5%8D%E0%A4%B0%E0%A4%B9

hebrew.html:
	wget -O $@ https://he.wikipedia.org/wiki/%D7%9E%D7%90%D7%93%D7%99%D7%9D

portuguese.html:
	wget -O $@ "https://pt.wikipedia.org/wiki/Marte_(planeta)"

russian.html:
	wget -O $@ https://ru.wikipedia.org/wiki/%D0%9C%D0%B0%D1%80%D1%81

thai.html:
	wget -O $@ https://th.wikipedia.org/wiki/%E0%B8%94%E0%B8%B2%E0%B8%A7%E0%B8%AD%E0%B8%B1%E0%B8%87%E0%B8%84%E0%B8%B2%E0%B8%A3

turkish.html:
	wget -O $@ https://tr.wikipedia.org/wiki/Mars

vietnamese.html:
	wget -O $@ https://vi.wikipedia.org/wiki/Sao_H%E1%BB%8Fa

japanese.html:
	wget -O $@ https://ja.wikipedia.org/wiki/%E7%81%AB%E6%98%9F

korean.html:
	wget -O $@ https://ko.wikipedia.org/wiki/%ED%99%94%EC%84%B1

chinese.html:
	wget -O $@ https://zh.wikipedia.org/wiki/%E7%81%AB%E6%98%9F
