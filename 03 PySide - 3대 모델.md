# Pyside 클래스

`QtWidgets`, `QtGui` 와 `QtCore`  크게 3가지 모델을 대표적으로 많이 사용한다.

그 외 아래와 같이 다양하게 존재한다.

```python
__pre_all__ = ["QtCore", "QtGui", "QtWidgets", "QtPrintSupport", "QtSql", "QtNetwork", "QtTest", "QtConcurrent", "QtDBus", "QtDesigner", "QtXml", "QtHelp", "QtMultimedia", "QtMultimediaWidgets", "QtOpenGL", "QtOpenGLWidgets", "QtPdf", "QtPdfWidgets", "QtPositioning", "QtLocation", "QtNetworkAuth", "QtNfc", "QtQml", "QtQuick", "QtQuick3D", "QtQuickControls2", "QtQuickTest", "QtQuickWidgets", "QtRemoteObjects", "QtScxml", "QtSensors", "QtSerialPort", "QtSerialBus", "QtStateMachine", "QtTextToSpeech", "QtCharts", "QtSpatialAudio", "QtSvg", "QtSvgWidgets", "QtDataVisualization", "QtGraphs", "QtGraphsWidgets", "QtBluetooth", "QtUiTools", "QtAxContainer", "QtWebChannel", "QtWebEngineCore", "QtWebEngineWidgets", "QtWebEngineQuick", "QtWebSockets", "QtHttpServer", "QtWebView", "Qt3DCore", "Qt3DRender", "Qt3DInput", "Qt3DLogic", "Qt3DAnimation", "Qt3DExtras"]
```





## 01 QtCore

Qt의 내부 시스템 기능을 제공.

특징:

- 메모리 관리, 스레드 관리, 네트워킹, 파일 시스템 접근 등 Qt의 핵심 기능을 제공
- Qt를 사용하는 모든 어플리케이션에서 필요한 기본 기능을 제공
- 이벤트 처리, 시스템 정보, 타이머 등의 기능을 제공





## 02 QtGui

기본적인 그래픽 기능을 제공.

특징:

- pixel, color, brush, 펜 등 기본적인 그래픽 요소를 다루는 기능을 제공합니다.
- 2D 그래픽, 이미지 처리, 폰트 관리 등의 기능을 제공합니다.
- Qt에서 제공하는 모든 그래픽 기능에 대한 기반을 제공합니다.





## 03 QtWidgets

역할: 사용자 인터페이스 위젯을 제공.

특징:

- 버튼, 라벨, 텍스트 편집기, 스크롤바 등 다양한 위젯을 제공
- 위젯을 사용하여 다양한 사용자 인터페이스를 구축
- Qt에서 제공하는 대부분의 위젯을 포함



---



### 1. `QWidget` class

Qt 에서 비어있는 기본 Widget 을 위한 Class.

- 일반적으로 관련있는 widgets를 포함하여 묶어주는 container 로 많이 사용됨.
- GUI Components (=Widgets) 이 공유하는 기본 기능들을 가지고 있음.
- Widgets가 공통적으로 가져야하는 기능 을 `QtWidget` Class에 abstraction시켜 놓음.
- 즉, Widget의 abstraction이라고 생각하면 된다.

GUI의 기본 구성요소인 [Widget](https://wikidocs.net/189238)을 추상화하고 있는 Class.

> 참고 : [추상화(abstraction) 란](https://dsaint31.me/mkdocs_site/python/oop/oop_1_01_abstraction/#abstraction-class-and-instance)

---

- `show()` :
  해당 Widget의 인스턴스를 화면에 보이게 하는 method.
- `setGeometry(left_x,left_y,widht,height)` :
  해당 Widget의 인스턴스의 위치와 크기를 설정하는 method.
- `setWindowTitle("title_str")` :
  해당 Widget의 윈도우의 titlebar text(문자열)을 설정하는 method.
- `close()` :
  해당 Widget의 윈도우를 닫음.

---





### 2. `QApplication` class

Qt 의 GUI Application을 추상화하고 있는 Class

- 이 클래스의 instance가 GUI Application에 해당함. 
- 해당 Application의 interaction을 처리하는 event loop 를 유지함.
  - 오직 하나의 `QApplication` instance만 생성되어야 하며,
  - 해당 instance의 `exec()` 메서드 호출을 통해 해당 GUI application 의 오직 하나뿐이 `Qt (Main) Event Loop` 가 수행된다.

* `QApplication` Class는
  - ***사용자와 OS와의 interaction(상호작용)을 위한 처리(=Event Loop)\*** 를 구현하고 있고,
  - 대응하는 GUI application 에 속한 Widgets의 ***초기화\*** 및 ***해제\*** 등을 담당함.
  - 일종의 Qt Application Handler라고 생각할 수 있음.

---









