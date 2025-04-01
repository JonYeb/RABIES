# Resize And Batch Images (RABIES)

This project provides a Python script to resize images and upload them to a Google Cloud Storage bucket. It includes instructions for setting up a virtual environment, managing dependencies, and configuring Google Cloud credentials.

---

## How to Use

### 1. Create a Virtual Environment
Run the following command in your project directory to create a virtual environment:
```bash
python -m venv rabies
```
This will create a virtual environment named `rabies` in your project directory.

### 2. Activate the Virtual Environment
- **On Windows**:
  ```bash
  rabies\Scripts\activate
  ```
- **On macOS/Linux**:
  ```bash
  source rabies/bin/activate
  ```

### 3. Install Dependencies
After activating the virtual environment, install the required dependencies:
```bash
pip install -r requirements.txt
```

### 4. Deactivate the Virtual Environment
When you're done working, deactivate the virtual environment by running:
```bash
deactivate
```

---

## Managing Dependencies

### Freeze Dependencies
To save the current dependencies to a `requirements.txt` file, run:
```bash
pip freeze > requirements.txt
```

---

## Setting Up Google Cloud Credentials

### 1. Create a Service Account
- Go to the [Google Cloud Console](https://console.cloud.google.com/).
- Create a service account in your project.
- Download the JSON key file for the service account.

### 2. Set the `GOOGLE_APPLICATION_CREDENTIALS` Environment Variable
Set the environment variable to the path of your service account JSON key file:
```bash
set GOOGLE_APPLICATION_CREDENTIALS="path\to\your\service-account-key.json"
```

Alternatively, you can add this to a `.env` file in your project:
```plaintext
GOOGLE_APPLICATION_CREDENTIALS=path\to\your\service-account-key.json
```

---

## Building the Executable

To create a standalone executable for the script, use `PyInstaller`:
```bash
pyinstaller --onefile --icon=your_icon.ico resize-image.py
```

The executable will be located in the `dist` folder.

---

## Notes

- Ensure that the `.env` file is properly configured if you're using it to manage environment variables.
- The script requires the `Pillow` and `google-cloud-storage` libraries, which are included in the `requirements.txt` file.

---

## Example Workflow

1. Activate the virtual environment:
   ```bash
   rabies\Scripts\activate
   ```
2. Run the script:
   ```bash
   python resize-image.py path\to\your\image.jpg
   ```
3. The resized image (`1.jpg`) and the extracted date (`1.txt`) will be uploaded to the configured Google Cloud Storage bucket.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
