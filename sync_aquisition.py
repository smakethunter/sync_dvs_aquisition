from ast import main
import signal
from time import time
from metavision_aquisition import main_dvs_aquisition
from arena_sdk_stream_aquisition import main_frame_aquisition
from multiprocessing import Process, Pool
import os
import time
import argparse

def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description='Metavision RAW file Recorder sample.',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        '-d', '--dvs_dir', default="", help="Directory where to create RAW file with recorded event data")

    parser.add_argument(
        '-f', '--frames_dir', default="", help="Directory where to write recorded frames")
    args = parser.parse_args()
    return args

class SigtermException(Exception):
    pass

def sigterm_handler(signum, frame):
    raise SigtermException('sigterm')

def sync_aquisition():
    args = parse_args()

    signal.signal(signal.SIGTERM, sigterm_handler)
    with Pool(2) as pool:
        async_result_dvs = pool.apply_async(main_dvs_aquisition, (args.dvs_dir,))
        async_result_frames = pool.apply_async(main_frame_aquisition, (args.frames_dir,))
    async_result_dvs.get()
    async_result_frames.get()


if __name__ == "__main__":
    sync_aquisition()
    


