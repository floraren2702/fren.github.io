# Python Virtual Environments Lab: ASCII Art Generator

## What You'll Learn
- How to create isolated Python environments
- How to install packages with pip
- How to build a fun ASCII art generator with color output

## What is a Virtual Environment?
A virtual environment is like a separate workspace for your Python project. It keeps your project's packages separate from other projects.

---

## Step 1: Create a Virtual Environment

Open the terminal in VSCode (Terminal → New Terminal) and run:

```bash
python -m venv myenv
```

This creates a folder called `myenv` with your virtual environment.

---

## Step 2: Activate the Virtual Environment

**On Mac/Linux:**
```bash
source myenv/bin/activate
```

**On Windows:**
```bash
myenv\Scripts\activate
```

You should see `(myenv)` appear at the start of your terminal line.

---

## Step 3: Install Packages

Let's install two fun packages for creating ASCII art:

```bash
pip install pyfiglet colorama
```

- `pyfiglet` - converts text into ASCII art fonts
- `colorama` - adds color to terminal output

---

## Step 4: Check Installed Packages

See what packages are installed:

```bash
pip list
```

---

## Step 5: Create an ASCII Art Generator

Create a file called `ascii_art.py` and add:

```python
import pyfiglet
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Get user input
text = input("Enter text to convert to ASCII art: ")
font = input("Choose a font (default, slant, banner, bubble, digital) or press Enter for default: ")

# Use default font if user just presses Enter
if not font:
    font = "standard"

# Generate ASCII art with chosen font
ascii_art = pyfiglet.figlet_format(text, font=font)

# Print in color
print(Fore.CYAN + ascii_art)
print(Fore.GREEN + "ASCII art generated successfully!")
print(f"{Fore.YELLOW}Try running again with different fonts!")
```

Run it:
```bash
python ascii_art.py
```

Try entering your name or any text!

---

## Step 6: Deactivate

When you're done, deactivate the virtual environment:

```bash
deactivate
```

The `(myenv)` will disappear from your terminal.

---

## Quick Reference

| Task | Command |
|------|---------|
| Create venv | `python -m venv myenv` |
| Activate (Mac) | `source myenv/bin/activate` |
| Activate (Windows) | `myenv\Scripts\activate` |
| Install package | `pip install package-name` |
| List packages | `pip list` |
| Deactivate | `deactivate` |

---

## Why Use Virtual Environments?

- Different projects can use different package versions
- Keeps your main Python installation clean
- Makes it easy to share your project with others
