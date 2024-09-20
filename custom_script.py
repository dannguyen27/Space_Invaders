from PIL import Image

# Load and resize the image
image = Image.open("enemy_laser.gif")
resized_image = image.resize((15, 15), Image.Resampling.LANCZOS)
resized_image.save("resized_enemy_laser.gif")

print("Image resized successfully.")
