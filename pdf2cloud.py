#! /usr/bin/env python

import sys
from os.path import join, dirname
from core.main import PDFClouder

PROJ_PATH = dirname(__file__)

if len(sys.argv) > 1:
    pdf = sys.argv[1]
else:
    pdf = join(PROJ_PATH, 'examples', 'SRC-Wilhelm.pdf')
    pdf = '/Users/mwilhelm/Desktop/nessa.pdf'
    #pdf = '/Users/mwilhelm/Desktop/capacity_wireless.pdf'
    #pdf = '/Users/mwilhelm/Desktop/MobiCom_2012/mobicom/p17.pdf'
    
pdfc = PDFClouder(pdf)
result = pdfc.get_histo(refs=True)
result.flatten(min_cnt=3)
