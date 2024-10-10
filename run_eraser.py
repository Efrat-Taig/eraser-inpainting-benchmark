

import requests
import base64

# Function to convert an image to Base64 format
def convert_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

"""
This script demonstrates how to use the Bria eraser API to process a single image and mask pair. 
It first converts both the color image and mask to Base64 format, sends them to the API, and then
saves the processed result locally. This script is useful for testing the API's functionality on 
specific examples, allowing for quick evaluation of the image editing process. Make sure to replace 
'TOKEN' with a valid API token and update the image and mask paths as needed.
"""

url = "https://engine.prod.bria-api.com/v1/eraser"

# Paths to the image and mask
image_path = "image.png"
mask_path = "mask.png"

# Convert image and mask to Base64
image_base64 = convert_image_to_base64(image_path)
mask_base64 = convert_image_to_base64(mask_path)


payload = {
  "file": image_base64,
  "mask_file": mask_base64
}

headers = {
  "Content-Type": "application/json",
  "api_token": "TOKEN"
}

response = requests.post(url, json=payload, headers=headers)

# Define the path to save the image
save_path = "/home/ubuntu/spring/misc/efrat/eraser/data_res/output_image.png"

# Check if request was successful
if response.status_code == 200:
    data = response.json()
    URL = data['result_url']
    
    # Download the image from result_url and save it
    image_data = requests.get(URL).content
    with open(save_path, "wb") as output_file:
        output_file.write(image_data)
    print(f"Image saved successfully at {save_path}")
else:
    print(f"Error: {response.status_code}, {response.text}")
