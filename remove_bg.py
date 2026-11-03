from rembg import remove
from PIL import Image
import os

input_path = r'c:\Users\HP\Desktop\Portfolio\assets\images\me.png'
output_path = r'c:\Users\HP\Desktop\Portfolio\assets\images\me_nobg.png'

print(f"Processing {input_path}...")

if not os.path.exists(input_path):
    print(f"Error: {input_path} not found.")
    exit(1)

input_img = Image.open(input_path)
output_img = remove(input_img)
output_img.save(output_path)

print(f"Saved to {output_path}")
