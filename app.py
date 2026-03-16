# Import necessary modules from Flask and the custom 'image' module
from flask import Flask, render_template, request
import image  # Custom module for image processing and metadata extraction
import os # Standard Python library for interacting with the Operating System

# Initialize the Flask application
app = Flask(__name__)

# Route for the home page
@app.route("/", methods=["GET"])
def home_page():
    """
    Render the main landing page of the application.
    This route only accepts GET requests.
    """
    return render_template("index.html")

# Route to display the image upload page
@app.route("/upload_image", methods=["GET"])
def upload():
    """
    Render the image upload page where users can select an image file.
    This route uses GET method because it only serves the HTML form.
    """
    return render_template("upload_image.html")

# Route to handle image upload and display metadata results
@app.route("/results", methods=["GET", "POST"])
def results():
    """
    Handles both displaying the image page and processing uploaded images.
    
    GET request:
        - Render a default page or image form if needed.
    
    POST request:
        - Receive the uploaded image from the form.
        - Extract metadata using the 'image' module.
        - Render a results page displaying the metadata.
    """
    if request.method == "POST":
        # Retrieve the uploaded file from the form
        file = request.files.get("imagem")
        
        # Process the image to extract metadata
        metadata = image.view_metadata(file)
        
        # Render the results page and pass the metadata
        return render_template("view_metadata.html", metadados=metadata)
    
    # For GET requests, render a default index page
    return render_template("index.html")

# Entry point for running the Flask application
if __name__ == "__main__":
    # Retrieve the port from environment variables (defaulting to 10000 if not set)
    # This is essential for compatibility with hosting services like Render or Heroku
   port = int(os.environ.get("PORT", 10000))

   # Start the Flask development server
   app.run(host="0.0.0.0", port=port)