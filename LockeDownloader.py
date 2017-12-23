# A lightweight  mp3 downloader for Python3.
# Takes youtube link as command line argument.
# lots of credit goes to Aman Roy:
# https://github.com/aman-roy/mp3_downloader
# This is a simplified version of their program.
# by locke1 Fri Dec 22 19:44:31 2017

import urllib, os, sys

# setup urllib for p3:
user_input = input
import urllib.request
import urllib.parse
urlopen = urllib.request.urlopen
encode = urllib.parse.urlencode
retrieve = urllib.request.urlretrieve
cleanup = urllib.request.urlcleanup()

# function to retrieve video title from provided link
def video_title(url):
    try:
        webpage = urlopen(url).read()
        title = str(webpage).split('<title>')[1].split('</title>')[0]
    except:
        title = 'Youtube Song'

    return title

def main(url=None):
    try:
        command = 'youtube-dl --embed-thumbnail --no-warnings --extract-audio --audio-format mp3 -o "%(title)s.%(ext)s" ' + sys.argv[1]
        # song=video_title(url)
        try:
            # print('Downloading %s' % song)
            os.system(command)
        except:
            print('Error downloading %s' % song)
    except KeyboardInterrupt:
        print('KeyboardInterrupt. Bye.')
        exit(1)
    except NameError:
        print('NameError. Bye')
        exit(1)
if __name__ == '__main__':
    main()
    exit(0)