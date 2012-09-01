#! /usr/bin/env python

import sys
from core.main import PDFClouder

if len(sys.argv) > 1:
    pdf = sys.argv[1]
else:
    pdf = 'examples/SRC-Wilhelm.pdf'
    #pdf = '/Users/mwilhelm/Desktop/nessa.pdf'
    #pdf = '/Users/mwilhelm/Desktop/MobiCom_2012/mobicom/p89.pdf'
    
pdfc = PDFClouder(pdf)
result = pdfc.get_histo()
result.flatten()
