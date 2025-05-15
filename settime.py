# import os
# import time

# def set_time(index, year, month, day, hour, minute, second):
#     """
#     设置模拟器的系统时间
#     :param index: 模拟器序号
#     :param year: 年
#     :param month: 月
#     :param day: 日
#     :param hour: 时
#     :param minute: 分
#     :param second: 秒
#     :return: 命令执行结果
#     """
#     # 构造日期时间字符串，格式为 YYYY-MM-DD HH:MM:SS
#     datetime_str = f"{year}-{month}-{day} {hour}:{minute}:{second}"
#     # 构造命令，使用 adb shell date 命令设置时间
#     cmd = f'date --set "{datetime_str}"'
#     # 通过 ldconsole.exe 向模拟器发送 adb 命令
#     return os.popen(f'E:\\Programmes\\leidian\\LDPlayer9\\ldconsole.exe run --index {index} --command "{cmd}"').read()

# # 示例：设置第 1 个模拟器的时间为 2025 年 5 月 15 日 10 点 30 分 0 秒
# print(set_time(0, 2025, 3, 4, 12, 30, 0))


# import os
# import time

# def set_simulator_time(index, year, month, day, hour, minute, second):
#     """
#     设置雷电模拟器的系统时间
#     :param index: 模拟器的索引号（从0开始）
#     :param year: 年份
#     :param month: 月份
#     :param day: 日期
#     :param hour: 小时
#     :param minute: 分钟
#     :param second: 秒
#     """
#     # 构造日期时间字符串，格式为 YYYY-MM-DD HH:MM:SS
#     datetime_str = f"{year}-{month}-{day} {hour}:{minute}:{second}"
    
#     # 构造 adb 命令，使用 date 命令设置系统时间
#     # 注意：需要使用 su 提升权限来设置系统时间
#     adb_command = f'E:\\Programmes\\leidian\\LDPlayer9\\ldconsole adb --index {index} --command "shell su -c \'date \\"{datetime_str}\\"\'"'
    
#     # 执行命令
#     result = os.popen(adb_command).read()
#     print(result)

# # 示例：设置索引为0的模拟器的时间为2025年5月15日10时30分0秒
# set_simulator_time(0, 2025, 5, 15, 10, 30, 0)



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
    adb_command = f'E:\\Programmes\\leidian\\LDPlayer9\\ldconsole adb --index {index} --command "shell su -c \'date {datetime_str}\'"'
    
    # 执行命令
    result = os.popen(adb_command).read()
    print(result)

# 示例：设置索引为0的模拟器的时间为2025年5月15日10时30分0秒
