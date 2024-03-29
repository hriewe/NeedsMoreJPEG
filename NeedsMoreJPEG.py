# Hayden Riewe
# github.com/hriewe
# hrcyber.tech

# Needs more JPEG

from PIL import Image, ImageEnhance, ImageFilter
import sys

# Open image
image = Image.open(sys.argv[1])

# Boost saturation
enhanced = ImageEnhance.Color(image)
SaturationBoost = enhanced.enhance(4)

# Boost contrast
enhanced = ImageEnhance.Contrast(SaturationBoost)
ContrastBoost = enhanced.enhance(1)

# Sharpen
Sharpen = ContrastBoost.filter(ImageFilter.SHARPEN)

Sharpen.save('NeedsMore.jpeg', quality=5)
