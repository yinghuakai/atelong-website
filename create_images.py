import os
from PIL import Image, ImageDraw

# Create images directory
img_dir = "F:/zhuomina/atelong-website-new/images"

# Create placeholder service images with gradients
def create_gradient_image(filename, color1, color2):
    img = Image.new('RGB', (600, 400))
    draw = ImageDraw.Draw(img)
    
    for y in range(400):
        ratio = y / 400
        r = int(color1[0] * (1 - ratio) + color2[0] * ratio)
        g = int(color1[1] * (1 - ratio) + color2[1] * ratio)
        b = int(color1[2] * (1 - ratio) + color2[2] * ratio)
        draw.line([(0, y), (600, y)], fill=(r, g, b))
    
    img.save(os.path.join(img_dir, filename))

# Swimming - blue gradient
create_gradient_image('swimming.jpg', (0, 150, 200), (0, 80, 150))

# Fitness - dark gray gradient
create_gradient_image('fitness.jpg', (50, 50, 50), (30, 30, 30))

# Courses - purple gradient
create_gradient_image('courses.jpg', (100, 50, 150), (60, 30, 100))

# VIP - gold gradient
create_gradient_image('vip.jpg', (200, 160, 80), (150, 120, 50))

# Hero background
create_gradient_image('hero-bg.jpg', (20, 20, 20), (40, 10, 30))

print("Images created successfully!")
