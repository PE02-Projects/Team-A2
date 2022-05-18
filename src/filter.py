import glob

LMZ_files = glob.glob('dat/**/*LMZ?.xml', recursive=True)
# Save the path to all LMZC and LMZO files in list format.