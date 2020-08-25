import os # Import's os
import platform  # Import's platform

OpSy = platform.system() # Get's the system OS

if OpSy == 'Linux': # Linux
  os.system('sudo shutdown now') # Shutsdown pc
if OpSy == 'Windows': # Windows
  os.system('shutdown -s') # Shutsdown pc
if OpSy == 'Darwin': # MacOS
  os.system('sudo shutdown -h now') # Shutsdown pc
