# xuexiqiangguo
超级简单的解放双手的学习强国脚本，旨在不用手动操作就可以方便学习，提高学习效率，妈妈再也不用担心我的学习～

### 1.准备
1.安装adb
- Windows用户下载[adb](https://pan.baidu.com/s/16EpQvsGX19L9b6vZwRx7Aw)资源，安装教程自行百度。
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
- 安装中...
### 2.运行
#### 手机用户
- 通过数据线让手机与电脑连接
- 在当前目录下打开adb服务
```
adb start-server
```
- 运行脚本
```
python study.py
```
#### Android模拟器用户
- 通过adb连接模拟器，其中7555为mumu模拟器默认端口号，[各模拟器默认端口号](https://www.cnblogs.com/HakunaMatata-/p/10609307.html)
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
