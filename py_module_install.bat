@echo off

python -m pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple

for %%i in (pyautogui, opencv-python, keyboard, pywin32) do (
	pip install %%i -i https://pypi.tuna.tsinghua.edu.cn/simple
	echo %%i��װ��ɡ�
	echo:
)

@rem Python3.7���ϲ�����win32gui
@rem pip install win32gui -i https://pypi.tuna.tsinghua.edu.cn/simple
echo ��װ��ϡ��������������
pause