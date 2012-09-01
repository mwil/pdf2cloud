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
    
    def dedup(self, histo):
        result = self.decap(histo)
        result = self.deplural(result)
        
        return result
    
    #######################################################
    
    def decap(self, histo):
        result = Histogram()
        
        for word, cnt in histo.items():
            if word.capitalize() in result or word.lower() in result:
                continue
            
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
    def deplural(self, histo):
        result = Histogram()
        
        for word, cnt in histo.items():
            if word+'s' in result or word[:-1] in result:
                continue
            
            if word[-1] == 's' and word[:-1] in histo:
                if cnt > histo[word[:-1]]:
                    result[word] = cnt + histo[word[:-1]]
                else:
                    result[word[:-1]] = cnt + histo[word[:-1]]
            else:
                result[word] = cnt
        
        return result
