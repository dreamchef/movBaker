import os

# Iterate through files in folder and check for .mov extension
for filename in os.listdir(os.path.dirname(os.path.realpath(__file__))):
  if filename.endswith(".mov"):
    # separate file name and extension
    base = os.path.splitext(filename)[0]
    # change extension
    os.rename(filename, base + ".m4v")
