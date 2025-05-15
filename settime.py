lddir = 'C:/leidian/' # 要以/或\\结尾，不可省略





import os

def set_simulator_time(index, year, month, day, hour, minute, second):
    """
    设置雷电模拟器的系统时间
    :param index: 模拟器的索引号（从0开始）
    :param year: 年份（如2025）
    :param month: 月份（如5）
    :param day: 日期（如15）
    :param hour: 小时（如10）
    :param minute: 分钟（如30）
    :param second: 秒（如0）
    """
    # 构造日期时间字符串，格式为 MMDDHHMMYY.SS
    datetime_str = f"{month:02d}{day:02d}{hour:02d}{minute:02d}{year % 100:02d}.{second:02d}"
    
    # 构造 adb 命令，使用 date 命令设置系统时间
    adb_command = lddir + f'ldconsole adb --index {index} --command "shell su -c \'date {datetime_str}\'"'
    
    # 执行命令
    result = os.popen(adb_command).read()
    print(result)

# 示例：设置索引为0的模拟器的时间为2025年5月15日10时30分0秒
