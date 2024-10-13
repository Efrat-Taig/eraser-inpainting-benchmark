# Eraser Inpainting Benchmark Dataset

Welcome to the **Eraser Inpainting Benchmark Dataset**! This dataset is specifically designed for evaluating inpainting models, particularly those focused on object removal. The Eraser model, developed by [Bria](https://bria.ai/), is based on diffusion techniques and was trained for this task using a carefully curated dataset that we are now making available for research and evaluation purposes.

The model is open for research (free) and available for purchase.




## Dataset Composition
The dataset consists of **100 images and their corresponding masks**, carefully curated to serve as a benchmark for object removal tasks. These images were sourced from three main areas:

- **Generated Images**:  Created using Bria's generative platform during earlier experiments with object removal scenarios. You can generate similar images through Bria’s platform [here](https://platform.bria.ai/apps/text-to-image).
- **Bria Repository Images**: Proprietary images from Bria, representing real-world use cases for object removal.
- **Academic Images**: Sourced from academic projects such as the  [LAMA project](https://github.com/advimman/lama/tree/main) and [Inpaint Anything](https://github.com/geekyutao/Inpaint-Anything).


Example of Image with Corresponding Mask from the Eraser Benchmark Dataset
<img src="https://github.com/Efrat-Taig/eraser-inpainting-benchmark/blob/main/eraser_bencmark_sample_im.png" alt="Example Image with Mask" width="600"/>





## Download the Dataset

The dataset is available for download from Google Drive. You can access it using the following link:

[**Download Eraser Inpainting Benchmark Dataset**](https://drive.google.com/drive/folders/1f_t6yUSTz8lxf6eO2hjWAs7O-vEFWEPZ?usp=sharing)

## About the Dataset
The benchmark dataset is organized into a main directory called eraser_benchmark_folders. Inside this directory, each color image has its own subfolder named after the image. Each subfolder contains the color image itself along with all associated mask files. This structure ensures that each image and its corresponding masks are grouped together for easy access and processing.


## About the results

The benchmark results are stored in the eraser_benchmark_results folder, with each output saved as a single Demo Image. This demo image combines the original color image, the mask, and the processed result from the eraser API into a single, horizontally concatenated file. Each demo image is named after its corresponding mask file, followed by _demo, making it easy to identify and associate with the original data. This organized structure allows for quick visual comparison of the input and output, providing an intuitive way to validate the results.







## How to Use

**Evaluate your model**:  
   Run your inpainting models on the images and compare results. We recommend trying [Bria’s inpainting models](https://huggingface.co/briaai) available on [Hugging Face](https://huggingface.co/briaai), particularly the **inpainting model**.

**Evaluate Bria eraser pipline on a single image (via code)**:  

To evaluate the Bria pipeline on a single image, use the provided Python script. Begin by specifying the paths to the color image and its corresponding mask. The script converts both files to Base64 format and sends them to the Bria eraser API. After processing, the API returns a URL containing the result image. The script then downloads the processed image and saves it to a specified output path, allowing for easy review. Ensure that the API token and URL are correctly set in the script to authenticate access. Upon successful execution, the processed image will be stored in the `data_res` folder under the specified filename, providing a straightforward way to test the Bria eraser functionality on an individual image and mask pair.

**Evaluate Bria eraser pipline on a single image (via space in HF #1)**:  
[demo on Hugging Face](https://huggingface.co/spaces/briaai/BRIA-Eraser-API)

**Evaluate Bria eraser pipline on a single image (via Bria playground #1)**:  
[demo on Bria playground](https://platform.bria.ai/apps/eraser)

**Evaluate Bria eraser pipline on a single image (via ComfyUI #1)**:  
[Via ComfyUI](https://github.com/Bria-AI/ComfyUI-BRIA-API)


**Evaluate Bria eraser pipline on benchmark**:  

To run the benchmark evaluation, ensure that the dataset is organized in the `benchmark_folders` directory, where each color image and its corresponding masks are stored in individual subfolders. Before starting, set the API endpoint and API token within the code, as these are required for accessing the eraser API. Once configured, run the `run_benchmark` function, which will process each image-mask pair in the dataset. The results will be saved in the `benchmark_res` folder, with each demo image showing the original color image, mask, and processed result side-by-side. This setup allows you to evaluate the effectiveness of the eraser model on the dataset and quickly review the output for each test case.

## Bria’s Inpainting Products

At Bria, we offer two main products:
1. **Inpainting Model**: Bria Demo inpainting foundation model  [Hugging Face](https://huggingface.co/spaces/briaai/BRIA-2.3-ControlNet-Erase)
   [Try the model here: XXXX]
1. **Inpainting Model**: Bria inpainting foundation model  [Hugging Face](https://huggingface.co/briaai/BRIA-2.3-Inpainting)
   [Try the model here: XXXX]
2. **Complete Pipeline**: In addition to the model, we provide a full inpainting pipeline accessible via **API**. This broader solution ensures that Bria’s clients not only get the foundation model but also the complete inpainting workflow for their use cases.  
   [Full pipeline documentation: XXXX]  
   [API demo: XXXX]

## Citation

When using the **Eraser Inpainting Benchmark Dataset**, please cite the [XXXXX](XXXX)

## License

Bria’s inpainting model is open source for academia. Academics can download the model, weights, and full training code from [Hugging Face](https://huggingface.co/briaai) or request access through this [link](https://docs.google.com/forms/d/e/1FAIpQLSe-E1r-QoBmsAZbJ5MJKB76wGnk6bUn2kBq5imPQVVJviv1Kg/viewform).

For industry users, the model is source available with a platform fee. You can purchase access to the full platform, which includes the inpainting model, weights, and training code, by contacting Bria through this [link](https://bria.ai/contact-us/) or request access via [Hugging Face](https://huggingface.co/briaai).

The images included in this benchmark are provided exclusively for research purposes. They are intended to support the development, evaluation, and analysis of algorithms within academic and non-commercial research contexts. Any commercial use of these images, including but not limited to reproduction, distribution, or incorporation into commercial products or services, is strictly prohibited. This restriction ensures that the dataset remains dedicated to advancing research and responsible innovation in the field.

## Contributions

We welcome contributions and discussions from the community! Feel free to open issues or submit pull requests to improve this repository.

---

