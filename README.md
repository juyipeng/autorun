# 项目介绍
本项目源自于[Autorun](https://github.com/cwlm/SJTU_AutoRun)，该项目实现了自动刷校园跑，但是没有修改系统时间实现多次跑步的功能，经过修改后无需多次操作，便可直接一次性刷完80km任务

# 使用方法
## 环境准备
本项目基于autorun项目，需要在电脑中下载雷电模拟器9，并配置交我办：
- 安装 [雷电模拟器9](https://www.ldmnq.com/)
- 在其中安装 `交我办3.4.3`(安装包在项目文件里有)
- 登录Jaccount

python环境：
- [安装 Python](https://zhuanlan.zhihu.com/p/111168324) , 推荐安装 [Python3.11](https://www.python.org/downloads/release/python-3119/).
- 如果已经有python，可以跳过上一步操作，如果已经有conda，可以自行配置相应环境，后续不做赘述
- 在命令行中输入以下内容安装项目包：
```sh
pip install -U sjtuautorun
```
## 运行
在命令行中执行以下步骤，直接运行main.py即可：
```sh
cd /project_path/ # /project_path/ 将/project_path/改为本项目的目录
```
然后输入
```sh
python main.py
```
运行程序即可

## 个性化运行
考虑到可能有跑了一部分的情况，可以打开`交我办-智慧体育-运动健康-跑步记录-跑步记录`查看自己没有跑的周数，在`calculate_dates.py`文件里修改最上面runweeks数组的周数（记得周数要-1，例如我只需要跑第1，2周就改成[0,1]），然后运行即可