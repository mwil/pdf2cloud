'''
Created on 31.08.2012

@author: Matthias Wilhelm
@email: mwilhelm.kl@gmail.com
'''

from os.path import join, dirname

RESOURCE_PATH = join(dirname(__file__), '..', 'resources')

class WordFilter(object):
    def __init__(self):
        with open(join(RESOURCE_PATH, 'common.txt'), 'r') as fd:
            self.common = set([word.strip() for word in fd.readlines()])
        with open(join(RESOURCE_PATH, 'paper.txt'), 'r') as fd:
            self.paper = set([word.strip() for word in fd.readlines()])
        with open(join(RESOURCE_PATH, 'verbs.txt'), 'r') as fd:
            self.verbs = set([word.strip() for word in fd.readlines()])
            
            
    def filter(self, words):
        res_words = []
        
        for word in words:
            if len(word) == 1:
                continue
            
            if word.lower() in self.common:
                continue
            if word.lower() in self.paper:
                continue
            if word.lower() in self.verbs:
                continue
            
            # FIXME this deletes some wanted strings like 802.15.4 or similar
            if not word[0].isalpha() or word[-1].isdigit():
                continue
                #print word.encode('utf-8')
            
            res_words.append(word)
        
        return res_words

if __name__ == '__main__':
    wf = WordFilter()
    
    print " ".join(wf.common)
    
        
        