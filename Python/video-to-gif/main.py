from moviepy.editor import *


def convert_to_gif(video_file, start_min, start_sec, end_min, end_sec, gif):
    clip = (VideoFileClip(video_file)
            .subclip((start_min, start_sec), (end_min, end_sec))
            .resize(1))
    clip.write_gif(gif)


def get_time(time: str):
    arr = time.split(':')
    return int(arr[0]), int(arr[1])


if __name__ == '__main__':
    video = input('Enter video path: ')
    start_time = input('Enter start time(mm:ss): ')
    end_time = input('Enter end time(mm:ss): ')
    save_as = input('Save gif as(xyz.gif): ')

    start_m, start_s = get_time(start_time)
    end_m, end_s = get_time(end_time)

    convert_to_gif(video, start_m, start_s, end_m, end_s, save_as)
