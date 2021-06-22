import globals
import lexical
import semantic
import sys

from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QObject, Signal, Slot
from Ui_MainWindow import Ui_MainWindow


class MainWindow(Ui_MainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.setupUi(self)
		self.show()


app = None
gui = None

if __name__ == '__main__':
	app = QApplication(sys.argv)
	gui = MainWindow()
	
	print(lexical.get_synonyms("美丽", 32))
	print(lexical.get_synonyms("帅", 32))
	
	text = """既然跟他一样正值青年时期的蒋志飞主动提出要在傍晚带自己去那个他所说的实打实的好地方，按照直觉和经验判断，那里多半跟这个词有着紧密联系。段立光以前算是个宅男，不论是放学后的晚上还是周末都不大喜欢出去。但足不出户不一定会限制人的遐想。每当段立光写完作业，静静地倚在窗边，用那时的单纯的眼光望向这座城市的绚烂夜景，他总会感觉全城的建筑都在向他招手，引诱他在大街小巷穿梭，令自己融于都市提供的欢乐与美好。他躺在床上准备入睡之前，常常望着天花板或窗户，想象着自己在夜幕之下独自背着运动背包踏出家门，开着一辆跑车或者重机，行驶于这座国际化大都市。立交桥网络仿佛通向各个浪漫的星际景点的传送门。他在大桥之间高速奔驰，用余光欣赏着两侧不断退后的车流。他也会在中心商业区不停地打转，以一个与世无争的过客的身份，观赏着人来人往。想停下的时候，他就把车停在路旁，亲身混入人群中，通过亲自观察猜测他们可能的奋斗目标，感受他们对理想的热情。江边有个生意还算不错的酒吧，不过现在管得紧了，严格禁止未成年人进入。他没有喝酒的习惯，不过他想象到这里的时候，还是希望能买支酒，在江边慢慢把酒注入江水里，让身心迷醉在这豁然之中，细品那几句流传已久的诗歌：
	"我有一壶酒，足以慰风尘。尽倾江海里，赠饮天下人。"
	如果能有人跟自己搭话，那再好不过。自己可以倚在江畔的围栏上，在无尽的人流中保持静止，在皓月之下与来人畅谈校园、游戏、小说和未来。末了，他便欣然上车，让车辆自如地释放一下轰鸣，而后有力地加速离去。"""
	
	print(lexical.tokenize(text))
	
	print(semantic.get_keywords(text, 16))
	print(semantic.get_summary(text))
	print(semantic.get_sentiment(text))
	
	sys.exit(app.exec_())
