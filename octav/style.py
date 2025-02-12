class octav:
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ITALIC = '\033[3m'
    BLINK = '\033[5m'
    INVERT = '\033[7m'
    STRIKETHROUGH = '\033[9m'
    END = '\033[0m'

    def bold(text):
        return f"{octav.BOLD}{text}{octav.END}"
    
    def underline(text):
        return f"{octav.UNDERLINE}{text}{octav.END}"
    
    def italic(text):
        return f"{octav.ITALIC}{text}{octav.END}"
    
    def blink(text):
        return f"{octav.BLINK}{text}{octav.END}"
    
    def invert(text):
        return f"{octav.INVERT}{text}{octav.END}"
    
    def strikethrough(text):
        return f"{octav.STRIKETHROUGH}{text}{octav.END}"
    
bold = octav.bold
underline = octav.underline
italic = octav.italic
blink = octav.blink
invert = octav.invert
strikethrough = octav.strikethrough

