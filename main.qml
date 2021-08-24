// Library import requires a specific version. Or QML files can't be opened by Design of Qt Creator.
import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Window 2.15

ApplicationWindow {
	visible: true

	visibility: "Maximized"
	title: qsTr("写作助手")
	
	menuBar: MenuBar {
		Menu {
			title: qsTr("文件")
		}
		Menu {
			title: qsTr("帮助")
			MenuItem {
				text: qsTr("使用说明")
			}
			MenuSeparator {}
			MenuItem {
				text: qsTr("关于")
			}
		}
	}
	
	TabBar {
		property int dwTabButtonNum: 4
		
		width: parent.width
		
		TabButton {
			text: qsTr("词库")
			width: Math.min(64, parent.width / parent.dwTabButtonNum)
		}
		
		TabButton {
			text: qsTr("摘抄管理")
			width: Math.min(64, parent.width / parent.dwTabButtonNum)
		}
		
		TabButton {
			text: qsTr("写作提示")
			width: Math.min(64, parent.width / parent.dwTabButtonNum)
		}
		
		TabButton {
			text: qsTr("备份恢复")
			width: Math.min(64, parent.width / parent.dwTabButtonNum)
		}
	}
}
