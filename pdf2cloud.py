#! /usr/bin/env python

from core.main import PDFClouder

pdf = 'examples/SRC-Wilhelm.pdf'
#pdf = '/Users/mwilhelm/Desktop/nessa.pdf'
pdfc = PDFClouder(pdf)

result = pdfc.get_histo()

for word, cnt in result:
    if cnt > 1:
        #print '%s: %i' % (word.encode('utf-8'), cnt)
        print ' '.join([word.encode('utf-8') for word in [word]*cnt]),