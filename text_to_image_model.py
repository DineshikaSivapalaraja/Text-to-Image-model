# -*- coding: utf-8 -*-
"""Text-to-Image-model.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1rkOEF0OOb8xqU3UhPFMdEG8-4F_LZ3C1
"""

from diffusers import StableDiffusionPipeline
import torch

# Load the model (Stable Diffusion)

# model_name = "openfree/flux-chatgpt-ghibli-lora"
model_name = "ZB-Tech/Text-to-Image"
pipe = StableDiffusionPipeline.from_pretrained(model_name, torch_dtype=torch.float16)
pipe.to("cuda")  # Use GPU for better performance
# pipe.to("cpu")

# Function to generate an image

import matplotlib.pyplot as plt

def generate_image(prompt):
    image = pipe(prompt).images[0]  # Generate the image
   # image.show()
    image.save("generated_image.png")  # Save the image

    plt.imshow(image)
    plt.axis("off")
    plt.show() # Show the image

user_prompt = input("Enter a description for the image: ")
generate_image(user_prompt)