'''
Created on 01.09.2012

@author: Matthias Wilhelm
@email: mwilhelm.kl@gmail.com
'''

from ..histo.histogram import Histogram

class PairExtractor(object):
    def __init__(self):
        pass
    
    #####################################################
    
    def extract(self, words):
        res_words = []
            
        prev = ''
        for word in words:
            if prev:
                res_words.append("~".join([prev, word]))
            prev = word

        return Histogram(res_words)

    #####################################################
    
    def dedup(self, singles, pairs):
        result = singles
        
        for pair, cnt in pairs.items():
            words = pair.split('~')
            all_words_valid = True
            
            for word in words:
                if word not in singles:
                    all_words_valid = False
                    
            if all_words_valid:
                result[pair] += cnt
                
                for word in words:
                    result[word] -= cnt
        
        return result