import tkinter as tk
from tkinter import ttk
from tkinter.constants import *
from typing import Union
import ctypes

from .unit import px2pt


class CnfBooleans:
    NO = FALSE = OFF = FALSE
    YES = TRUE = ON = TRUE


class CnfState:
    NORMAL = 'normal'
    DISABLED = 'disabled'
    ACTIVE = 'active'
    # Canvas state
    HIDDEN = 'hidden'


class CnfAnchor:
    N = N  # 上中方
    S = S  # 下中方
    W = W  # 垂直中左方
    E = E  # 垂直中右方
    NW = NW  # 上左方
    SW = SW  # 下左方
    NE = NE  # 上右方
    SE = SE  # 下右方
    CENTER = CENTER  # 垂直水平居中

    NS = 'ns'
    EW = 'ew'
    NSEW = 'nsew'


CnfSticky = CnfAnchor


class CnfFill:
    NONE = NONE
    X = X
    Y = Y
    BOTH = BOTH


class CnfSide:
    LEFT = LEFT
    TOP = TOP
    RIGHT = RIGHT
    BOTTOM = BOTTOM


CnfFloat = CnfSide


class CnfRelief:
    RAISED = RAISED
    SUNKEN = SUNKEN
    FLAT = FLAT
    RIDGE = RIDGE
    GROOVE = GROOVE
    SOLID = SOLID


class CnfOrient:
    HORIZONTAL = HORIZONTAL
    VERTICAL = VERTICAL


class CnfTabs:
    NUMERIC = NUMERIC


class CnfWrap:
    CHAR = CHAR
    WORD = WORD


class CnfAlign:
    BASELINE = BASELINE


class CnfBordermode:
    INSIDE = INSIDE
    OUTSIDE = OUTSIDE


class CnfMenuType:
    CASCADE = CASCADE
    CHECKBUTTON = CHECKBUTTON
    COMMAND = COMMAND
    RADIOBUTTON = RADIOBUTTON
    SEPARATOR = SEPARATOR


class CnfJustify:
    LEFT = LEFT
    RIGHT = RIGHT
    CENTER = CENTER


class CnfCompound:
    LEFT = LEFT
    RIGHT = RIGHT
    BOTTOM = BOTTOM
    TOP = TOP
    CENTER = CENTER


class CnfCursor:
    POINTER = "hand2"
    MOVE = "fleur"
    TEXT = "xterm"


class ThemeColor:
    primary = "#0170FE"
    danger = "#FF4D4F"
    white = "#FFFFFF"
    black = "#333333"


class WidgetCnfProvider:

    def __init__(self):
        # 前景色
        self.fg = self.foreground = None

        # 背景色
        self.bg = self.background = None

        # 当功能组件获取焦点时背景颜色
        self.highlightbackground = None

        # 当功能组件获取焦点时文字颜色
        self.highlightcolor = None

        # 组件宽度
        self.width = None

        # 组件高度
        self.height = None

        # 文本到多少宽度换行，单位是像素
        self.wraplength = None

        # 文字字体
        self.font = None

        # 存在多行文本时最后一行的对齐方式
        self.justify = CnfJustify.CENTER

        """

        内置位图：
            error
            hourglass
            info
            questhead
            question
            warning
            gray12
            gray25
            gray50
            gray75

        """
        self.bitmap = None

        # 位图与文字共存时，文字位置
        self.compound = None

        # 控制标签的外框样式
        self.relief = None

        # 水平边距
        self.padx = None

        # 垂直边距
        self.pady = None

        # 设置 PhotoImage 图片对象
        self.image = None

        # 设置光标形状
        self.cursor = None

        # 边框大小
        self.bd = self.borderwidth = None

        # 组件状态
        self.state = CnfState.NORMAL

    def set_font(self, family: str = "SimHei", size: Union[int, float] = 12, is_bold: bool = FALSE):
        self.font = (family, size, "bold" if is_bold else "normal")
        return self

    def set_img(self, image_path: str):
        """

        支持图片格式 PGM, PPM, GIF, PNG
        更多格式使用PIL处理

        :param image_path:
        :return:

        """
        self.image = tk.PhotoImage(file=image_path)
        return self

    def build(self):
        return self.__dict__


