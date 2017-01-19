#!/usr/bin/env python
# -*- coding:utf-8 -*-

name = 'songshouli'
chinese_name = "宋守立"
age = 18
grade1 = 68
grade2 = 96

print('name is %s, chinese_name is %s, chinese_name len is %d, chinese_name len byte is %d' % (name, chinese_name, len(chinese_name), len(chinese_name.encode('utf-8'))))
print('age is %s\n' % age)
print('grade is %d, promote %.1f%%' % (grade2, ((grade2-grade1)/grade1*100))) 
