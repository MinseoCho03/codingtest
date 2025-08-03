def solution(video_len, pos, op_start, op_end, commands):
    def time_to_sec(t):
        m, s = map(int, t.split(":"))
        return m * 60 + s

    def sec_to_time(sec):
        m, s = divmod(sec, 60)
        return f"{m:02}:{s:02}"

    video_len_sec = time_to_sec(video_len)
    pos_sec = time_to_sec(pos)
    op_start_sec = time_to_sec(op_start)
    op_end_sec = time_to_sec(op_end)

    for cmd in commands:
        # 1. 오프닝 구간이면 op_end로 이동
        if op_start_sec <= pos_sec <= op_end_sec:
            pos_sec = op_end_sec

        # 2. 명령어 수행
        if cmd == "prev":
            pos_sec = max(0, pos_sec - 10)
        elif cmd == "next":
            pos_sec = min(video_len_sec, pos_sec + 10)

    # 명령 끝난 후에도 오프닝에 있다면 건너뛰기
    if op_start_sec <= pos_sec <= op_end_sec:
        pos_sec = op_end_sec

    return sec_to_time(pos_sec)