class LabelCnfProvider(WidgetCnfProvider):

    def __init__(self):
        super().__init__()

        # 组件在盒子中内容位置
        self.anchor = CnfAnchor.CENTER

        # 是否存在下划线
        self.underline = -1

        # Label标签文字内容
        self.text = ""

        # 文本变量
        self.textvariable = None


class ButtonCnfProvider(WidgetCnfProvider):

    def __init__(self):
        super().__init__()

        # 组件在盒子中内容位置
        self.anchor = CnfAnchor.CENTER

        # 是否存在下划线
        self.underline = -1

        # 激活回调函数
        self.command = None


class RadioButtonCnfProvider(WidgetCnfProvider):

    def __init__(self):
        super().__init__()

        # 鼠标光标在选项按钮上时的背景颜色
        self.activebackground = None

        # 鼠标光标在选项按钮上时的前景颜色
        self.activeforeground = None

        # 当选项按钮被选取时的图像
        self.selectcolor = None

        # 当选项按钮被选取时的颜色
        self.selectimage = None

        # 激活回调函数
        self.command = None

        # 当此值为0时，用盒子取代选项按钮
        self.indicatoron = None

        # 文本变量
        self.textvariable = None

        # 选项按钮的值
        self.value = None

        # 设置或取得目前选取的单选按钮，tk变量对象
        self.variable = None


class CheckButtonCnfProvider(WidgetCnfProvider):

    def __init__(self):
        super().__init__()

        # 鼠标光标在选项按钮上时的背景颜色
        self.activebackground = None

        # 鼠标光标在选项按钮上时的前景颜色
        self.activeforeground = None

        # 禁用时颜色
        self.disabledforeground = None

        # 当选项按钮被选取时的图像
        self.selectcolor = None

        # 当选项按钮被选取时的颜色
        self.selectimage = None

        # 激活回调函数
        self.command = None

        # 当此值为0时，用盒子取代选项按钮
        self.indicatoron = None

        # 文本变量
        self.textvariable = None

        # 设置或取得目前选取的单选按钮，tk变量对象
        self.variable = None

        # 设置默认未选中复选框是0
        self.offvalue = None

        # 设置默认未选中复选框是1
        self.onvalue = None


class EntryCnfProvider(WidgetCnfProvider):

    def __init__(self):
        super().__init__()

        # 选取的字符串是否自动到剪贴板中
        self.exportselection = CnfBooleans.FALSE

        # 显示输入字符串
        self.show = None

        # 被选取字符串的背景颜色
        self.selectbackground = None

        # 被选取字符串的前景颜色
        self.selectfroeground = None

        # 选取字符串时的边界宽度
        self.selectborderwidth = 1

        # 在x轴使用滚动条
        self.xscrollcommand = CnfBooleans.FALSE

        # 文本变量
        self.textvariable = None


class FrameCnfProvider(WidgetCnfProvider):

    def __init__(self):
        super().__init__()


class LabelFrameCnfProvider(WidgetCnfProvider):

    def __init__(self):
        super().__init__()

        del self.justify
        del self.state

        # 盒子文本内容
        self.text = None

        # 盒子文本锚点
        self.labelAnchor = None


class TkcButtonCnfProvider(LabelCnfProvider):

    def __init__(self):
        super(TkcButtonCnfProvider, self).__init__()
        self.set_font(size=int(px2pt(14)))
        self.text = "按 钮"
        self.fg = ThemeColor.white
        self.bg = ThemeColor.primary
        self.padx = 15
        self.pady = 6
        self.cursor = CnfCursor.POINTER


class TTKWidgetCnfProvider:

    def __init__(self):
        pass

    def build(self):
        return self.__dict__


class SeparatorCnfProvider(TTKWidgetCnfProvider):

    def __init__(self):
        super().__init__()

        # 定义方向
        self.orient = CnfOrient.HORIZONTAL


