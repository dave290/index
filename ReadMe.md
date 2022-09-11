Purpose: The Python scripts index.py and meta_index.py create scatterplots showing GLONG vs GLAT for observing sessions.
The .kel files are formatted according to NsfIntegrate data collection software for radio astronomy.

index.py
place .kel (or .ast files) into a subfolder labelled "data" (Be sure to delete the file named "Delete_this_file")

Creates a single index file (.ind) that lists GLONG, GLAT, RA and DEC values for every .kel file.
Place this file into the folder labelled "index_archive"

Creates a scatterplot of GLAT vs GLONG for a single observing session

meta_index.py
reads the .ind files that reside in the "index_archive" folder.
Creates a scatterplot of GLAT vs GLONG overlaying all of your observing sessions.
