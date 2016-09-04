#!/usr/bin/env python
# -*- coding:utf-8 -*-
# filename: tail.py
__author__ = 'Jason tom'

'''
功能：实现 Linux 下的 tail -f 功能.

基本思路：
   打开文件，指针移动到最后，每隔 0.3 秒 readline 一次，有内容就打印出来，没有内容就继续 sleep.

默认打印 10 行的思路：
   1、假设日志中每一行的长度都是 100 个字符；注意，这只是个假设，代码会根据实际情况自动修改.
   2、默认读取最后 10 行；所以一开始就 seek 到文件末尾倒数 1000 个字符的位置(seek(-1000, 2))，
      并读取这 1000 个字符，再做判断.
   3、判断如果 1000 个字符长度大于文件总的长度，那么直接 read，然后按换行符进行 split 取最后
      10 个.
   4、如果 1000 个字符里面的换行符大于 10，说明这 1000 个字符中至少包含了 10 行内容，
      那么也是直接 read 这 1000 个字符，然后按换行符 split 取最后 10 个.
   5、如果这 1000 个字符中没有 10 个换行符，那么你应该读取这 1000 个字符并判断这 1000 个字符
      中有多少个换行符，假设有 3 个换行符，那么 1000//3 == 333，则每行有 333 个字符，10 行就
      是 333 * 10 == 3330 个字符，之后，再从文件末尾处开始读取 3330 个字符，再判断这 3330 个
      字符中有没有 10 个换行符，如果有，则直接 read，然后按换行符 split 取后 10 个；如果没有
      ，则继续读取判断，直到换行符数量大于 10 则读取结束.

'''
import sys
import time

class Tail:
    def __init__(self, filename):
        self.filename = filename

    def follow(self, n=10):
        # n += 1 表示当以换行符 \n 进行 split 的时候，list 最后会多出一个空元素；代码后面的 last_line.pop()
        # 就是去掉这个空元素，而加一是为了满足默认读取 10 行的这个要求.
        n += 1
        try:
            # 以 rb 模式打开文件，以便支持二进制文件的读取，否者会抛出 io.UnsupportedOperation 异常
            with open(self.filename, 'rb+') as f:
                self._file = f
                self._file.seek(0, 2)
                self.file_length = self._file.tell()
                self.__showlastline(n)
                while True:
                    # 解码二进制文件内容
                    line = self._file.readline().decode()
                    if line:
                        print(line, end='')
                    time.sleep(0.3)
        # except io.UnsupportedOperation as e:
        #     print(e, 'Please use rb+ mode open file.')
        except FileNotFoundError as e:
            print(e)
        except KeyboardInterrupt as e:
            print()
    
    # n 代表默认读取文件前十行
    def __showlastline(self, n):
        # 假设文件中每行长度为 100 个字符，
        line_len = 100
        read_line = line_len * n
        while True:
            if read_line > self.file_length:
                self._file.seek(0)
                last_line = self._file.read().decode().split('\n')[-n:]
                break
            self._file.seek(-read_line, 2)
            last_word = self._file.read(read_line).decode()
            count_enter = last_word.count('\n')
            if count_enter >= n:
                last_line = last_word.split('\n')[-n:]
                break
            else:
                if count_enter == 0:
                    read_line *= n
                else:
                    read_line = (read_line // count_enter) * n
        last_line.pop()
        for line in last_line:
            print(line)


if __name__ == '__main__':
    py_tail = Tail(sys.argv[1])
    py_tail.follow()
