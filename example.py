import grayscale_py.grayscale as gs
import matplotlib.pyplot as plt

# Convert an RGB image to grayscale
gray_image = gs.rgb_to_grayscale("input_image.jpg")

# Save the grayscale image
gs.save_grayscale(gray_image, "output_image.png")

# Display the grayscale image
plt.imshow(gray_image, cmap='gray')
plt.axis('off')  # Hide axes
plt.show()
