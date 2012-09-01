'''
Created on 31.08.2012

@author: Matthias Wilhelm
@email: mwilhelm.kl@gmail.com
'''

from core.pdf.extract import PDFExtractor
from core.filter.single import SingleExtractor
from core.filter.pair import PairExtractor
from core.filter.dedup import DeDuplicate

from core.histo.histogram import Histogram

class PDFClouder(object):
    def __init__(self, pdf):
        self.pdf = pdf
        
    def get_histo(self):
        pdfex = PDFExtractor(self.pdf)
        single = SingleExtractor()
        pair = PairExtractor()
        dedup = DeDuplicate()
        
        words = pdfex.get_words(cleanup=True)
        
        singles = single.extract(words)
        pairs = pair.extract(words)
        
        histo = pair.dedup(singles, pairs)
        histo = dedup.dedup(histo)
        
        return histo