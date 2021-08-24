#include <QGuiApplication>
#include <QQmlApplicationEngine>

#include <QLocale>
#include <QTranslator>

int main(int argc, char *argv[]) {
#if QT_VERSION < QT_VERSION_CHECK(6, 0, 0)
	QCoreApplication::setAttribute(Qt::AA_EnableHighDpiScaling);
#endif
	
	QGuiApplication App(argc, argv);
	
	QTranslator Translator;
	const QStringList UILanguages = QLocale::system().uiLanguages();
	for (const QString& Locale : UILanguages) {
		const QString BaseName = "writing-assistant_" + QLocale(Locale).name();
		if (Translator.load(":/i18n/" + BaseName)) {
			App.installTranslator(&Translator);
			break;
		}
	}
	
	QQmlApplicationEngine Engine;
	const QUrl URL(QStringLiteral("qrc:/main.qml"));
	QObject::connect(&Engine, &QQmlApplicationEngine::objectCreated, &App,
					 [URL](QObject *Obj, const QUrl &ObjURL) {
		if (!Obj && URL == ObjURL) QCoreApplication::exit(-1);
	}, Qt::QueuedConnection);
	Engine.load(URL);
	
	return App.exec();
}
