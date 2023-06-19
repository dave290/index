OVERVIEW 
The Python scripts index.py and meta_index.py create scatterplots showing GLONG vs GLAT for observing sessions.
The .kel files are formatted according to NsfIntegrate data collection software for radio astronomy.

index.py
place .kel (or .ast files) into a subfolder labelled "data" (Be sure to delete the file named "Delete_this_file")
Creates a single index file (.ind) that lists GLONG, GLAT, RA and DEC values for every .kel file.
Creates a scatterplot of GLAT vs GLONG for a single observing session

meta_index.py
reads the .ind files that reside in the "data" subfolder.
Creates a scatterplot of GLAT vs GLONG overlaying all of your observing sessions.

seek.py
reads a collection of index files and displays kel file names for values of galactic
longitude and latitude falling within a requested range.
