"""import multiprocessing as mp
import time


def main(url, num):
    print('開始執行', url)
    time.sleep(2)
    print('結束', num)

if __name__ == '__main__': 

    url_list1 = ['www.yahoo.com.tw, www.google.com']
    url_list2 = ['www.yahoo.com.tw, www.google.com']
    url_list3 = ['www.yahoo.com.tw, www.google.com']

    # 定義線程
    p_list = []
    p1 = mp.Process(target=main, args=(url_list1, 2))
    p_list.append(p1)

    p2 = mp.Process(target=main, args=(url_list2, 2))
    p_list.append(p2)

    p3 = mp.Process(target=main, args=(url_list3, 2))
    p_list.append(p3)

    # 開始工作
    for p in p_list:
        p.start()

    # 調整多程順序
    for p in p_list:
        p.join()"""


import multiprocessing as mp
import os


class Dosomething:
    def __init__(self):
        self.p_list = []

    def dosomething(self, i):
        print('第' + str(i))
        print('多程序 ID:' + str(os.getpid()))

    def run(self):
        for i in range(5):
            self.p_list.append(
            mp.Process(target=self.dosomething, args=(str(i))))
            self.p_list[i].start()

        for i in self.p_list:
            i.join()


if __name__ == "__main__":
    d = Dosomething()
    d.run()