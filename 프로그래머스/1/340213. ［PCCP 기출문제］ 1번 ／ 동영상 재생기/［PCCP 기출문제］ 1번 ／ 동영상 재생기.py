def time_to_sec(time):
    min, sec = map(int, time.split(":"))
    return min*60+sec

def sec_to_time(time):
    min = time // 60
    sec = time % 60
    return f"{min:02d}:{sec:02d}"

def solution(video_len, pos, op_start, op_end, commands):
    backup_pos = time_to_sec(pos)
    video_len_sec = time_to_sec(video_len)
    op_start_sec = time_to_sec(op_start)
    op_end_sec = time_to_sec(op_end)
    
    for command in commands:
        if op_start_sec <= backup_pos <= op_end_sec:
            backup_pos = op_end_sec
            
        if command == "prev":
            if backup_pos < 10:
                backup_pos = 0
            else:
                backup_pos -= 10
        elif command == "next":
            backup_pos += 10
            if backup_pos > video_len_sec:
                backup_pos = video_len_sec
            elif op_start_sec <= backup_pos <= op_end_sec:
                    backup_pos = op_end_sec
    
        if op_start_sec <= backup_pos <= op_end_sec:
            backup_pos = op_end_sec

    answer = sec_to_time(backup_pos)

    return answer

print(solution("34:33", "13:00", "00:55", "02:55", ["next", "prev"]))
print(solution("10:55", "00:05", "00:15", "06:55", ["prev", "next", "next"]))
print(solution("07:22", "04:05", "00:15", "04:07", ["next"]))

