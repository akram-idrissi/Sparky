import pygame
from .component import Component 

# hashtable for constant time access to all keyboard keys
keyboard = {
'backspace' : pygame.K_BACKSPACE,
'tab' : pygame.K_TAB,
'clear' : pygame.K_CLEAR,
'return' : pygame.K_RETURN,
'pause' : pygame.K_PAUSE,
'escape' : pygame.K_ESCAPE,
'space' : pygame.K_SPACE,
'exclaim' : pygame.K_EXCLAIM,
'quotedbl' : pygame.K_QUOTEDBL,
'hash' : pygame.K_HASH,
'dollar' : pygame.K_DOLLAR,
'ampersand' : pygame.K_AMPERSAND,
'quote' : pygame.K_QUOTE,
'left parenthesis' : pygame.K_LEFTPAREN,
'right parenthesis' : pygame.K_RIGHTPAREN,
'asterisk' : pygame.K_ASTERISK,
'plus' : pygame.K_PLUS,
'comma' : pygame.K_COMMA,
'minus' : pygame.K_MINUS,
'period' : pygame.K_PERIOD,
'forward slash' : pygame.K_SLASH,
'0' : pygame.K_0,
'1' : pygame.K_1,
'2' : pygame.K_2,
'3' : pygame.K_3,
'4' : pygame.K_4,
'5' : pygame.K_5,
'6' : pygame.K_6,
'7' : pygame.K_7,
'8' : pygame.K_8,
'9' : pygame.K_9,
'colon' : pygame.K_COLON,
'semicolon' : pygame.K_SEMICOLON,
'less than' : pygame.K_LESS,
'equal' : pygame.K_EQUALS,
'greater than' : pygame.K_GREATER,
'question' : pygame.K_QUESTION,
'at' : pygame.K_AT,
'left bracket' : pygame.K_LEFTBRACKET,
'backslash' : pygame.K_BACKSLASH,
'right bracket' : pygame.K_RIGHTBRACKET,
'caret' : pygame.K_CARET,
'underscore' : pygame.K_UNDERSCORE,
'grave' : pygame.K_BACKQUOTE,
'a' : pygame.K_a,
'b' : pygame.K_b,
'c' : pygame.K_c,
'd' : pygame.K_d,
'e' : pygame.K_e,
'f' : pygame.K_f,
'g' : pygame.K_g,
'h' : pygame.K_h,
'i' : pygame.K_i,
'j' : pygame.K_j,
'k' : pygame.K_k,
'l' : pygame.K_l,
'm' : pygame.K_m,
'n' : pygame.K_n,
'o' : pygame.K_o,
'p' : pygame.K_p,
'q' : pygame.K_q,
'r' : pygame.K_r,
's' : pygame.K_s,
't' : pygame.K_t,
'u' : pygame.K_u,
'v' : pygame.K_v,
'w' : pygame.K_w,
'x' : pygame.K_x,
'y' : pygame.K_y,
'z' : pygame.K_z,
'delete' : pygame.K_DELETE,
'0' : pygame.K_KP0,
'1' : pygame.K_KP1,
'2' : pygame.K_KP2,
'3' : pygame.K_KP3,
'4' : pygame.K_KP4,
'5' : pygame.K_KP5,
'6' : pygame.K_KP6,
'7' : pygame.K_KP7,
'8' : pygame.K_KP8,
'9' : pygame.K_KP9,
'period' : pygame.K_KP_PERIOD,
'divide' : pygame.K_KP_DIVIDE,
'multiply' : pygame.K_KP_MULTIPLY,
'minus' : pygame.K_KP_MINUS,
'plus' : pygame.K_KP_PLUS,
'enter' : pygame.K_KP_ENTER,
'equals' : pygame.K_KP_EQUALS,
'up' : pygame.K_UP,
'down' : pygame.K_DOWN,
'right' : pygame.K_RIGHT,
'left' : pygame.K_LEFT,
'insert' : pygame.K_INSERT,
'home' : pygame.K_HOME,
'end' : pygame.K_END,
'page up' : pygame.K_PAGEUP,
'page down' : pygame.K_PAGEDOWN,
'F1' : pygame.K_F1,
'F2' : pygame.K_F2,
'F3' : pygame.K_F3,
'F4' : pygame.K_F4,
'F5' : pygame.K_F5,
'F6' : pygame.K_F6,
'F7' : pygame.K_F7,
'F8' : pygame.K_F8,
'F9' : pygame.K_F9,
'F10' : pygame.K_F10,
'F11' : pygame.K_F11,
'F12' : pygame.K_F12,
'F13' : pygame.K_F13,
'F14' : pygame.K_F14,
'F15' : pygame.K_F15,
'numlock' : pygame.K_NUMLOCK,
'capslock' : pygame.K_CAPSLOCK,
'scrollock' : pygame.K_SCROLLOCK,
'right shift' : pygame.K_RSHIFT,
'left shift' : pygame.K_LSHIFT,
'right ctrl' : pygame.K_RCTRL,
'left ctrl' : pygame.K_LCTRL,
'right alt' : pygame.K_RALT,
'left alt' : pygame.K_LALT,
'right meta' : pygame.K_RMETA,
'left meta' : pygame.K_LMETA,
'left windows' : pygame.K_LSUPER,
'right windows' : pygame.K_RSUPER, 
'mode shift' : pygame.K_MODE,
'help' : pygame.K_HELP,
'print screen' : pygame.K_PRINT,
'sysrq' : pygame.K_SYSREQ,
'break' : pygame.K_BREAK,
'menu' : pygame.K_MENU,
'power' : pygame.K_POWER,
'euro' : pygame.K_EURO,
}

class Input(Component):
    """
    A simple class that gives its users a set of utility methods
    to handle keyboard and mouse events. 
    """
    def __init__(self, actor):
        super().__init__(actor)

    def keydown(self, events, key):
        """ Checks if a given key is pressed """
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == keyboard[key]:
                    return True
            return None

    def keyup(self, events,  key):
        """ Checks if a given key is not pressed """
        for event in events:
            if event.type == pygame.KEYUP:
                if event.key == keyboard[key]:
                    return True
            return None

    def keyheld(self, key):
        """ Checks if a given key is held down """
        key_pressed = pygame.key.get_pressed()
        if(key_pressed[keyboard[key]]):
            return True
        return None

    def mouse_clicked(self, events):
        """ Checks if mouse btns are clicked """
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                return True
        return None

    def mouse_released(self, events):
        """ Checks if mouse btns are released """
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                return True
        return None

    def mouse_held(self):
        """ Checks if any of the mouse btns are held down """
        if any(pygame.mouse.get_pressed()):
            return True
        return None

    def mouse_ldown():
        """ Checks if the left mouse btn is pressed """
        if any(pygame.mouse.get_pressed()[0]):
            return True
        return None

    def mouse_mdown():
        """ Checks if the mouse wheel is pressed """
        if any(pygame.mouse.get_pressed()[1]):
            return True
        return None

    def mouse_rdown():
        """ Checks if the right mouse btn is pressed """
        if any(pygame.mouse.get_pressed()[2]):
            return True
        return None
