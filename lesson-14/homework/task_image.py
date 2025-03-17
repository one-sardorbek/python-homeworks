import numpy as np
from PIL import Image

# Load the image using PIL and convert it to a NumPy array
image_path = "images/birds.jpg"
image = Image.open(image_path)
img_array = np.array(image)

# Function to flip the image horizontally and vertically
def flip_image(img):
    return np.flipud(np.fliplr(img))

# Function to add random noise to the image
def add_noise(img, noise_level=30):
    noise = np.random.randint(-noise_level, noise_level, img.shape, dtype=np.int16)
    noisy_img = np.clip(img.astype(np.int16) + noise, 0, 255).astype(np.uint8)
    return noisy_img

# Function to brighten the image channels
def brighten_channels(img, value=40):
    brightened_img = np.clip(img.astype(np.int16) + value, 0, 255).astype(np.uint8)
    return brightened_img

# Function to apply a black mask to a 100x100 region in the center
def apply_mask(img, mask_size=100):
    h, w, _ = img.shape
    start_x = (w - mask_size) // 2
    start_y = (h - mask_size) // 2
    img[start_y:start_y + mask_size, start_x:start_x + mask_size] = [0, 0, 0]
    return img

# Apply the transformations
flipped_img = flip_image(img_array)
noisy_img = add_noise(img_array)
brightened_img = brighten_channels(img_array)
masked_img = apply_mask(img_array.copy())

# Convert NumPy arrays back to images
Image.fromarray(flipped_img).save("flipped_image.jpg")
Image.fromarray(noisy_img).save("noisy_image.jpg")
Image.fromarray(brightened_img).save("brightened_image.jpg")
Image.fromarray(masked_img).save("masked_image.jpg")

print("Image manipulations completed and saved successfully!")
