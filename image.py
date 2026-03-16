# Import Pillow library modules for image processing and EXIF metadata access
from PIL import Image, ExifTags

def view_metadata(file):
    """
    Extract and return EXIF metadata from an image file.
    
    Steps:
    1. Open the image file using Pillow (PIL).
    2. Retrieve EXIF metadata associated with the image.
    3. Convert EXIF tag codes to human-readable names when available.
    4. Store each tag and its value in a list of dictionaries.
    
    Parameters:
        ficheiro (str or file-like object): Path to the image file or file object.
        
    Returns:
        list[dict]: A list of dictionaries containing 'Tag' and 'Valor' keys
                    representing the metadata of the image.
    
    Example:
        metadata = ver_metadados("example.jpg")
        for item in metadata:
            print(item["Tag"], ":", item["Valor"])
    """
    
    # Open the image file
    im = Image.open(file)
    
    # Retrieve EXIF metadata; returns a dictionary-like object
    exif = im.getexif()
    
    # Prepare a list to store metadata in a readable format
    metadata_list = []
    
    # Iterate over each EXIF tag and its value
    for key, value in exif.items():
        # Convert tag code to human-readable name, fallback to code if unknown
        name = ExifTags.TAGS.get(key, key)
        # Append the tag and value as a dictionary to the list
        metadata_list.append({"Tag": name, "Value": value})
    
    # Return the list of metadata dictionaries
    return metadata_list