import time

def focus_timer(minutes):
    seconds = minutes * 60
    end_time = time.time() + seconds

    print(f"专注倒计时开始，将持续 {minutes} 分钟。")

    while time.time() < end_time:
        remaining_seconds = int(end_time - time.time())
        minutes = remaining_seconds // 60
        seconds = remaining_seconds % 60
        time_format = f"{minutes:02d}:{seconds:02d}"
        print(f"剩余时间：{time_format}", end="\r")
        time.sleep(1)

    print("\n专注时间结束！")

# 设置专注时间为25分钟
minutes = int(input("输入专注时间:"))
focus_timer(minutes)
