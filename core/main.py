'''
Created on 31.08.2012

@author: Matthias Wilhelm
@email: mwilhelm.kl@gmail.com
'''

from core.pdf import PDFExtractor
from core.single import SingleExtractor
from core.pair import PairExtractor
from core.dedup import DeDuplicate

# Bundle together the PDF extraction and the processing steps on the extracted words
#
class PDFClouder(object):
    def __init__(self, pdf):
        self.pdf = pdf
        
    def get_histo(self, refs=False):
        pdfex = PDFExtractor(self.pdf)
        single = SingleExtractor()
        pair = PairExtractor()
        dedup = DeDuplicate()
        
        words = pdfex.get_words(cleanup=True, refs=refs)
        
        singles = single.extract(words)
        pairs = pair.extract(words)
        
        histo = pair.dedup(singles, pairs)
        histo = dedup.dedup(histo)
        
        return histo
