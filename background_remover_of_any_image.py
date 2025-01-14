from rembg import remove
from PIL import Image

input_path = 'image.png'
output_path = 'image_no_bg.png'

inp = Image.open(input_path)
output = remove(inp)
output.save(output_path)