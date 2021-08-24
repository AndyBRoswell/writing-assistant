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
		width: parent.width
		
		Repeater {
			model: [qsTr(""), qsTr(""), qsTr("")]
			
			
		}
	}
}
