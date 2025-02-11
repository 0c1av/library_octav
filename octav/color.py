class octav:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    END = '\033[0m'
    
    def red(text):
        return f"{octav.RED}{text}{octav.END}"
    
    def green(text):
        return f"{octav.GREEN}{text}{octav.END}"
    
    def yellow(text):
        return f"{octav.YELLOW}{text}{octav.END}"
    
    def blue(text):
        return f"{octav.BLUE}{text}{octav.END}"
    
    def magenta(text):
        return f"{octav.MAGENTA}{text}{octav.END}"
    
    def cyan(text):
        return f"{octav.CYAN}{text}{octav.END}"
    
red = octav.red
green = octav.green
yellow = octav.yellow
blue = octav.blue
magenta = octav.magenta
cyan = octav.cyan