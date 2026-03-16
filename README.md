# 🖼️ Image Metadata Extractor

A simple application that allows you to upload an image and view its metadata.
Metadata can include information such as creation date, camera model, GPS location, resolution, format, and other EXIF data stored in the image.

## 🚀 Features

* Upload images via a user-friendly interface
* Automatic extraction of image metadata
* Organized display of EXIF data
* Support for multiple image formats (e.g., JPG, PNG)
* Simple and easy-to-use interface
* Lightweight backend using Python and Flask

## 📸 What is Metadata?

Metadata is additional information stored within an image file.
Depending on the image, it can include:

* 📅 Date and time of the photo
* 📷 Camera model
* 📍 GPS location
* 📐 Image resolution
* 🎞️ File format
* ⚙️ Camera settings (ISO, exposure, etc.)

## 🛠️ Technologies Used

This project uses the following technologies:

* **HTML / CSS**
* **Python**
* **Flask – web framework for the backend**
* **Pillow (PIL) – library for image manipulation and EXIF metadata extraction**

## 📂 Project Structure

image-metadata-extractor
│
├── static/                     
│   ├── imgs/                   
│   │   ├── first_image.png
│   │   └── image_upload.png
│   │
│   ├── anexar_imagem.css
│   ├── script.js
│   ├── style.css
│   └── ver_metadados.css
│
├── templates/                  
│   ├── index.html           
│   ├── upload_imagem.html
│   └── ver_metadados.html
│
├── app.py                      
├── image.py                    
├── README.md                   
└── requirements.txt            

## ⚙️ How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/seu-usuario/image-metadata-extractor.git
```

### 2. Enter the project folder

```bash
cd image-metadata-extractor
```

### 3. Install dependencies

```bash
pip install flask pillow
```

### 4. Run the application

```bash
python app.py
```

### 5. Open in your browser

http://127.0.0.1:10000

## ⚠️ Notes

* Not all images contain metadata.
* Some social media platforms remove metadata when uploading images.
* Support depends on the image format.

## 📌 Future Improvements

* Download metadata as **JSON**
* Display location on a map
* Support for more image formats
* Drag & Drop for image upload

## 👨‍💻 Author

Project developed by **[Ricardo Melo]**

## 📄 License

This project is licensed under the [MIT License](LICENSE).