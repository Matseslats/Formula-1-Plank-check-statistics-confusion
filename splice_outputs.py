from PIL import Image

# Open and load all your images into a list
images = []
for i in range(0, 36):
    image = Image.open(f'./graphs/out_{i}.png')
    images.append(image)

# Calculate the dimensions of the final grid
grid_width = 6
grid_height = 6
image_width, image_height = images[0].size
grid_size = (image_width * grid_width, image_height * grid_height)

# Create a new blank image for the grid
grid_image = Image.new('RGB', grid_size)

# Iterate through the images and paste them into the grid
for i in range(len(images)):
    row = i // grid_width
    col = i % grid_width
    x = col * image_width
    y = row * image_height
    grid_image.paste(images[i], (x, y))

# Save the final grid image
grid_image.save('all_graphs.png')  # Replace with your desired output filename
