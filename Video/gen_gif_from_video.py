import os 
import os.path as osp
import shutil

import cv2 
import numpy as np 
import moviepy.editor as mpy


def frame_extraction(video_path):
    """Extract frames given video_path.

    Args:
        video_path (str): The video_path.
    """
    # Load the video, extract frames into ./tmp/video_name
    target_dir = osp.join('./tmp', osp.basename(osp.splitext(video_path)[0]))
    os.makedirs(target_dir, exist_ok=True)
    # Should be able to handle videos up to several hours
    frame_tmpl = osp.join(target_dir, 'img_{:06d}.jpg')
    vid = cv2.VideoCapture(video_path)
    frames = []
    frame_paths = []
    flag, frame = vid.read()
    cnt = 0

    while flag:
        frames.append(frame)
        frame_path = frame_tmpl.format(cnt + 1)
        frame_paths.append(frame_path)

        cv2.imwrite(frame_path, frame)
        cnt += 1
        flag, frame = vid.read()

    return frame_paths, frames



if __name__ == "__main__":
    video_path = "demo_trim.mp4"

    # ----------------------------------- #
    # == Extract frames from the video == # 
    # ----------------------------------- #
    frame_paths, original_frames = frame_extraction(video_path)
    num_frame = len(frame_paths)
    h, w, _ = original_frames[0].shape

    # --------------------------- #
    # == Visualize the results == #
    # --------------------------- #
    vid = mpy.ImageSequenceClip([x[:, :, ::-1] for x in original_frames], fps=24)
    vid.write_gif(f"./result.gif")


    tmp_frame_dir = osp.dirname(frame_paths[0])
    shutil.rmtree(tmp_frame_dir)
