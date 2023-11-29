import os
from PIL import Image
import imageio
import re
import natsort



def create_gif(input_folder, output_gif_path, duration=0.1):
    images = []

    # Get a sorted list of image files in the folder
    image_files = sorted([f for f in os.listdir(input_folder) if f.endswith(('.png', '.jpg', '.jpeg'))])

    image_files=natsort.natsorted(image_files)
    
    
    #for i in range(3):
    #   image_files.extend(image_files)

    #image_files=image_files[::6]
    print(image_files)

    for image_file in image_files:
        image_path = os.path.join(input_folder, image_file)
        img = Image.open(image_path)
        images.append(img)

    # Save the images as a GIF
    imageio.mimsave(output_gif_path, images, duration=duration)

if __name__ == "__main__":
    input_folder = "gif"
    output_gif_path = "AcousticPhononModes.gif"
    create_gif(input_folder, output_gif_path, duration=0.1)