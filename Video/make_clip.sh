# 비디오 클립 자르기 
# -ss : 시작 시간 
# -t : duration (sec)
ffmpeg -y -loglevel info -ss 0 -t 5 -i Demo_Trim.mp4 data_dst.mp4
