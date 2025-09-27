import torch
from diffusers import StableDiffusionPipeline
import os

def generate_dream_image(prompt, num_images=3, save_dir="dream_outputs", resolution=(512, 512)):
    """
    Generates images from a text prompt using Stable Diffusion.

    Args:
        prompt (str): Text prompt for image generation.
        num_images (int): Number of images to generate.
        save_dir (str): Folder to save generated images.
        resolution (tuple): (width, height) of images.
    Returns:
        List[str]: Paths to generated images.
    """

    os.makedirs(save_dir, exist_ok=True)

    device = "mps" if torch.backends.mps.is_available() else "cpu"
    print(f"📌 Using device: {device}")

    pipe = StableDiffusionPipeline.from_pretrained(
        "runwayml/stable-diffusion-v1-5",
        torch_dtype=torch.float32,
        use_safetensors=True,
    ).to(device)
    pipe.enable_attention_slicing()

    # Generate images
    result = pipe(
        prompt,
        num_inference_steps=30,
        guidance_scale=7.5,
        height=resolution[1],
        width=resolution[0],
        num_images_per_prompt=num_images,
    )
    images = result.images

    # Determine next available file index
    base = 1
    while os.path.exists(os.path.join(save_dir, f"generated_dream_{base}.png")):
        base += 1

    paths = []
    for i, img in enumerate(images):
        filename = os.path.join(save_dir, f"generated_dream_{base + i}.png")
        img.save(filename)
        paths.append(filename)
        print(f"✅ Saved: {filename}")

    return paths
