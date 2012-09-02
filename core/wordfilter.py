'''
Created on 31.08.2012

@author: Matthias Wilhelm
@email: mwilhelm.kl@gmail.com
'''

from os.path import join, dirname

from histogram import Histogram

RESOURCE_PATH = join(dirname(__file__), '..', 'resources')

class WordFilter(object):
    def __init__(self):
        with open(join(RESOURCE_PATH, 'common.txt'), 'r') as fd:
            self.common = set([word.strip() for word in fd.readlines()])
        with open(join(RESOURCE_PATH, 'paper.txt'), 'r') as fd:
            self.paper = set([word.strip() for word in fd.readlines()])
        with open(join(RESOURCE_PATH, 'verbs.txt'), 'r') as fd:
            self.verbs = set([word.strip() for word in fd.readlines()])
     
    #####################################################      
            
    def cleanup(self, words):
        res_words = []
        
        histo = Histogram(words)
        
        for word in words:
            word = self.filter(word)
            if word:
                word = self.decap(word, histo)
            if word:
                word = self.deplural(word, histo)             
            
            res_words.append(word)
                
        return res_words
    
    #####################################################
    
    # Remove strings that are obviously bad, e.g., appear in the most common words
    #
    def filter(self, word):
        if len(word) == 1:
            return ''
        for wdict in [self.common, self.paper, self.verbs]:
            if word.lower() in wdict:
                return ''
            
        # FIXME this deletes some wanted strings like 802.15.4 or similar
        if not word[0].isalpha() or word[-1].isdigit():
            return ''
            
        return word
    
    
    #######################################################
    
    # Find the most frequent word in terms of capitalization
    #
    def decap(self, word, histo):
        lword = word.lower()
        cword = word.capitalize()
        
        # There are at least two capitalized characters, prob.ly an abbreviation
        if word != lword and word != cword:
            return word
        
        if lword in histo and cword in histo:
            if histo[lword] > histo[cword]:
                return lword
            else:
                return cword
        else:
            return word
    
    # Find the most frequent word in terms of number
    #
    def deplural(self, word, histo):
        if word[-1] == 's':
            sg_word = word[:-1]
            pl_word = word
        else:
            sg_word = word
            pl_word = word+'s'
        
        if sg_word in histo and pl_word in histo:
            if histo[sg_word] > histo[pl_word]:
                return sg_word
            else:
                return pl_word
        else:
            return word
        