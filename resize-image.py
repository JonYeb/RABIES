from PIL import Image
import sys
import os

def resize_image(input_path, output_path, max_dimension):
    """
    Resizes an image to fit within a maximum dimension while preserving aspect ratio.

    :param input_path: Path to the input image file.
    :param output_path: Path to save the resized image.
    :param max_dimension: Maximum width or height of the resized image.
    """
    try:
        with Image.open(input_path) as img:
            # Get original dimensions
            original_width, original_height = img.size

            # Calculate the scaling factor
            scaling_factor = min(max_dimension / original_width, max_dimension / original_height)

            # Calculate new dimensions
            new_width = int(original_width * scaling_factor)
            new_height = int(original_height * scaling_factor)

            # Resize the image
            resized_img = img.resize((new_width, new_height), Image.ANTIALIAS)

            # Save the resized image
            resized_img.save(output_path)
            print(f"Image resized and saved to {output_path}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: Drag and drop an image file onto the script, or provide the file path as an argument.")
        sys.exit(1)

    input_path = sys.argv[1]
    if not os.path.exists(input_path):
        print(f"Error: Input file '{input_path}' does not exist.")
        sys.exit(1)

    # Automatically generate the output path and set a default max dimension
    output_path = os.path.splitext(input_path)[0] + "_resized.jpg"
    max_dimension = 500  # Default maximum dimension

    resize_image(input_path, output_path, max_dimension)
