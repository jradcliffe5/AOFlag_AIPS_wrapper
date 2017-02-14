# This is the external python script to convert from measurement sets to fits files
# Only to be used with the AOFlag_module
import os, sys

print sys.argv

if sys.argv[3] == 'fits':
	importuvfits(fitsfile=sys.argv[4], vis=sys.argv[4][:-4]+'ms')

if sys.argv[3] == 'ms':
	exportuvfits(vis=sys.argv[4], fitsfile=sys.argv[4][:-2]+'fits', datacolumn='data', multisource=False, combinespw=True)
