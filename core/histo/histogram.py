'''
Created on 01.09.2012

@author: Matthias Wilhelm
@email: mwilhelm.kl@gmail.com
'''

from collections import defaultdict
from operator import itemgetter

class Histogram(defaultdict):
    def __init__(self, words=[]):
        super(Histogram, self).__init__(int)
        
        for word in words:
            self[word] += 1
        
    def __repr__(self):
        data = sorted(self.iteritems(), key=itemgetter(1), reverse=True)
        return '\n'.join(['%s: %i' % (word, cnt) for word, cnt in data if cnt > 1])
    
    def flatten(self):
        for word, cnt in self.items():
            if cnt > 1:
                print ' '.join([word.encode('utf-8') for word in [word]*cnt]),