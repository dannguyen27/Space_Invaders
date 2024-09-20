from PIL import Image

# Load and resize the image
image = Image.open("background.gif")
resized_image = image.resize((800, 600), Image.Resampling.LANCZOS)
resized_image.save("resized_background.gif")

print("Image resized successfully.")
