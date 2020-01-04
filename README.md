# xuexiqiangguo
超级简单的解放双手的学习强国脚本，旨在提高学习效率，妈妈再也不用担心我的学习～

### 1.准备
1.安装adb
- Windows用户下载[adb资源](https://pan.baidu.com/s/16EpQvsGX19L9b6vZwRx7Aw)，安装教程自行百度。
- deepin用户
```
sudo apt-get install adb
```
2.安装依赖包
```
pip install uiautomator
```
```
pip install numpy
```
3. 安装Python
- 安装中(^_^)...
### 2.运行
切换至项目目录，手机或者模拟器需在运行python脚本前自己打开学习强国。
#### 手机用户
- 打开手机的开发者模式，开启手机调试功能并允许通过adb安装应用，通过数据线让手机与电脑连接。本程序基于uiautomator编写，所以第一次会在手机安装两个应用，需要用户手动点击同意安装。
```
adb start-server
```
- 运行脚本
```
python study.py
```
#### Android模拟器用户
- 通过adb连接模拟器，其中7555为mumu模拟器默认端口号，可以参考这篇文章[各模拟器默认端口号](https://www.cnblogs.com/HakunaMatata-/p/10609307.html)
```
adb connect 127.0.0.1:7555
```
- 运行脚本
```
python study.py
```
### 3.问题
如果抛出异常，试试kill掉adb，重启试试。
### 4.后续
目前是看文章和视频，有24分，后续可能加入收藏，分享，评论，关注等功能，敬请关注。
