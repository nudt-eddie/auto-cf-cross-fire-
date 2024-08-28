
# -*- coding:UTF-8 -*-
def zh_ch(string):
    return string.encode('UTF-8').decode(errors='ignore')
import numpy as np
from PIL import ImageGrab
import cv2
import pythoncom
import time,datetime
from pynput import keyboard
import pydirectinput
keyboard_controller = keyboard.Controller()
def click_left_button():
    # 执行点击鼠标左键的操作
    print("点击鼠标")
    pydirectinput.mouseDown()
    pydirectinput.mouseUp()
def shun():
    import time, datetime
    print("shun!!!!")
    pydirectinput.mouseDown(button="right")
    time.sleep(0.005)
    pydirectinput.mouseDown(button="left")
    time.sleep(0.01)
    pydirectinput.mouseUp(button="right")
    time.sleep(0.05)
    pydirectinput.mouseUp(button="left")
    time.sleep(0.04)
    keyboard_controller.press('3')
    time.sleep(0.04)
    keyboard_controller.release('3')
    time.sleep(0.06)
    keyboard_controller.press('1')
    time.sleep(0.03)
    keyboard_controller.release('1')
    time.sleep(0.02)
    keyboard_controller.press('1')
    time.sleep(0.02)
    keyboard_controller.release('1')

# BOX = (880+100, 670+100, 1030+100, 710+100)
BOX = (1280-75, 650-5, 1280+75, 650+15)


flag = 1
lock = 0
while True:
    import time, datetime
    e1 = cv2.getTickCount()
    screen = np.array(ImageGrab.grab(bbox=BOX))
    imm=cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)
    cv2.imshow("window",imm )
    hsv = cv2.cvtColor(imm, cv2.COLOR_BGR2HSV)
    low_hsv = np.array([0,43,46])
    high_hsv = np.array([10, 255, 255])
    cv2.imshow("windows",hsv )
    mask = cv2.inRange(hsv, lowerb=low_hsv, upperb=high_hsv)
    a = np.asarray(mask)
    # 200 5000
    if  len(a.nonzero()[0])>200 and len(a.nonzero()[0])<2500 and flag == True:
        if lock//3==0:
            print("lock:", lock//3)
            print("click")
            shun()
            # click_left_button()
        elif lock//3==1:
            print("lock:", lock//3)
            print("shun")
            shun()
        elif lock //3 ==2:
            print("lock:", lock//3)
            print("rest")
            break
        time.sleep(1.4)
        e2 = cv2.getTickCount()
        time = (e2 - e1) / cv2.getTickFrequency()
        print((time))
    # if cv2.waitKey(1) & 0xFF == ord("l"):
    #     cv2.destroyAllWindows()
    #     break
    if cv2.waitKey(1) & 0xFF == ord("p"):
        lock +=1
    # if cv2.waitKey(1) & 0xFF == ord("p"):
    #     flag = False
    #     print(flag)
    #     break
    # if cv2.waitKey(1) & 0xFF == ord("o"):
    #     flag = True
    #     print(flag)
    #     break
cv2.waitKey(0)
cv2.destroyAllWindows()









#pydirectinput.moveTo(100, 150) # 移动鼠标至坐标100，150
# pydirectinput.click(200, 220) # 移动鼠标至坐标200，220，并点击左键
# pydirectinput.move(None, 10)  # 鼠标移动相对y位置
# pydirectinput.doubleClick() # 双击鼠标左键
# pydirectinput.press('esc') # 按一下esc
# pydirectinput.keyDown('shift')#按下shift
# pydirectinput.keyUp('shift')#弹起shift




             #  pydirectinput.click()  # 点击鼠标左键
            # m = PyMouse()
            # a = m.position()  # 获取当前坐标的位置(这个东西到时候可以新建个py 获取坐标)
            # #print(a)
            # #m.move(50, 500)  # 鼠标移动到(x,y)位置
            # #a = m.position()
            # print(a)
            # m.click(a[0],a[1])  # 移动并且在(x,y)位置左击
# 鼠标事件处理函数
def OnMouseEvent(event):
  #print('MessageName:',event.MessageName)  #事件名称
  #print('Message:',event.Message)          #windows消息常量
  #print('Time:',event.Time)                #事件发生的时间戳
  #print('Window:',event.Window)            #窗口句柄
  #print('WindowName:',event.WindowName)    #窗口标题
  print('Position:',event.Position)        #事件发生时相对于整个屏幕的坐标
  #print('Wheel:',event.Wheel)              #鼠标滚轮
  print('Injected:',event.Injected)        #判断这个事件是否由程序方式生成，而不是正常的人为触发。
  print('---')

  # 返回True代表将事件继续传给其他句柄，为False则停止传递，即被拦截
  return True

# #键盘事件处理函数
# def OnKeyboardEvent(event):
#   print('MessageName:',event.MessageName)          #同上，共同属性不再赘述
#   print('Message:',event.Message)
#   print('Time:',event.Time)
#   print('Window:',event.Window)
#   print('WindowName:',event.WindowName)
#   print('Ascii:', event.Ascii, chr(event.Ascii))   #按键的ASCII码
#   print('Key:', event.Key)                         #按键的名称
#   print('KeyID:', event.KeyID)                     #按键的虚拟键值
#   print('ScanCode:', event.ScanCode)               #按键扫描码
#   print('Extended:', event.Extended)               #判断是否为增强键盘的扩展键
#   print('Injected:', event.Injected)
#   print('Alt', event.Alt)                          #是某同时按下Alt
#   print('Transition', event.Transition)            #判断转换状态
#   print('---')
#hm.MouseAllButtonsDown = OnMouseEvent #将OnMouseEvent函数绑定到MouseAllButtonsDown事件上
#hm.KeyDown = OnKeyboardEvent   #将OnKeyboardEvent函数绑定到KeyDown事件上

#hm.HookMouse()        #设置鼠标钩子
#hm.HookKeyboard()   #设置键盘钩子
