'''
Created on 31.08.2012

@author: Matthias Wilhelm
@email: mwilhelm.kl@gmail.com
'''

from collections import defaultdict
from operator import itemgetter

from core.pdf.extract import PDFExtractor
from core.spell.wordfilter import WordFilter

class PDFClouder(object):
    def __init__(self, pdf):
        self.pdf = pdf
        
    def get_histo(self):
        pdfex = PDFExtractor(self.pdf)
        wf = WordFilter()
        
        words = pdfex.get_words(cleanup=True)
        
        words = wf.filter(words)
        
        dw = defaultdict(int)
        
        for word in words:
            dw[word] += 1
            
        hist = sorted(dw.iteritems(), key=itemgetter(1), reverse=True)
        
        return hist