class PackCnfProvider:

    def __init__(self):
        # 在指定的组件前面进行pack
        self.before = None

        # 在指定的组件后面进行pack
        self.after = None

        # 组件在盒子中内容位置
        self.anchor = CnfAnchor.CENTER

        # 若没有启用组件expand空间，则只包含组件独占空间
        self.expand = CnfBooleans.FALSE

        # 填充空间方式
        self.fill = CnfFill.NONE

        # 空间位置，理解为CSS中float浮动属性
        self.side = CnfSide.TOP

        # 内部padding值
        self.ipadx = None
        self.ipady = None

        # 外部边距值
        self.padx = [0, 0]
        self.pady = [0, 0]

    @property
    def float(self):
        return self.side

    @float.setter
    def float(self, value):
        self.side = value

    def build(self):
        return self.__dict__

    def pack(self, component):
        component.pack(self.build())
        return component


class GridCnfProvider:

    def __init__(self):
        # 行序号
        self.row = None

        # 列序号
        self.column = None

        # 行跨单元格
        self.rowspan = None

        # 列跨单元格
        self.columnspan = None

        # 类似anchor
        self.sticky = None

        # 外部边距值
        self.padx = [0, 0]
        self.pady = [0, 0]

    def build(self):
        return self.__dict__

    def grid(self, component):
        component.grid(self.build())
        return component


class PlaceCnfProvider:

    def __init__(self):
        # 水平绝对坐标
        self.x = None

        # 垂直绝对坐标
        self.y = None

        # 水平相对坐标，设置百分比0-1
        self.relx = None

        # 垂直相对坐标，设置百分比0-1
        self.rely = None

        self.weight = None
        self.height = None

        self.relweight = None
        self.relheight = None

    def build(self):
        return self.__dict__

    def place(self, component):
        component.place(self.build())
        return component


class App(tk.Tk):

    def __init__(self, screenName=None, baseName=None, className='Tk', useTk=1, sync=0, use=None):
        super().__init__(screenName, baseName, className, useTk, sync, use)

        self._is_set_specs = False

    def set_specs(self, w: int = 800, h: int = 600, x: int = None, y: int = None):
        if x is None:
            x = (self.winfo_screenwidth() // 2) - (w // 2)

        if y is None:
            y = (self.winfo_screenheight() // 2) - (h // 2)

        self.geometry(f"{w}x{h}+{x}+{y}")

        self._is_set_specs = True

    def mainloop(self, n=0):
        if not self._is_set_specs:
            self.set_specs()

        super(App, self).mainloop(n)

    def Label(self, provider: LabelCnfProvider):
        """

        构建Label组件

        :param provider:
        :return:

        """
        return tk.Label(self, provider.build())

    def Button(self, provider: ButtonCnfProvider):
        """

        构建Button组件

        :param provider:
        :return:

        """
        return tk.Button(self, provider.build())

    def RadioButton(self, provider: RadioButtonCnfProvider):
        """

        构建单选组件

        :param provider:
        :return:

        """
        return tk.Radiobutton(self, provider.build())

    def CheckButton(self, provider: CheckButtonCnfProvider):
        """

        构建多选框组件

        :param provider:
        :return:

        """
        return tk.Checkbutton(self, provider.build())

    def Entry(self, provider: EntryCnfProvider):
        """

        构建文本输入框组件

        :param provider:
        :return:

        """
        return tk.Entry(self, provider.build())

    def Frame(self, provider: FrameCnfProvider):
        """

        构建组件盒子容器

        :param provider:
        :return:

        """
        return tk.Frame(self, provider.build())

    def LabelFrame(self, provider: LabelFrameCnfProvider):
        """

        构建组件内联盒子容器

        :param provider:
        :return:

        """
        return tk.LabelFrame(self, provider.build())

    def Separator(self, provider: SeparatorCnfProvider):
        """

        构建分割线组件

        :param provider:
        :return:

        """
        return ttk.Separator(self, **provider.build())

    def Tkc_Button(self, provider: TkcButtonCnfProvider):
        """

        构建一个TKC样式Button组件

        :param provider:
        :return:

        """
        return self.Label(provider)

    def fix_win_display(self):
        # 告诉操作系统使用程序自身的dpi适配
        ctypes.windll.shcore.SetProcessDpiAwareness(1)
        # 设置程序缩放
        self.tk.call("tk", "scaling", ctypes.windll.shcore.GetScaleFactorForDevice(0) / 75)
