
Purpose: The Python scripts index.py and meta_index.py create scatterplots showing GLONG vs GLAT for observing sessions.
The .kel files are formatted according to NsfIntegrate data collection software for radio astronomy.

If you're using index.py, then into the Data folder go:
...the .kel files that you processed using the T program, 

Index.py will then create a single index file (.ind) that lists
GLONG, GLAT, RA and DEC values for every .kel file.

It will also create a scatterplot of GLAT vs GLONG for a single 
observing session


OR, if you're using meta_index.py, then into the Data folder go:
...the index files from multiple data collections

meta_index.py will create a scatterplot of GLAT vs GLONG overlaying all 
of your observing sessions.
