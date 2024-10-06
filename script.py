from subprocess import Popen, PIPE
from PIL import Image
import requests
import climage
import os
import time
import shutil
from termcolor import colored

scp3 = '''
on run
    tell application "Spotify"
		set songTitle to the name of the current track
		set songArtist to the artist of the current track
		set songAlbum to the album of the current track
        set artworkUrl to artwork url of current Track
		set result to songArtist & "%-%" & songTitle & "%-%" & songAlbum & "%-%" & artworkUrl
		if player state is playing then
			return result
		else
			return "None" & "%-%" & "None" & "%-%" & "None"
		end if
	end tell
end run
'''


def run_script(script):
	p = Popen(['osascript', '-'], stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True)
	stdout, stderr = p.communicate(scp3)
	if 'None' in stdout or stdout == '':
		return None, None, None, 0, 0, 0, 0
	else:
		elements = stdout.split(sep='%-%')
		artist, title, album = elements[0], elements[1], elements[2]
		url = elements[3][:-1]
		im = Image.open(requests.get(url, stream=True).raw).convert('RGB')
		width, height = shutil.get_terminal_size(fallback=(80, 24))
		return im, url, height, width, artist, title, album

def clear():
	os.system('clear')

cur_url = ''
old_width = 0
old_height = 0
while True:
	image, new_url, h, w, artist, title, album = run_script(scp3)
	
	if image is None:
		clear()
		print('No song playing')
		cur_url = ''
		#time.sleep(1)
	else:
		len_text = len(f'{artist} - {title} - {album}')
		mid_screen = w//2
		pre_spacing = ' '*(w-(mid_screen + len_text//2))
		text = colored(f'{artist} - {title} - {album}', 'green', 'on_black', attrs=['bold', 'underline'])
		if new_url != cur_url:
			clear()
			im_w = min(h,w)
			output = climage.convert_pil(image, is_unicode=True, width=im_w)
			print(output)
			cur_url = new_url
			print(pre_spacing+text)
			#print(text)
			#time.sleep(0.5)
		if w != old_width or h != old_height:
			clear()
			im_w = min(h,w)
			output = climage.convert_pil(image, is_unicode=True, width=im_w)
			print(output)
			old_width = w
			old_height = h
			print(pre_spacing+text)
			#print(text)
			#time.sleep(0.5)
