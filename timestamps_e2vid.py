import datetime
import os
import argparse
# "image_yyMMdd_hhmmss_fff"
def get_dvs_file_start_timestamp(filename):
    return datetime.datetime.strptime(filename.split('.')[0], "%Y%m%d_%H%M%S").timestamp()
def get_frame_timestamp(filename):
    return datetime.datetime.strptime(filename.split('.')[0], 'image_%Y%m%d_%H%M%S_%f').timestamp()
def get_timestamp_for_frame(frame_timestamp, dvs_start_timestamp):
    print(dvs_start_timestamp)
    print(frame_timestamp)
    return int((dvs_start_timestamp - frame_timestamp)*1e6)

def get_frame_timestamps(dvs_filename, images_dir):
    start_timestamp = get_dvs_file_start_timestamp(dvs_filename)
    timestamps = [f"{get_timestamp_for_frame(start_timestamp, get_frame_timestamp(image))}\n" for image in os.listdir(images_dir)]
    timestamps.sort(reverse=False)
    return timestamps

def write_timestamps(timestamps, timestamps_file):
    with open(timestamps_file, "w") as f:
        f.writelines(timestamps)

if __name__ == "__main__":
    parser = argparse.ArgumentParser('Obtains frame timestaps in microseconds with respect to .raw file aquisition time')
    parser.add_argument('input_files_dir', help='Path to files to get timestamps of.')
    parser.add_argument('--output_file', '-o', default="", help='Output path for h5 file. Default: Input path but with h5 suffix.')
    parser.add_argument('--dvs_filename', '-d', default='dvs', help='Filemame of dvs to get starting_point')

    args = parser.parse_args()
    frame_filename = args.output_file # "image_20230508_120420_603.bmp"
    dvs_filename = args.dvs_filemane #"20230508_120419.raw"
    frame_dir = args.input_files_dir #"dir"
    write_timestamps(get_frame_timestamps(dvs_filename, frame_dir))
