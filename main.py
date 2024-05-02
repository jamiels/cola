import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

# Load the image
image_path = 'cola.jpg'  # Specify the path to your image
image = Image.open(image_path)

# Convert the image to RGB (if not already in that format)
rgb_image = image.convert('RGB')

# Convert RGB to HSV
hsv_image = rgb_image.convert('HSV')
hsv_pixels = np.array(hsv_image)

# Extract Hue, Saturation, and Value layers
hue_layer = hsv_pixels[:, :, 0]
saturation_layer = hsv_pixels[:, :, 1]
value_layer = hsv_pixels[:, :, 2]

# Define the range for red hue
# Typically, red hue ranges from 0-30 and 330-360 degrees.
# Since Pillow scales the HSV hues to 0-255, we adjust: (0-30)/360*255 and (330-360)/360*255
lower_red = int((0/360) * 255)
upper_red = int((30/360) * 255)
lower_red2 = int((330/360) * 255)
upper_red2 = int((360/360) * 255)

# Identify red pixels
red_pixels = ((hue_layer <= upper_red) & (hue_layer >= lower_red)) | \
             ((hue_layer <= upper_red2) & (hue_layer >= lower_red2))

# Visualization of red pixels
plt.imshow(red_pixels, cmap='gray')  # Show red pixels in white and others in black
plt.title('Red Pixels in the Image')
plt.axis('off')  # Turn off axis labels
plt.show()
