import sys
import pandas as pd
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import threading

table_name = sys.argv[1]
input_video_file = sys.argv[2]

df = pd.read_excel(table_name, header=None)

def process_row(row):
    start_time = row.values[0]
    end_time = row.values[1]
    output_name = f"{row.values[2]}.mp4"

    try:
        ffmpeg_extract_subclip(input_video_file, start_time, end_time, targetname=output_name)
        print(f"Video clip {output_name} has been successfully created.")
    except Exception as e:
        print(f"Error creating video clip {output_name}: {e}")

for _, row in df.iterrows():
    threading.Thread(target=process_row, args=(row,)).start()



