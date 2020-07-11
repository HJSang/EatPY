from pytube import YouTube
import os
from absl import app
from absl import flags

FLAGS = flags.FLAGS

flags.DEFINE_string('url',None,'The url link for the youtube video')
flags.DEFINE_string('name', None, 'The Youtube nmae')

def download():
    # url 
    video = YouTube(FLAGS.url)
    print(video.streams.all())
    dest_dir = '/Users/hejiansang/Downloads/youtube/'
    video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(output_path=dest_dir,filename=FLAGS.name)

def main(_):
    download()

if __name__ == '__main__':
  app.run(main)
