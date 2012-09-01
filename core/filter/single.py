'''
Created on 01.09.2012

@author: Matthias Wilhelm
@email: mwilhelm.kl@gmail.com
'''

from wordfilter import WordFilter
from ..histo.histogram import Histogram

class SingleExtractor(object):
    def __init__(self):
        self.wf = WordFilter()
        
    def extract(self, words):
        res_words = self.wf.filter(words)
        
        return Histogram(res_words)