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

