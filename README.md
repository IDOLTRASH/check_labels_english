# nnsvslabeling
Python scripts I made to make NNSVS labeling easier.

# How to Use
### General
You will need Python for all of these to work, of course. I wrote this in Python 3.7.

### check_labels.py

It's exactly what the file says. It checks for wrong phonemes in every .lab file that it finds. It also checks if you have a label that has the same start and end timing. To run, put it in the folder where you keep your .lab files and just, run normally!

It checks Japanese labels by default, but if you want to change what language it checks, just open it up and change the `phones` list to the phoneme list you want it to be.
