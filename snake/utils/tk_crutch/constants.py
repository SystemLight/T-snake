from tkinter.constants import *


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


class MouseEvent:
    ANY = "<Any-Button>"  # 任何鼠标按钮

    CLICK_LEFT = "<Button-1>"  # 单击鼠标左键
    CLICK_MIDDLE = "<Button-2>"  # 单击鼠标中建
    CLICK_RIGHT = "<Button-3>"  # 单击鼠标右建

    DOUBLE_CLICK_LEFT = "<Double-Button-1>"  # 双击鼠标左键
    DOUBLE_CLICK_MIDDLE = "<Double-Button-2>"  # 双击鼠标中建
    DOUBLE_CLICK_RIGHT = "<Double-Button-3>"  # 双击鼠标右建

    MOVE = "<Motion>"  # 鼠标移动

    CLICK_LEFT_MOVE = "<B1-Motion>"  # 按住鼠标左键移动
    CLICK_MIDDLE_MOVE = "<B2-Motion>"  # 按住鼠标中键移动
    CLICK_RIGHT_MOVE = "<B2-Motion>"  # 按住鼠标右键移动

    UP_LEFT = "<ButtonRelease-1>"  # 放开鼠标左键
    UP_MIDDLE = "<ButtonRelease-2>"  # 放开鼠标中建
    UP_RIGHT = "<ButtonRelease-3>"  # 放开鼠标右建

    ENTER = "<Enter>"  # 鼠标光标进入控件
    LEAVE = "<Leave>"  # 鼠标光标离开控件

    SCROLL_TOP = "<Button-4>"  # 滑轮向上滚动
    SCROLL_BOTTOM = "<Button-5>"  # 滑轮向下滚动


class KeyEvent:
    Focus_In = "<FocusIn>"
    Focus_Out = "<FocusOut>"

    SHIFT_UP = "<Shift-Up>"
    ALT_UP = "<Alt-Up>"
    CTRL_UP = "<Ctrl-Up>"

    Return = "<Return>"
    KEY_DOWN = "<Key>"

    ESC = "<Escape>"


class ComponentEvent:
    CONFIGURE = "<Configure>"


class Protocols:
    CLOSE_WINDOW = "WM_DELETE_WINDOW"


class States:
    MAX_WINDOW = "zoomed"  # 最大化窗口


class Attributes:
    MAX_WINDOW = "-fullscreen"  # 最大化窗口
