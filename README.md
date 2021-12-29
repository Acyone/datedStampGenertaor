# datedStampGenertaor
A python tool using PIL to generate PNGs of scanned stamps, for multiple dates.
# Purpose
This tool's objective is to solve a problem by automating a manual task.

In the context of signing digital documents, a stamp must be applied. This can be done digitally from an image from software such as ABBYY finereader.
To make this image (PNG with transparency) this is the workflow :
- Apply the stamp to a piece of paper
- Scan the paper in high resolution
- Open the resulting image in Photoshop
- Mask the background to make it transparent
- Crop the image to only have the stamp
- Save as PNG

When then is a dated stamp, whith a changeable date within the stamp impression, it means every date must be converted to a digital PNG individually. This is time consuming.

# What this tool does
Using PIL, this tool picks from a previously scanned collection of images to combine them into a realistic looking stamp.
The stamp is separated in parts:

- Outside ring
- Day
- Month
- Year

The tool iterates through every date and generates, then saves the corresponding stamp.
It picks from different variations of every eement to make a unique stamp each time.

# Weaknesses

This tool generates impossible dates (such as 31 february)
This tool needs to be supplied with a lot of input data (approx 2h work in photoshop)
This tool does not use OOP
