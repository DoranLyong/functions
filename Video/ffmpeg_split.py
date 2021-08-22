import sys 
import os 
import os.path as osp 

import numpy as np 
import pandas as pd 
import subprocess   # (ref) https://wikidocs.net/14350
                    # (ref) https://newsight.tistory.com/354





def read_xlxData(Path:str) -> pd.core.frame.DataFrame: 
    df = pd.read_excel(Path, index_col = 0 )
    df = df.dropna(axis=0)  # drop rows(axis=0) including NaN

    return df 





def video_split(data_dir, subject_num):
    sbjDir_path = osp.join(data_dir, subject_num)

    items = os.listdir(sbjDir_path)

    if not len(items)==3:
        print(f"skip @ {subject_num}")
        return 

    
    # =================== #
    #      Read Files     #
    # =================== #
    nameVideo = f"{subject_num}.mp4"
    anno_global_name = f"{subject_num}_semi_global.xlsx"
    anno_indiv_name = f"{subject_num}_semi_indiv.xlsx"


    
    df_anno_global = read_xlxData(osp.join(sbjDir_path, anno_global_name))
    df_anno_indiv = read_xlxData(osp.join(sbjDir_path, anno_indiv_name))


    g_shape = df_anno_global.shape
    i_shape = df_anno_indiv.shape
    

    if not (g_shape == i_shape):
        print(f"wrong annotation @ {subject_num}")
        return 


    # ==================== # 
    #    Get parameters    # 
    # ==================== # 
    num_instance, _ = g_shape

    start_mins = df_anno_global["Start_min"].to_numpy()  # video times 
    start_secs = df_anno_global["Start_sec"].to_numpy()
    end_mins = df_anno_global["End_min"].to_numpy()
    end_secs = df_anno_global["End_sec"].to_numpy()

    motions = df_anno_global["Motion"].to_numpy()

    g_features = df_anno_global["Global_feature"].to_numpy()
    i_features = df_anno_indiv ["Indiv_feature"].to_numpy()



    # ==================== # 
    # FFmpeg section split # 
    # ==================== # 
    # (ref) https://wikidocs.net/90002

    video_filePath = osp.join(sbjDir_path,  nameVideo)  # video where to be? 

    videoName_list = []
    

    for i in range(num_instance):
        start_min, start_sec = map(int, [start_mins[i].item(), start_secs[i].item()])
        end_min, end_sec = map(int, [end_mins[i].item(), end_secs[i].item()])


        cmd = f"ffmpeg -i {video_filePath} -ss 00:{start_min:02d}:{start_sec:02d} -to 00:{end_min:02d}:{end_sec:02d} -c copy {sbjDir_path}/{subject_num}_s{i+1:04d}.mp4"
        videoName_list.append(f"{subject_num}_s{i+1:04d}")
        
        os.system(cmd)


    os.system(f"rm -rf {video_filePath}") # remove the original 
    os.system(f"rm -rf {osp.join(sbjDir_path, anno_global_name)}")
    os.system(f"rm -rf {osp.join(sbjDir_path, anno_indiv_name)}")



    videoName_array = np.array(videoName_list)

    # ==================== # 
    #  new annotation file #  
    # ==================== # 
    # (ref) https://datatofish.com/numpy-array-to-pandas-dataframe/
    # (ref) https://stackoverflow.com/questions/45399950/how-to-create-a-pandas-dataframe-with-several-numpy-1d-arrays

    column_names = ["name", "indiv_feature", "global_feature", "motion"]

    concate = pd.DataFrame( np.hstack((videoName_array.reshape(-1,1), i_features.reshape(-1,1), g_features.reshape(-1,1), motions.reshape(-1,1))),    
                            columns = column_names, 
                            )

    new_annoName = f"{sbjDir_path}/{subject_num}_anno.csv"
    concate.to_csv(new_annoName , index=False)








if __name__ == '__main__':


    data_dir = 'process'   # ???_jpg_data 
    subject_list = sorted(os.listdir(data_dir))


    for subject_num in subject_list:
        video_split(data_dir, subject_num)
    
