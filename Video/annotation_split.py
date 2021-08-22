import sys 
import os 
import os.path as osp 
from glob import glob   # (ref) https://wikidocs.net/83
from operator import itemgetter 
from pathlib import Path 

import cv2 
import numpy as np 
import pandas as pd 


""" [Code run]

    # individual feature 에서 band-width를 (-1, 1) 기준으로 쪼개겠다:
    ~$ python annotation_split.py indiv -1 1   
    ~$ python annotation_split.py global -1.5 1.5
"""




#%%
def video_move(subject_num, src_path, idx_dict, video_list):
    

    for key, items in idx_dict.items():

        if len(items) == 0:
            path = Path(osp.join(".", key))
            path.mkdir(parents=True, exist_ok=True)   
            continue


        save_path = osp.join(".", key, subject_num)
        saveDir = Path(save_path)
        saveDir.mkdir(parents=True, exist_ok=True)   

        videoNames = itemgetter(*items)(video_list) # (ref) https://stackoverflow.com/questions/18272160/access-multiple-elements-of-list-knowing-their-index


        for videoName in videoNames:
            src = osp.join(src_path, videoName)

            cap = cv2.VideoCapture(src)  
            frame_num = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) 	# get the total number of frames 


            if frame_num < 29:
                """ skip the video which including less than 29-frame
                """
                continue

#            print(f"fps: {frame_num}")
            cmd = f"cp {src} {save_path}"
            os.system(cmd)


#%%
def read_csv(Path:str) -> pd.core.frame.DataFrame: 
    df = pd.read_csv(Path, index_col = 0 ) # (ref) https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
    df = df.dropna(axis=0)  # drop rows(axis=0) including NaN

    return df



#%%
def split_data(data_dir, subject_num, criteria_feature, *band_width): 


    sbjDir_path = osp.join(data_dir, subject_num)

    csv_path = glob(osp.join(sbjDir_path, "*.csv"))[0]
    video_list = sorted([x for x in os.listdir(sbjDir_path) if x.endswith(".mp4")])  # (ref) https://www.delftstack.com/ko/howto/python/how-to-find-files-with-certain-extension-only-in-python/
    


    # =================== #
    #      Read Files     #
    # =================== #
    df_anno_csv = read_csv(csv_path)



    # ==================== # 
    #    Get parameters    # 
    # ==================== # 
    num_instance, _ = df_anno_csv.shape

    band_min, band_max = band_width


    if criteria_feature == "indiv":
        features = df_anno_csv["indiv_feature"].to_numpy() 

    elif criteria_feature == "global":
        features = df_anno_csv["global_feature"].to_numpy() 


    # ==================== # 
    #        Splits        # 
    # ==================== # 

    total_index = [idx for idx in range(num_instance)]

    negative_attenIdx = np.where(features < band_min)[0].tolist()
    positive_attenIdx = np.where(band_max < features)[0].tolist()

    natural_attenIdx = set(total_index) - set(negative_attenIdx)    # difference set 
    natural_attenIdx = list(set(natural_attenIdx) - set(positive_attenIdx))


    idx_dict = {"not_attention" : negative_attenIdx, 
                "attention" : positive_attenIdx,
                "natural" :  natural_attenIdx, 
                    }

    video_move(subject_num, sbjDir_path, idx_dict, video_list)                        







#%%
if __name__ == '__main__':

    data_dir = 'test'   # data directory
    subject_list = sorted(os.listdir(data_dir))

    criteria_feature = sys.argv[1]  # "indiv" or "global"

    try: 
        band_min, band_max = map(float, (sys.argv[2], sys.argv[3]))

                                # 

        if not (band_min < band_max):
            # (ref) https://dojang.io/mod/page/view.php?id=2400
            raise Exception("'band_min' should be smaller than 'band_max'")


        print(f"criteria_feature: {criteria_feature}")
        print(f"band_width: {band_min},{band_max}")

        for subject_num in subject_list:
            split_data(data_dir, subject_num,  criteria_feature, *[band_min, band_max])


    except Exception as e:
        print(e)
        sys.exit()

    


