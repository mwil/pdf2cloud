'''
Created on 01.09.2012

@author: Matthias Wilhelm
@email: mwilhelm.kl@gmail.com
'''

from ..histo.histogram import Histogram

class DeDuplicate(object):
    def __init__(self):
        pass
    
    #######################################################
    
    # Run all methods to de-duplicate unneeded elements in the histo.
    #
    def dedup(self, histo):
        result = self.decap(histo)
        result = self.deplural(result)
        
        return result
    
    #######################################################
    
    # If both a capitalized and lower version of a word is around, choose only
    # the one with higher count.
    # For example: {test:1, Test:2} -> {Test:3}
    #
    # FIXME: since pairs are included there may be un-handled cases such as the~Test.
    #
    def decap(self, histo):
        result = Histogram()
        
        for word, cnt in histo.items():
            # we already saw the alternative version and decided, skip ...
            if word.capitalize() in result or word.lower() in result:
                continue
            
            # this is a capitalized version, choose the more frequent one
            if  word != word.lower() and word.lower() in histo:
                if cnt > histo[word.lower()]:
                    result[word] = cnt + histo[word.lower()]
                else:
                    result[word.lower()] = cnt + histo[word.lower()]
            else:
                result[word] = cnt
        
        return result
    
    # If a word and its plural are both in the histo take only the more frequent one.
    # For example, {test:4 tests:5} --> {tests:9}
    #
    def deplural(self, histo):
        result = Histogram()
        
        for word, cnt in histo.items():
            # we already decided on an alternative version, so drop this one ...
            if word+'s' in result or word[:-1] in result:
                continue
            
            # if this is plural and there is a singular version around, 
            # add the one with higher count
            if word[-1] == 's' and word[:-1] in histo:
                if cnt > histo[word[:-1]]:
                    keep = word
                else:
                    keep = word[:-1]
                    
                result[keep] = cnt + histo[word[:-1]]
            else:
                # the version is unique, keep it.
                result[word] = cnt
        
        return result
