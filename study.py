
# coding: utf-8

# In[1]:


from uiautomator import device as driver
import numpy as np
import time
import os
import sys


# In[2]:


ip=None
Height=1280
Width=720
all_of_list=[]
if os.path.isfile("db.npy"):
    all_of_list = np.load ("db.npy").tolist()


# In[3]:


def autoJob(tv,sleep_time):
    count=0
    drag_str='adb shell input swipe '+str(Width*0.5)+' '+str(Height*0.88)+' '+str(Width*0.5)+' '+str(Height*0.3)
    for _ in range(100):
        for d_text in driver(className='android.widget.TextView'):
            txt=d_text.text
            if len(txt)>11 and txt not in all_of_list and count<6:
                count=count+1
                all_of_list.append(txt)
                print("正在"+tv+"...",txt)
                driver(text=txt,className='android.widget.TextView').click()
                time.sleep(sleep_time)
                driver.press.back()
        if count >=6:
            break
        os.system(drag_str)


# In[4]:


#阅读文章,阅读6个文章，每个文章停留125秒
def read_articles():
    time.sleep(5)
    #切换到要闻界面
    driver(text='要闻').click()
    autoJob("阅读文章",130)
    print("阅读文章结束")


# In[5]:


#观看视频,每个视频观看12秒，以及17分钟新闻联盟
def watch_video():
    time.sleep(2)
    #切换到电视台页面
    driver(resourceId="cn.xuexi.android:id/home_bottom_tab_button_contact").click()
    driver(text="联播频道").click()
    autoJob("观看视频",15)
    driver(text="联播频道").click()
    
    news=None
    for v in driver(className='android.widget.TextView'):
        if "新闻联播" in v.text:
            news=v.text
            break
    driver(text=news).click()

    #存储已看视频和文章
    text_list = np.array (all_of_list)
    np.save ('db.npy',text_list)
    
    print("正在观看新闻联播...")
    time.sleep(1100)
    driver.press('back')
    print("观看视频结束.")


# In[6]:


if __name__ == '__main__':
    #自动打开学习强国
    #os.system('adb shell am start cn.xuexi.android/com.alibaba.android.rimet.biz.SplashActivity')
    #屏幕高度
    Height=driver.info['displayHeight']
    Width=driver.info['displayWidth']

    read_articles()
    watch_video()
    driver.press('back')
    #熄灭屏幕
    os.system('adb shell input keyevent 26')

