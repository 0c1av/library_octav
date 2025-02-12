# Octav - Simple Terminal Text Styling

Octav is a lightweight Python library that allows you to easily format terminal output with colors, bold text, underline, and more.

## Installation

Install Octav using pip:

```sh
pip install octav
```

## Usage

Import Octav and use its functions to style your terminal output:

```python
import octav

print(octav.red("This is red text"))
print(octav.green("This is green text"))
print(octav.blue("This is blue text"))
print(octav.bold("This is bold text"))
print(octav.underline("This is underlined text"))
print(octav.strikethrough("This is strikethrough text"))
```

## Available Styles

### Colors
| Function    | Output  |
|------------|---------|
| `octav.red(text)` | Red text |
| `octav.green(text)` | Green text |
| `octav.yellow(text)` | Yellow text |
| `octav.blue(text)` | Blue text |
| `octav.magenta(text)` | Magenta text |
| `octav.cyan(text)` | Cyan text |

### Text Formatting
| Function    | Output  |
|------------|---------|
| `octav.bold(text)` | Bold text |
| `octav.underline(text)` | Underlined text |
| `octav.italic(text)` | Italic text (may not work in all terminals) |
| `octav.blink(text)` | Blinking text (may not work in all terminals) |
| `octav.invert(text)` | Inverted colors |
| `octav.strikethrough(text)` | Strikethrough text |

## Contributing

Feel free to contribute by submitting issues or pull requests on [GitHub](https://github.com/0c1av/library_octav).

