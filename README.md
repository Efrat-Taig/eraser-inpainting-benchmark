# Eraser Inpainting Benchmark Dataset

Welcome to the Eraser Inpainting Benchmark Dataset! This dataset is designed for evaluating inpainting models, especially those specialized in object removal. The Eraser model, developed by [Bria](https://bria.ai/), is based on advanced diffusion techniques and trained specifically for object removal tasks. It has been rigorously tested on a carefully curated benchmark, which we are now 
making available for research and evaluation purposes.



The eraser model and pipeline are open for academic research (free of charge) and available for purchase for other applications.

For an in-depth overview of the Eraser pipeline, benchmarks, and key features, check out our Medium article [here](https://medium.com/@efrat_37973/brias-eraser-a-groundbreaking-tool-for-object-removal-in-images-787e7fcacf63).


## Dataset Composition
The dataset consists of **100 images and their corresponding masks**, carefully curated to serve as a benchmark for object removal tasks. These images were sourced from three main areas:

- **Generated Images**:  Created using Bria's generative platform. You can generate similar images through Bria’s platform [here](https://platform.bria.ai/apps/text-to-image).
- **Bria Repository Images**: Proprietary images from Bria, representing real-world use cases for object removal.
- **Academic Images**: Sourced from academic projects such as the  [LAMA project](https://github.com/advimman/lama/tree/main) and [Inpaint Anything](https://github.com/geekyutao/Inpaint-Anything).


Example of Image with Corresponding Mask from the Eraser Benchmark Dataset
<img src="https://github.com/Efrat-Taig/eraser-inpainting-benchmark/blob/main/eraser_bencmark_sample_im.png">





## Download the Dataset

The dataset is available for download from Google Drive. You can access it using the following link:

[**Download Eraser Inpainting Benchmark Dataset**](https://drive.google.com/drive/folders/1f_t6yUSTz8lxf6eO2hjWAs7O-vEFWEPZ?usp=sharing)

## About the Dataset
The benchmark dataset is organized into a main directory called [eraser_benchmark_folders](https://drive.google.com/drive/folders/1f_t6yUSTz8lxf6eO2hjWAs7O-vEFWEPZ?usp=drive_link). Inside this directory, each color image has its own subfolder named after the image. Each subfolder contains the color image itself along with all associated mask files. This structure ensures that each image and its corresponding masks are grouped together for easy access and processing.


## About the results


The benchmark results are stored in the [eraser_benchmark_results](https://drive.google.com/drive/folders/1d6WDODdNHbV_q9ti3uLOpl1jWRafaGuK?usp=drive_link) folder, where each output combines the original image, mask, and processed result from the Eraser API into a single, concatenated file. Each demo image is named after its corresponding mask file for easy identification. The code to generate these images is included in the `run_eraser_on_benchmark.py` function. This setup enables quick and clear comparison of inputs and outputs.


Example of benchmark results:

<img src="https://github.com/Efrat-Taig/eraser-inpainting-benchmark/blob/main/eraser_bencmark_results.png" >


## About the pipline 
The Eraser pipeline by Bria is a robust, modular framework specifically designed for seamless object removal in images. It combines Bria’s advanced foundation models, ControlNet guidance, and LoRA for precise customization, ensuring high-quality results that align with users’ expectations. By incorporating low-frequency details and global context from the image, the pipeline maintains visual coherence and natural backgrounds, even in complex scenes. Designed with flexibility in mind, the Eraser pipeline can adapt to various use cases, from simple object removal to intricate background adjustments, all while upholding ethical data practices through legally sourced training sets.

For a deeper look into the Eraser Pipeline, including insights into the technology, customization options, and unique features that make Bria's Eraser stand out, read our detailed Medium article: [Bria’s Eraser: A Groundbreaking Tool for Object Removal in Images
](https://medium.com/@efrat_37973/brias-eraser-a-groundbreaking-tool-for-object-removal-in-images-787e7fcacf63)
## How to Use

**Evaluate Bria eraser pipline on a single image (via code)**:  

To evaluate the Bria pipeline on a *single* image, use the provided Python script [run_eraser.py](https://github.com/Efrat-Taig/eraser-inpainting-benchmark/blob/main/run_eraser.py). Begin by specifying the paths to the color image and its corresponding mask. The script converts both files to Base64 format and sends them to the Bria eraser API. After processing, the API returns a URL containing the result image. We than download the processed image and saves it to a specified output path. Note to ensure that the API token and URL are correctly set in the script to authenticate access. Upon successful execution, the processed image will be stored in the `data_res` folder under the specified filename, providing a straightforward way to test the Bria eraser functionality on an individual image and mask pair.
**[Get TOKEN from here](https://bria.ai/api)**

**Evaluate Bria eraser pipline on a single image (via API)**:  
[API documentation for Bria eraser ](https://bria-ai-api-docs.redoc.ly/tag/Image-Modifications/#operation/eraser)

**Evaluate Bria eraser pipline on a single image (via space in HF #1)**:  
[demo on Hugging Face](https://huggingface.co/spaces/briaai/BRIA-Eraser-API)

**Evaluate Bria eraser pipline on a single image (via Bria playground #1)**:  
[demo on Bria playground](https://platform.bria.ai/apps/eraser)

**Evaluate Bria eraser pipline on a single image (via ComfyUI #1)**:  
[Via ComfyUI](https://github.com/Bria-AI/ComfyUI-BRIA-API)

**Evaluate other model**:  
   Run your inpainting models on the images and compare results. We recommend trying [Bria’s inpainting models](https://huggingface.co/briaai) available on [Hugging Face](https://huggingface.co/briaai), particularly the **inpainting model**.
**Evaluate Bria eraser pipline on benchmark**:  


** Benchmark evaluation**:  

To run the benchmark evaluation, ensure that the dataset is organized in the `benchmark_folders` directory, where each color image and its corresponding masks are stored in individual subfolders. Before starting, set the API endpoint and API token within the code, as these are required for accessing the eraser API. Once configured, run the [run_eraser_on_benchmark.py](https://github.com/Efrat-Taig/eraser-inpainting-benchmark/blob/main/run_eraser_on_benchmark.py) script, which will process each image-mask pair in the dataset. The results will be saved in the `benchmark_res` folder, with each demo image showing the original color image, mask, and processed result side-by-side. This setup allows you to evaluate the effectiveness of the eraser model on the dataset and quickly review the output for each test case.

## Bria’s Other Inpainting Products

At Bria, we offer two main products:
1. **Inpainting Model**: Bria inpainting foundation model (weights and code) from [Hugging Face](https://huggingface.co/spaces/briaai)
   [Get the model here](https://huggingface.co/briaai/BRIA-2.3-Inpainting)
   
1. **Inpainting Model**: Bria Demo for inpainting foundation model  from [Hugging Face](https://huggingface.co/spaces/briaai)
   [Try the model here](https://huggingface.co/spaces/briaai/BRIA-2.3-Inpainting)


## Citation

When using the **Eraser Inpainting Benchmark Dataset**, please cite the [BRIA.AI](https://bria.ai/)

## License

Bria’s inpainting model is open source for academia. Academics can download the model, weights, and full training code from [Hugging Face](https://huggingface.co/briaai) or request access through this [link](https://docs.google.com/forms/d/e/1FAIpQLSe-E1r-QoBmsAZbJ5MJKB76wGnk6bUn2kBq5imPQVVJviv1Kg/viewform).

For industry users, the model is source available with a platform fee. You can purchase access to the full platform, which includes the inpainting model, weights, and training code, by contacting Bria through this [link](https://bria.ai/contact-us/) or request access via [Hugging Face](https://huggingface.co/briaai).

For more information about Bria, its business model, and its free access approach for academia, read this blog: [Bridging the Gap from Academic AI to Ethical Business Models](https://medium.com/@efrat_37973/bridging-the-gap-from-academic-ai-to-ethical-business-models-89327517b940).

The images included in this benchmark are provided exclusively for research purposes. They are intended to support the development, evaluation, and analysis of algorithms within academic and non-commercial research contexts. Any commercial use of these images, including but not limited to reproduction, distribution, or incorporation into commercial products or services, is strictly prohibited. 

## Contributions

We welcome contributions and discussions from the community! Feel free to open issues or submit pull requests to improve this repository.

---

