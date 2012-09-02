'''
Created on 31.08.2012

@author: Matthias Wilhelm
@email: mwilhelm.kl@gmail.com
'''

from core.pdf import PDFExtractor
from core.wordfilter import WordFilter
from core.pair import PairExtractor
from core.triple import TripleExtractor

from core.histogram import Histogram

# Bundle together the PDF extraction and the processing steps on the extracted words
#
class PDFClouder(object):
    def __init__(self, pdf):
        self.pdf = pdf
        
    def get_histo(self, refs=False):
        pdfex = PDFExtractor(self.pdf)
        pair = PairExtractor()
        triple = TripleExtractor()
        wfilter = WordFilter()
        
        words = pdfex.get_words(cleanup=True, refs=refs)
        words = wfilter.cleanup(words) 

        singles = Histogram(words)
        
        # FIXME: don't feed cleanup words, this makes weird pairs
        pairs = pair.extract(words, wfilter=singles)        
        triples = triple.extract(words, wfilter=pairs)
        
        # FIXME: this kills too many singles, something's wrong here.
        pairs = pair.dedup(singles, pairs)
        triples = triple.dedup(pairs, triples)
        
        histo = singles.merge(pairs, triples)
        
        return histo
