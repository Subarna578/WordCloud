from mypack import calculate_frequencies, upload



import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys
import ipywidgets


upload()  #Uploading the text file



myimage= calculate_frequencies(file_contents)
plt.figure(figsize=(15,15))
plt.imshow(myimage, interpolation= 'nearest')
plt.show()

