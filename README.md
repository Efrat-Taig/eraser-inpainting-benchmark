# Eraser Inpainting Benchmark Dataset

Welcome to the **Eraser Inpainting Benchmark Dataset**! This dataset is specifically designed for evaluating inpainting models, particularly those focused on object removal. The Eraser model, developed by [Bria](https://bria.ai/), is based on diffusion techniques and was trained for this task using a carefully curated dataset that we are now making available for research and evaluation purposes.

The model is open for research (free) and available for purchase.




## Dataset Composition
The dataset consists of **107 images and their corresponding masks**, carefully curated to serve as a benchmark for object removal tasks. These images were sourced from three main areas:

- **Generated Images**:  Created using Bria's generative platform during earlier experiments with object removal scenarios. You can generate similar images through Bria’s platform [here](https://platform.bria.ai/apps/text-to-image).
- **Bria Repository Images**: Proprietary images developed in-house at Bria, representing real-world use cases for object removal.
- **Academic Images**: Sourced from academic projects such as the  [LAMA project](https://github.com/advimman/lama/tree/main) and [Inpaint Anything](https://github.com/geekyutao/Inpaint-Anything).


Example of Image with Corresponding Mask from the Eraser Benchmark Dataset
<img src="https://github.com/Efrat-Taig/eraser-inpainting-benchmark/blob/main/eraser_bencmark_sample_im.png" alt="Example Image with Mask" width="600"/>





## Download the Dataset

The dataset is available for download from Google Drive. You can access it using the following link:

[**Download Eraser Inpainting Benchmark Dataset**](https://drive.google.com/drive/folders/1f_t6yUSTz8lxf6eO2hjWAs7O-vEFWEPZ?usp=sharing)

## How to Use

**Evaluate your model**:  
   Run your inpainting models on the images and compare results. We recommend trying [Bria’s inpainting models](https://huggingface.co/briaai) available on [Hugging Face](https://huggingface.co/briaai), particularly the **inpainting model**.

**Evaluate Bria model**:  
  TBD

**Evaluate Bria pipline**:  
  TBD

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

## Contributions

We welcome contributions and discussions from the community! Feel free to open issues or submit pull requests to improve this repository.

---

