'''
Created on 01.09.2012

@author: Matthias Wilhelm
@email: mwilhelm.kl@gmail.com
'''

from ..histo.histogram import Histogram

class Decap(object):
    def __init__(self):
        pass
    
    def decap(self, histo):
        result = Histogram()
        
        for word, cnt in histo.items():
            if word.lower() in histo and word not in result:
                if cnt > histo[word.lower()]:
                    result[word] = cnt
                else:
                    result[word.lower()] = histo[word.lower()]
        
        return result