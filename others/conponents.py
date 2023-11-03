from datetime import datetime
from zhconv import convert

def is_all_chinese(strs):
    """判断是否全部中文"""
    if strs:
        for i in strs:
            if not "\u4e00" <= i <= "\u9fa5":
                return False
        return True
    return False

def is_all_eng(strs):
    """判断字符串是否全部英文"""
    if strs:
        import string

        for i in strs:
            if i not in string.ascii_lowercase + string.ascii_uppercase:
                return False
        return True
    return False

def remove_special_characters(str):
    """替换｜为、，防止出现bug"""
    return str.replace(r"|", "、")

def timestamp():
    """时间戳"""
    now = datetime.now()
    return now.strftime("%Y%m%d_%H%M%S")

def write_log(log):
    """日志"""
    with open("brand_match_log.txt", "a+", encoding="utf-8") as f:
        f.write(timestamp() + ', ' + log)

