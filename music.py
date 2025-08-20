# -*- coding: utf-8 -*-
import time
import random
from pynput import mouse, keyboard

content2 = ['/music play 我们的歌', '/music play 我们的歌', '/music play 我们的歌']


# contentLength = len(content))
# print(len(content))
# contentLength = 505
contentLength = 3

def main():

    time.sleep(5)
    my_mouse = mouse.Controller()  # 创建鼠标
    my_keyboard = keyboard.Controller()  # 创建键盘
    # m_mouse.positoin = (850,670)#将鼠标移动到指定位置
    my_mouse.click(mouse.Button.left)  # 点击鼠标左键
    steadyNum = random.randint(0, contentLength)  # 计数
    count = 0

    while True:  # 无线循环
        count += 1

        # my_keyboard.type(f'你好呀~{count}')  # 需要发送的文字
        text = content2[(count + steadyNum) % contentLength]
        my_keyboard.type(f'{text}')  # 需要发送的文字
        time.sleep(random.randint(3, 5))
        my_keyboard.press(keyboard.Key.enter)  # 按回车enter
        my_keyboard.release(keyboard.Key.enter)  # 松开回车enter

        print('Msg: ' + text + ' Num: ' + f'{count}')

        # waitSecond = random.randint(60,70)

        time.sleep(1)

        # print(f"剩余时间（秒）: ")

        # lineBreak = 1

        # while waitSecond >= 0:
        #     # 在这里你可以做其他事情，比如检查某个条件来决定是否提前结束睡眠
        #     print(f"{waitSecond}" + ".", end ='')
        #
        #     if lineBreak % 10 == 0 :
        #         print("/n")
        #
        #     waitSecond -= 1
        #     lineBreak += 1
        #     time.sleep(1)  # 设定秒数

        # if count >= 10:  # 设定自动停止时间
            # break
    pass


if __name__ == '__main__':
    main()


