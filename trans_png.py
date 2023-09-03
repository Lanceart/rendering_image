from PIL import Image

def read_ppm(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    # Remove comments
    lines = [line for line in lines if not line.startswith("#")]

    # Verify the magic number
    if lines[0].strip() != "P3":
        print("Not a P3 PPM file")
        return None

    # Get image dimensions and max color value
    width, height = map(int, lines[1].split())
    max_value = int(lines[2])

    # Read the pixel data
    pixels = []
    for line in lines[3:]:
        pixels.extend(map(int, line.split()))

    # Create an Image object
    image = Image.new("RGB", (width, height))
    for y in range(height):
        for x in range(width):
            index = 3 * (y * width + x)
            pixel = tuple(pixels[index:index + 3])
            image.putpixel((x, y), pixel)

    return image

# Read the PPM file
ppm_image = read_ppm("image.ppm")
if ppm_image:
    # Save as JPG
    ppm_image.save("image.png")
