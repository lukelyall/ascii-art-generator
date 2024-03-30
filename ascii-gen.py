from PIL import Image

# open an image at location
im = Image.open("./image.jpg")

# ASCII grayscale from dark to light
scale = [
         "$", "@", "B", "%", "8", "&", "W", "M", "#", "*",
         "o", "a", "h", "k", "b", "d", "p", "q", "w", "m",
         "Z", "O", "0", "Q", "L", "C", "J", "U", "Y", "X",
         "z", "c", "v", "u", "n", "x", "r", "j", "f", "t",
         "/", "\\", "|", "(", ")", "1", "{", "}", "[", "]",
         "?", "-", "_", "+", "~", "<", ">", "i", "!", "l",
         "I", ";", ":", ",", "\"", "^", "`", "'", "."
        ]

# get the width and height of the image
width, height = im.size

# convert the img to RGB
im.convert('RGB')
ascii_image = ""

for y in range(height):
  for x in range(width):
    # Get RGB value of pixel coordinates
    R, G, B  = im.getpixel((x, y))

    # brightness 0 (black) - 255 (white)
    brightness = sum([R,G,B])/3
    index = int(brightness / 256 * len(scale))
    ascii_image += scale[index]

  ascii_image += "\n"

# store the art in a .txt file
with open("ascii_image.txt", "w") as f:
    f.write(ascii_image)

print("ASCII art saved")