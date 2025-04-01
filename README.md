# Resize And Batch ImagES
pyinstaller --onefile  --icon=your_icon.ico resize-image.py

How to Use a Virtual Environment with pip:
Create a Virtual Environment: Run the following command in your project directory:
python -m venv rabies
This will create a virtual environment named rabies in your project directory.

Activate the Virtual Environment:

On Windows:
rabies\Scripts\activate

Deactivate the Virtual Environment: When you're done, deactivate the virtual environment by running:
deactivate


python -m venv rabies
rabies\Scripts\activate  # On Windows
source rabies/bin/activate  # On macOS/Linux
pip install -r requirements.txt


pip freeze > requirements.txt
