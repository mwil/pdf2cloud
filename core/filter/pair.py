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
    
    # Find all possible pairs in the list, pruning comes later (dedup below)
    #
    def extract(self, words):
        res_words = []
            
        prev = ''
        for word in words:
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
