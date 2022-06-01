# import required module
import os
import sys

from g_synthesize import synthesize_text

# assign directory
directory = sys.argv[1]

# iterate over files in
# that directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f) and not filename.endswith('DS_Store'):
        g = open(f).read()
        s = synthesize_text(g, filename + ".mp3")
