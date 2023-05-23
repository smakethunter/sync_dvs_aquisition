import argparse
import cv2
import yaml
from calib import parse_calibration_settings_file, \
    calibrate_camera_for_intrinsic_parameters

if __name__ == '__main__':
    parser = argparse.ArgumentParser('Obtains frame timestaps in microseconds with respect to .raw file aquisition time')
    parser.add_argument('--yaml_file', '-f', help='Yaml file for globals', default='calibration_settings.yaml')
    args = parser.parse_args()
    with open(args.yaml_file) as f:
        calibration_settings = yaml.safe_load(f)
    # Open and parse the settings file

    """Step1. Save calibration frames for single cameras"""
    # save_frames_single_camera('camera0') #save frames for camera0
    # save_frames_single_camera('camera1') #save frames for camera1


    """Step2. Obtain camera intrinsic matrices and save them"""
    # camera0 intrinsics
    # images_prefix_global_shutter = ""
    cmtx0, dist0 = calibrate_camera_for_intrinsic_parameters(calibration_settings['images_prefix_global_shutter'], calibration_settings)
    print(cmtx0, dist0)
    # save_camera_intrinsics(cmtx0, dist0, 'camera0')  # this will write cmtx and dist to disk
    # #camera1 intrinsics