'''
Created on 01.09.2012

@author: Matthias Wilhelm
@email: mwilhelm.kl@gmail.com
'''

from histogram import Histogram

class PairExtractor(object):
    def __init__(self):
        pass
    
    #####################################################
    
    # Find all possible pairs in the list, pruning comes later (dedup below)
    #
    def extract(self, words, wfilter=[]):
        res_words = []
            
        prev = ''
        for word in words:
            if not word or word not in set(wfilter):
                prev = ''
                continue
            
            if prev:
                res_words.append("~".join([prev, word]))
            
            prev = word

        return Histogram(res_words)

    #####################################################
    
    # Remove duplicates from singles that also appear in pairs.
    # Since singles are cleaned up, keep only pairs that contain only checked words.
    # Recalculate count of singles, subtract what we gain from the pairs.
    # 
    # For example (the~test is not accepted because of 'the')
    # {test:3, tests:2} and {the~test:1, test~tests:2} -> {test:1, tests:0, test~tests:2}
    #
    def dedup(self, singles, pairs):
        result = Histogram()
        
        for pair, cnt in pairs.items():
            if cnt < 3:
                continue
            
            words = pair.split('~')
                                
            result[pair] += cnt
                
            for word in words:
                result[word] -= cnt
        
        return result
