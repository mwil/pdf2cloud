'''
Created on 01.09.2012

@author: Matthias Wilhelm
@email: mwilhelm.kl@gmail.com
'''

from wordfilter import WordFilter
from histogram import Histogram

class SingleExtractor(object):
    def __init__(self):
        self.wf = WordFilter()
    
    ##################################################
    
    # Filter out words that are not wanted for the tag cloud and return a histogram
    # of it, a defaultdict with words as keys and counts as values.
    #
    def extract(self, words):
        res_words = self.wf.filter(words)
        
        return Histogram(res_words)
