import os
import urllib.request
import zipfile

# URL of the password-protected ZIP file
url = 'http://example.com/file.zip'

# Path where the downloaded ZIP file is saved
zip_path = 'C:/path/to/file.zip'

# Password for the ZIP file
password = 'yourpassword'

# Download the ZIP file
urllib.request.urlretrieve(url, zip_path)

# Extract the contents of the ZIP file
with zipfile.ZipFile(zip_path) as zip_file:
    # Set the password for the ZIP file
    zip_file.setpassword(password.encode())
    
    # Extract all the files to the current working directory
    zip_file.extractall()
    
# Remove the ZIP file after extraction
os.remove(zip_path)
