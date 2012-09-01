'''
Created on 31.08.2012

@author: Matthias Wilhelm
@email: mwilhelm.kl@gmail.com
'''

from StringIO import StringIO

from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams

class PDFExtractor(object):
    def __init__(self, pdf):
        self.pdf = pdf
    
    # returns a list of 'words,' a sequence of letters with whitespace in-between.    
    def get_words(self, cleanup=True):
        rsrcmgr = PDFResourceManager()
        raw_words = StringIO()
        device = TextConverter(rsrcmgr, raw_words, codec='utf-8', laparams=LAParams())

        with file(self.pdf, 'rb') as fp:
            process_pdf(rsrcmgr, device, fp, set(), maxpages=0, password='')

        device.close()
        
        raw_words = raw_words.getvalue().decode('utf-8')
        words = self.split_n_merge(raw_words)
            
        if cleanup:
            words = self.cleanup_words(words)
             
        return words
    
    def cleanup_words(self, words):
        clean_words = []
        
        for word in words:
            word = self.replace_unicode(word)
            word = self.zap_punctuation(word)
            
            if word:
                clean_words.append(word)
            
        return clean_words
    
    def split_n_merge(self, raw_words):
        splitters = [u'\u2212', u'\u2014' ]
        
        # Extract single words from one long raw string
        words = []
        for word in raw_words.split():
            word = word.strip(u'.,:;()"\u201d\u201c')
            
            if word:
                results = [word]
            else:
                continue
            
            for splitter in splitters:
                if word.find(splitter) > 0:
                    results = word.split(splitter)

            words.extend(results)
        
        # de-hyphen the text, just glue together words that end in '-'
        res_words = []
        hyph = None
        
        for word in words:
            if not word:
                continue
            
            if hyph:
                word = hyph + word
                hyph = None
            
            if word[-1] == '-':
                hyph = word[:-1]
                continue
            
            if not word.isalpha() and word.find('-') == -1:
                continue
            
            res_words.append(word)
            
        return res_words
    
    def replace_unicode(self, word):
        lig_map = {u'\ufb01':'fi', u'\ufb02':'fl', u'\ufb00':'ff', u'\ufb03':'ffi',
                   u'\u2019':"'", u'\u2013':'-', 
                   u'\u201d':'"', u'\u201c':'"'}
        
        for lig, repl in lig_map.items():
            word = word.replace(lig, repl)
        
        return word
        
    def zap_punctuation(self, word):
        if word and word[0] == '[' or word[-1] == ']':
            word = None
        
        if word and len(word) == 1 and not word.isalpha():
            word = None
            
        if word and word.isdigit():
            word = None
            
        return word

if __name__ == '__main__':
    pdfex = PDFExtractor('/Users/mwilhelm/Desktop/nessa.pdf')
    
    words = pdfex.get_words()
    
    print(words)