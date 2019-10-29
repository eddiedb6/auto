import AFWConst

def GetKeyFromChar(char):
    key = None
    needShift = False
    if char.islower():
        key = ord(char) - ord('a') + AFWConst.AFWKeyA
    elif char.isupper():
        key = ord(char) - ord('A') + AFWConst.AFWKeyA
        needShift = True
    elif char.isdigit():
        key = ord(char) - ord('0') + AFWConst.AFWKey0
    elif char in __keyMap:
        key = __keyMap[char]
    elif char in __keyMapWithShift:
        key = __keyMapWithShift[char]
        needShift = True
    return key, needShift

def SimulateTextInput(ui, text):
    for char in text:
        key, needShift = GetKeyFromChar(char)
        if key is None:
            continue
        if needShift:
            ui.PressKey(AFWConst.AFWKeyShift)
        ui.PressKey(key)
        ui.ReleaseKey(key)
        if needShift:
            ui.ReleaseKey(AFWConst.AFWKeyShift)
    return True

__keyMap = {
    '`': AFWConst.AFWKeyTidle,
        
    '-': AFWConst.AFWKeyMinus,
    '=': AFWConst.AFWKeyPlus,

    '[': AFWConst.AFWKeyBracketLeft,
    ']': AFWConst.AFWKeyBracketRight,
    '\\': AFWConst.AFWKeyBackslash,

    ';': AFWConst.AFWKeySemicolon,
    '\'': AFWConst.AFWKeyQuote,

    ',': AFWConst.AFWKeyComma,
    '.': AFWConst.AFWKeyPeriod,
    '/': AFWConst.AFWKeySlash,

    ' ': AFWConst.AFWKeySpace
}
    
__keyMapWithShift = {
    '~': AFWConst.AFWKeyTidle,

    '_': AFWConst.AFWKeyMinus,
    '+': AFWConst.AFWKeyPlus,

    '{': AFWConst.AFWKeyBracketLeft,
    '}': AFWConst.AFWKeyBracketRight,
    '|': AFWConst.AFWKeyBackslash,

    ':': AFWConst.AFWKeySemicolon,
    '\"': AFWConst.AFWKeyQuote,

    '<': AFWConst.AFWKeyComma,
    '>': AFWConst.AFWKeyPeriod,
    '?': AFWConst.AFWKeySlash,

    ')': AFWConst.AFWKey0,
    '!': AFWConst.AFWKey1,
    '@': AFWConst.AFWKey2,
    '#': AFWConst.AFWKey3,
    '$': AFWConst.AFWKey4,
    '%': AFWConst.AFWKey5,
    '^': AFWConst.AFWKey6,
    '&': AFWConst.AFWKey7,
    '*': AFWConst.AFWKey8,
    '(': AFWConst.AFWKey9
}
