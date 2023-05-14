# -----------------------------------------------------------------------------
# Copyright (c) 2022, Lucid Vision Labs, Inc.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
# -----------------------------------------------------------------------------

from arena_api.system import system
from arena_api.buffer import *

import ctypes
import numpy as np
import cv2
import time
from arena_api.__future__.save import Writer
'''
Live Stream: Introduction
    This example introduces the basics of running a live stream 
    from a single device. This includes creating a device, selecting
    up stream dimensions, getting buffer cpointer data, creating an
    array of the data and reshaping it to fit image dimensions using
    NumPy and displaying using OpenCV-Python.
'''


def create_devices_with_tries():
	'''
	This function waits for the user to connect a device before raising
		an exception
	'''

	tries = 0
	tries_max = 6
	sleep_time_secs = 10
	while tries < tries_max:  # Wait for device for 60 seconds
		devices = system.create_device()
		if not devices:
			print(
				f'Try {tries+1} of {tries_max}: waiting for {sleep_time_secs} '
				f'secs for a device to be connected!')
			for sec_count in range(sleep_time_secs):
				time.sleep(1)
				print(f'{sec_count + 1 } seconds passed ',
					'.' * sec_count, end='\r')
			tries += 1
		else:
			print(f'Created {len(devices)} device(s)')
			return devices
	else:
		raise Exception(f'No device found! Please connect a device and run '
						f'the example again.')


def setup(device):
    """
    Setup stream dimensions and stream nodemap
        num_channels changes based on the PixelFormat
        Mono 8 would has 1 channel, RGB8 has 3 channels

    """
    nodemap = device.nodemap
    nodes = nodemap.get_node(['Width', 'Height', 'PixelFormat'])

    nodes['Width'].value = 1280
    nodes['Height'].value = 720
    nodes['PixelFormat'].value = 'RGB8'

    num_channels = 3

    # Stream nodemap
    tl_stream_nodemap = device.tl_stream_nodemap

    tl_stream_nodemap["StreamBufferHandlingMode"].value = "NewestOnly"
    tl_stream_nodemap['StreamAutoNegotiatePacketSize'].value = True
    tl_stream_nodemap['StreamPacketResendEnable'].value = True

    return num_channels


def main_frame_aquisition():

    devices = create_devices_with_tries()
    device = devices[0]

    # Setup
    num_channels = setup(device)

    curr_frame_time = 0
    prev_frame_time = 0
    FILE_NAME_PATTERN = "Images/py_save_file_name_pattern/image_yyMMdd_hhmmss_fff>.bmp"
    writer = Writer()

    '''
    Must register tags with writer before including them in pattern
        Must include a generator function
    '''

    print("Set file name pattern")
    writer.pattern = FILE_NAME_PATTERN


    with device.start_stream():
        """
        Infinitely fetch and display buffer data until esc is pressed
        """
        while True:
            # Used to display FPS on stream
            curr_frame_time = time.time()

            # 'Device.get_buffer()' with no arguments returns only one buffer
            print('\tGet one buffer')
            buffer = device.get_buffer()

            # Print some info about the image in the buffer
            print(f'\t\tbuffer received   | '
                f'Width = {buffer.width} pxl, '
                f'Height = {buffer.height} pxl, '
                f'Pixel Format = {buffer.pixel_format.name}')

            writer.save(buffer)

            # Requeue the image buffer
            device.requeue_buffer(buffer)
            fps = str(1/(curr_frame_time - prev_frame_time))

            """
            Destroy the copied item to prevent memory leaks
            """
            prev_frame_time = curr_frame_time
                    

if __name__ == '__main__':
	print('\nWARNING:\nTHIS EXAMPLE MIGHT CHANGE THE DEVICE(S) SETTINGS!')
	print('\nExample started\n')
	main_frame_aquisition()
