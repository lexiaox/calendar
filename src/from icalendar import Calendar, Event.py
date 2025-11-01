from icalendar import Calendar, Event
import datetime
import pytz

# ===== 参数设定 =====
semester_start_single = datetime.date(2025, 10, 13)  # 单周起始
semester_start_double = semester_start_single + datetime.timedelta(days=7)  # 双周起始
tz = pytz.timezone("Asia/Shanghai")

# ======= 你的作息表（略） =======
# 这里填你的 single_week 和 double_week 内容不变
~~~
格式类似于
single_week = {
    "周一": [
        (0.0, 7.5, "睡眠"),
        (7.5, 8.1667, "起床/洗漱/通勤"),
        (8.5, 12.1667, "程序设计基础Ⅰ · 天山堂 A414"),
        (12.1667, 12.5, "午餐"),
        (12.5167, 12.9167, "午睡"),
        (14.5, 18.1667, "思想道德与法治 · 天山堂 B501"),
        (18.1667, 18.6667, "晚餐"),
        (19.0, 20.6667, "体育（1/4） · 东区运动场"),
        (21.0, 21.5, "跑步"),
        (21.5, 22.0, "洗澡"),
        (22.0, 23.5, "自习/复习"),
    ],
    "周二": [

    ],
    "周三": [

    ],
    "周四": [

    ],
    "周五": [

    ],
    "周六": [

    ],
    "周日": [

    ],
}

double_week = {
    "周一": [

    ],
    "周二": [

    ],
    "周三": [

    ],
    "周四": [

    ],
    "周五": [

    ],
    "周六": [

    ],
    "周日": [

    ],
}
~~~
# ===== 辅助函数：创建 Event =====
def make_event(start_date, day_offset, start_h, end_h, desc):
    ev = Event()
    date = start_date + datetime.timedelta(days=day_offset)
    # 处理跨午夜情况
    if end_h >= start_h:
        dtstart = datetime.datetime(date.year, date.month, date.day,
                                    int(start_h), int((start_h - int(start_h)) * 60),
                                    tzinfo=tz)
        dtend   = datetime.datetime(date.year, date.month, date.day,
                                    int(end_h), int((end_h - int(end_h)) * 60),
                                    tzinfo=tz)
    else:
        # 跨午夜
        dtstart = datetime.datetime(date.year, date.month, date.day,
                                    int(start_h), int((start_h - int(start_h)) * 60),
                                    tzinfo=tz)
        next_day = date + datetime.timedelta(days=1)
        dtend = datetime.datetime(next_day.year, next_day.month, next_day.day,
                                  int(end_h), int((end_h - int(end_h)) * 60),
                                  tzinfo=tz)
    ev.add("dtstart", dtstart)
    ev.add("dtend", dtend)
    ev.add("summary", desc)
    return ev

# ===== 主生成 ICS 的函数 =====
def generate_ics(filename, schedule, start_date, is_repeat=True):
    cal = Calendar()
    cal.add("prodid", "-//LZU 作息表//")
    cal.add("version", "2.0")

    wkmap = {"周一":0, "周二":1, "周三":2, "周四":3, "周五":4, "周六":5, "周日":6}

    for dayname, evs in schedule.items():
        offset = wkmap[dayname]
        evs_sorted = sorted(evs, key=lambda t: t[0])
        filled = []
        filled.append(evs_sorted[0])
        for i in range(1, len(evs_sorted)):
            prev = evs_sorted[i-1]
            curr = evs_sorted[i]
            if curr[0] - prev[1] >= 0.5:
                filled.append((prev[1], curr[0], "自习"))
            filled.append(curr)
        for (st, en, desc) in filled:
            ev = make_event(start_date, offset, st, en, desc)
            if is_repeat:
                ev.add("rrule", {"freq": "weekly", "interval": 2})
            cal.add_component(ev)

    with open(filename, "wb") as f:
        f.write(cal.to_ical())
    print("✅ 已生成:", filename)

# ===== 执行部分 =====
if __name__ == "__main__":
    generate_ics("单周作息.ics", single_week, semester_start_single, True)
    generate_ics("双周作息.ics", double_week, semester_start_double, True)
