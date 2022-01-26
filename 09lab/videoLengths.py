def read_file():
    video_file = open ('video_times.txt')
    return video_file

def print_videos(video_file):
    video_list = []
    for line in video_file:
             run_time = float(line)
             video_list.append (run_time)
             print ('Video #', ':', run_time)
    return(video_list)

def sum_videos(video_list):
    sum_vid = 0
    for i in range(len(video_list)):
            sum_vid = sum_vid + video_list[i]
    print ('the total is ', sum_vid)

#main
sum_videos(print_videos(read_file()))
