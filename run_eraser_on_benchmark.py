
"""
This script evaluates Bria's eraser API on a benchmark dataset by processing each color image 
and its associated masks in a structured format. The main function `run_benchmark` traverses 
through the benchmark folders, where each subfolder contains a single color image and its relevant masks. 
For each image-mask pair, the script sends a request to the Bria API, receives the processed result, 
and generates a demo image combining the original image, mask, and result. 

To use this script:
1. Make sure to replace 'api_token' with your valid API token.
2. Update the paths for the benchmark folder, output folder, and API URL if needed.
3. Run the script to process all images in the benchmark dataset and save results in `benchmark_res`.

Each output demo image is saved with a name derived from the mask file and contains a visual representation 
of the original, mask, and result side-by-side, providing an intuitive comparison for each processed example.
"""
```


import os
import requests
import base64
from PIL import Image

# Converts an image to Base64 format
def convert_image_to_base64(image_path):
    """
    Convert an image file to a Base64-encoded string.
    
    Parameters:
    image_path (str): Path to the image file.
    
    Returns:
    str: Base64-encoded string of the image, or None if there's an error.
    """
    try:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    except Exception as e:
        print(f"Failed to convert {image_path} to Base64. Error: {e}")
        return None

# Concatenates the original image, mask, and result image horizontally
def concatenate_images(image_path, mask_path, result_path, save_path):
    """
    Concatenate the original image, mask, and result horizontally and save it.
    
    Parameters:
    image_path (str): Path to the original image.
    mask_path (str): Path to the mask image.
    result_path (str): Path to the result image.
    save_path (str): Path to save the concatenated image.
    """
    try:
        original = Image.open(image_path)
        mask = Image.open(mask_path)
        result = Image.open(result_path)
        
        # Resize mask and result to match original size if needed
        mask = mask.resize(original.size)
        result = result.resize(original.size)
        
        # Concatenate images
        concatenated = Image.new('RGB', (original.width * 3, original.height))
        concatenated.paste(original, (0, 0))
        concatenated.paste(mask, (original.width, 0))
        concatenated.paste(result, (original.width * 2, 0))
        
        # Save concatenated image
        concatenated.save(save_path)
        print(f"Concatenated image saved at {save_path}")
    except Exception as e:
        print(f"Failed to concatenate images. Error: {e}")

# Sends a request to the API with an image and mask, then saves the result
def process_image_with_mask(api_url, api_token, color_image_path, mask_path, output_folder):
    """
    Send the color image and mask to the API, receive and save the result, and create a demo image.
    
    Parameters:
    api_url (str): API endpoint URL.
    api_token (str): API token for authorization.
    color_image_path (str): Path to the color image.
    mask_path (str): Path to the mask image.
    output_folder (str): Folder to save the result and demo images.
    """
    # Convert images to Base64
    image_base64 = convert_image_to_base64(color_image_path)
    mask_base64 = convert_image_to_base64(mask_path)
    
    if not image_base64 or not mask_base64:
        print("Skipping due to Base64 conversion failure.")
        return

    payload = {
        "file": image_base64,
        "mask_file": mask_base64
    }

    headers = {
        "Content-Type": "application/json",
        "api_token": api_token
    }

    # Send request to the API
    try:
        response = requests.post(api_url, json=payload, headers=headers)
        print(f"Request sent for {color_image_path} with mask {mask_path}, status code: {response.status_code}")
    except Exception as e:
        print(f"Failed to send request for {color_image_path} with mask {mask_path}. Error: {e}")
        return

    # Save the result if the request is successful
    result_filename = os.path.basename(mask_path)
    save_path = os.path.join(output_folder, result_filename)

    if response.status_code == 200:
        try:
            data = response.json()
            result_url = data['result_url']
            image_data = requests.get(result_url).content
            
            # Save the result image
            with open(save_path, "wb") as output_file:
                output_file.write(image_data)
            print(f"Image saved successfully at {save_path}")

            # Create and save the concatenated demo image
            demo_save_path = os.path.join(output_folder, f"{os.path.splitext(result_filename)[0]}_demo.png")
            concatenate_images(color_image_path, mask_path, save_path, demo_save_path)

        except Exception as e:
            print(f"Failed to download/save the result image for {color_image_path} with mask {mask_path}. Error: {e}")
    else:
        print(f"Error: {response.status_code}, {response.text}")

# Main function to process the benchmark dataset
def run_benchmark(api_url, api_token, benchmark_folder, output_folder):
    """
    Run the benchmark by processing each color image and its associated masks in the dataset.
    
    Parameters:
    api_url (str): API endpoint URL.
    api_token (str): API token for authorization.
    benchmark_folder (str): Path to the main benchmark folder with subfolders for each image group.
    output_folder (str): Path to save the results and demo images.
    """
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    print(f"Output folder path: {output_folder}")

    # Loop through each subfolder in benchmark_folders
    for subfolder in os.listdir(benchmark_folder):
        subfolder_path = os.path.join(benchmark_folder, subfolder)
        if os.path.isdir(subfolder_path):
            print(f"Processing subfolder: {subfolder_path}")

            # Identify color image and masks
            color_image_path = None
            masks = []
            
            for file in os.listdir(subfolder_path):
                if file.endswith("_.png"):
                    color_image_path = os.path.join(subfolder_path, file)
                elif file.endswith(".png") and not file.endswith("_.png"):
                    masks.append(os.path.join(subfolder_path, file))
            
            # If no color image or masks found, skip the subfolder
            if not color_image_path or not masks:
                print(f"No valid color image or masks found in {subfolder_path}. Skipping.")
                continue

            # Process each mask with the color image
            for mask_path in masks:
                process_image_with_mask(api_url, api_token, color_image_path, mask_path, output_folder)

# Define parameters and paths
api_url = "https://engine.prod.bria-api.com/v1/eraser"
api_token = "TOKE"
benchmark_folder = "benchmark_folders"
output_folder = "benchmark_res"

# Run the benchmark
run_benchmark(api_url, api_token, benchmark_folder, output_folder)





