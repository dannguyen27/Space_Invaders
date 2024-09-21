from PIL import Image

# Load the image
image_path = "images/background4.gif"
image = Image.open(image_path)

# Resize the image to fit the screen dimensions (500x600)
resized_image = image.resize((500, 600), Image.LANCZOS)

# Save the resized image as PNG
resized_image.save("background_level4.gif", format="PNG")
