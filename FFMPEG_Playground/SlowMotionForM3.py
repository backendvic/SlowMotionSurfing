ffmpeg -i "SeaBass75.mp4" -t 6 -c copy -bsf:a aac_adtstoasc SeaBass75_1.mp4

ffmpeg -i "SeaBass75.mp4" -ss 00:00:06 -t 2 -strict -2 SeaBass75_2.mp4

ffmpeg -i "SeaBass75.mp4" -ss 00:00:08 -strict -2 SeaBass75_3.mp4

ffmpeg -i SeaBass75_2.mp4 -filter:v "setpts=5.0*PTS" -strict -2 SeaBass75_slow.mp4

ffmpeg -i SeaBass75_1.mp4 -c copy -bsf:v h264_mp4toannexb -f mpegts Bass1.ts

ffmpeg -i SeaBass75_slow.mp4 -c copy -bsf:v h264_mp4toannexb -f mpegts Bass2.ts

ffmpeg -i SeaBass75_3.mp4 -c copy -bsf:v h264_mp4toannexb -f mpegts Bass3.ts

ffmpeg -i "concat:Bass1.ts|Bass2.ts" -c copy -bsf:a aac_adtstoasc BassBS_.mp4

ffmpeg -i BassBS_.mp4 -c copy -bsf:v h264_mp4toannexb -f mpegts Bass4.ts

ffmpeg -i "concat:Bass4.ts|Bass3.ts" -c copy -bsf:a aac_adtstoasc BassFinal.mp4

ffmpeg -i "concat:Bass1.ts|Bass2.ts|Bass3.ts" -c copy -bsf:a aac_adtstoasc Bass3in1.mp4

#Can we skip the entire cutting process and go straight to saving it into a '.ts' file? need to create a loop that will run ffmpeg command necessary amount of times. (dependent upon time markers). 
