'''
Created on 31.08.2012

@author: Matthias Wilhelm
@email: mwilhelm.kl@gmail.com
'''

from collections import defaultdict
from operator import itemgetter

from core.pdf.extract import PDFExtractor

class PDFClouder(object):
    def __init__(self, pdf):
        self.pdf = pdf
        
    def get_histo(self):
        pdfex = PDFExtractor(self.pdf)
        
        words = pdfex.get_words(cleanup=True)
        
        dw = defaultdict(int)
        
        for word in words:
            dw[word] += 1
            
        hist = sorted(dw.iteritems(), key=itemgetter(1), reverse=True)
        
        return hist