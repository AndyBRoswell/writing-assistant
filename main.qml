// Library import requires a specific version. Or QML files can't be opened by Design of Qt Creator.
import QtQuick 2.15
import QtQuick.Layouts 1.12
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
		id: tabMain
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
	StackLayout {
		width: parent.width
		y: tabMain.height
		height: parent.height - tabMain.height
		currentIndex: tabMain.currentIndex
		
		Item {
			id: tabLexica
			width: parent.width
			height: parent.height
			
			SplitView {
				anchors.fill: parent
				
				Item {
					SplitView.preferredWidth: parent.width * 1 / 4
					
					TextField {
						id: tfDictName
						width: parent.width
						placeholderText: qsTr("搜索：词典名称")
					}
					TextArea {
						y: tfDictName.height
						width: parent.width
						height: parent.height - tfDictName.height
					}
				}
				Item {
					TextField {
						id: tfKeyword
						width: parent.width
						placeholderText: qsTr("输入：要查询的词语、短语或句子")
					}
					SplitView {
						orientation: Qt.Vertical
						anchors.top: tfKeyword.bottom
						anchors.bottom: parent.bottom
						anchors.left: parent.left
						anchors.right: parent.right
						
						Item {
							SplitView.preferredHeight: parent.height * 1 / 2
							TextArea {
								anchors.fill: parent
							}
						}
						Item {
							SplitView {
								anchors.fill: parent
								
								Item {
									SplitView.preferredWidth: parent.width * 1 / 8
									
									ListModel {
										id: lmLibs
										ListElement {
											name: "synonyms"
										}
									}
									ListView {
										anchors.fill: parent
										model: lmLibs
										delegate: Row {
											CheckBox { checked: true }
											Text { text: name }
										}
									}
								}
								Item {
									TextArea {
										anchors.fill: parent
									}
								}
							}
						}
					}
				}
			}
		}
		Item {
			id: tabExcerpts
			width: parent.width
			height: parent.height
			
			Text {
				text: "Excerpts"
			}
		}
		Item {
			id: tabWritingHints
			width: parent.width
			height: parent.height
			
			Text {
				text: "WritingHints"
			}
		}
		Item {
			id: tabBackupAndRestore
			width: parent.width
			height: parent.height
			
			Text {
				text: "BackupAndRestore"
			}
		}
	}
}
