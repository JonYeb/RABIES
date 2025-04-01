from PIL import Image
import sys
import os
import re
from datetime import datetime
from dotenv import load_dotenv  # Import the dotenv library

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
            resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

            # Save the resized image
            resized_img.save(output_path)
            print(f"Image resized and saved to {output_path}")

    except Exception as e:
        print(f"Error: {e}")

def extract_date_from_filename(filename):
    """
    Extracts the date in YYYY-MM-DD format from the input filename.

    :param filename: The input filename.
    :return: The extracted date as a string, or None if no date is found.
    """
    match = re.search(r"(\d{4}-\d{2}-\d{2})", filename)
    return match.group(1) if match else None

if __name__ == "__main__":
    # Load environment variables from .env file
    load_dotenv()

    if len(sys.argv) < 2:
        print("Usage: Drag and drop an image file onto the script, or provide the file path as an argument.")
        sys.exit(1)

    input_path = sys.argv[1]
    if not os.path.exists(input_path):
        print(f"Error: Input file '{input_path}' does not exist.")
        sys.exit(1)

    # Read max_dimension from .env file, default to 500 if not set
    max_dimension = int(os.getenv("MAX_DIMENSION", 500))

    # Extract the date from the input filename
    input_filename = os.path.basename(input_path)
    extracted_date = extract_date_from_filename(input_filename)

    if extracted_date:
        # Write the extracted date to 1.txt
        with open("1.txt", "w") as date_file:
            date_file.write(extracted_date)
        print(f"Date '{extracted_date}' extracted and written to 1.txt")
    else:
        # Write the current date to 1.txt
        current_date = datetime.now().strftime("%Y-%m-%d")
        with open("1.txt", "w") as date_file:
            date_file.write(current_date)
        print(f"No date found in the input filename. Current date '{current_date}' written to 1.txt")

    # Set the output path to 1.jpg
    output_path = "1.jpg"

    resize_image(input_path, output_path, max_dimension)
    input("Press Enter to exit...")
