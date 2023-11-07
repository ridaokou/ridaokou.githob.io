import sys  # 系统内置类
from PyQt5.Qt import *  # 主要包含了我们常用的一些类，汇总到了一块

if __name__ == '__main__':
	# 创建一个应用程序对象
	app = QApplication(sys.argv)
	# 创建一个空白控件(窗口)
	window = QWidget()
	# 设置窗口标题
	window.setWindowTitle("监视器窗口")
	# 设置窗口尺寸
	window.resize(500, 500)
	# 移动窗口位置
	window.move(200, 200)
	# 创建label控件
	label = QLabel(window)
	# 为控件设置文本
	label.setText("hello")
	# 移动控件的位置
	label.move(160, 160)
	# 显示窗口
	window.show()
	# 进入程序的主循环，并通过exit函数确保主循环安全结束
	sys.exit(app.exec_())


