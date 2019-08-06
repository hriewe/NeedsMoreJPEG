# Hayden Riewe
# github.com/hriewe

# Needs more JPEG

from PIL import Image, ImageEnhance, ImageFilter
import sys

image = Image.open(sys.argv[1])
enhanced = ImageEnhance.Color(image)
image2 = enhanced.enhance(7)
image2.save('new.jpeg', quality=12)
