'''
Created on 01.09.2012

@author: Matthias Wilhelm
@email: mwilhelm.kl@gmail.com
'''

from histogram import Histogram

class TripleExtractor(object):
    def __init__(self):
        pass
    
    #####################################################
    
    # Find all possible triples in the list, pruning comes later (dedup below)
    #
    def extract(self, words, wfilter=[]):
        res_words = []
            
        pprev = ''
        prev = ''
        for word in words:            
            if not word or u'~'.join([prev, word]) not in set(wfilter):
                pprev, prev = '', word
                continue
            
            if prev and pprev:
                res_words.append("~".join([pprev, prev, word]))
                
            pprev, prev = prev, word

        return Histogram(res_words)

    #####################################################
    
    # Remove duplicates from singles that also appear in triples.
    # Since singles are cleaned up, keep only triples that contain only checked words.
    # Recalculate count of singles, subtract what we gain from the triples.
    #
    def dedup(self, pairs, triples):
        result = Histogram()
        
        for triple, cnt in triples.items():
            if cnt < 3:
                continue
            
            words = triple.split('~')
            words = ['~'.join(words[:2]), '~'.join(words[1:])]
                    
            result[triple] += cnt
                
            for word in words:
                result[word] = pairs[word] - cnt
        
        return result
