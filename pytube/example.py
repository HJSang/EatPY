from pytube import YouTube
import os
import shutil
import math
import datetime
import matplotlib.pyplot as plt
# import cv2

# url 
url = 'https://www.youtube.com/watch?v=ZaqLGNdhi7g'
video = YouTube(url)
print(video.streams.all())
#dir = '/Downloads/youtube/'
#print(os.listdir(dir))
video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
