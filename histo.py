import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Assuming `original_image`, `encrypted_image`, and `decrypted_image` are numpy arrays
image = Image.open('101_4.jpg').convert('L')  # Convert to grayscale
original_image = np.array(image)

image2 = Image.open('D:\computed.tif').convert('L')  # Convert to grayscale
decrypted_image = np.array(image2)


# Calculate mean and standard deviation
mean_original = np.mean(original_image)
std_original = np.std(original_image)
mean_decrypted = np.mean(decrypted_image)
std_decrypted = np.std(decrypted_image)

# Print the results
print(f"Original Image - Mean: {mean_original}, Std Dev: {std_original}")
print(f"Decrypted Image - Mean: {mean_decrypted}, Std Dev: {std_decrypted}")

# Plot histograms
plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
plt.hist(original_image.ravel(), bins=256, color='blue', alpha=0.7, label='Original')
plt.hist(decrypted_image.ravel(), bins=256, color='red', alpha=0.7, label='Decrypted')

plt.legend(loc='upper right')
plt.title('Histogram of Pixel Values')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')

plt.show()
