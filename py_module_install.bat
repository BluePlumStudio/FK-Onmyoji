@echo off

python -m pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple

for %%i in (pyautogui, opencv-python, keyboard, pywin32) do (
	pip install %%i -i https://pypi.tuna.tsinghua.edu.cn/simple
	echo %%i安装完成。
	echo:
)

@rem Python3.7以上不兼容win32gui
@rem pip install win32gui -i https://pypi.tuna.tsinghua.edu.cn/simple
echo 安装完毕。按任意键继续。
pause