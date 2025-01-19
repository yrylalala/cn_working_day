#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from calendra.asia import China
from datetime import timedelta, date
import json
import logging

from calendra.exceptions import CalendarError

# 在这里设置记录的是什么等级以上的日志
logging.basicConfig(filename='run.log', format='%(asctime)s - %(name)s - %(levelname)s -%(module)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S', level=20)

if __name__ == "__main__":
    cal = China()
    cur = date.today() - timedelta(days=3)
    res = {}
    for i in range(16):
        cur += timedelta(days=1)
        try:
            res[str(cur)] = cal.is_working_day(cur)
        except CalendarError:
            logging.exception("CalendarError", exc_info=True)
            break
    with open('cn.json', 'w') as json_file:
        json.dump(res, json_file, indent=4, sort_keys=True)
