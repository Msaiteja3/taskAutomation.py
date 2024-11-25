import os
import shutil

def organize_files(directory):
    """Organizes files in the given directory into subfolders based on file type."""
    # Define file type categories
    file_types = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
        "Documents": [".txt", ".pdf", ".docx", ".xlsx"],
        "Audio": [".mp3", ".wav", ".aac"],
        "Video": [".mp4", ".avi", ".mov"],
        "Archives": [".zip", ".rar", ".tar", ".gz"],
        "Others": []
    }
    
    # Make sure the target directory exists
    if not os.path.exists(directory):
        print(f"Error: The directory {directory} does not exist.")
        return
    
    # Create subdirectories for each category if they don't already exist
    for category in file_types:
        category_path = os.path.join(directory, category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)
    
    # Iterate over all files in the given directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        # Skip directories
        if os.path.isdir(file_path):
            continue
        
        # Get the file extension and determine the category
        file_extension = os.path.splitext(filename)[1].lower()
        categorized = False
        
        for category, extensions in file_types.items():
            if file_extension in extensions:
                # Move the file to the corresponding category folder
                category_path = os.path.join(directory, category)
                shutil.move(file_path, os.path.join(category_path, filename))
                print(f"Moved: {filename} -> {category}")
                categorized = True
                break
        
        # If the file type does not match any category, move it to 'Others'
        if not categorized:
            category_path = os.path.join(directory, "Others")
            shutil.move(file_path, os.path.join(category_path, filename))
            print(f"Moved: {filename} -> Others")

if __name__ == "__main__":
    # Set the directory you want to organize
    directory_to_organize = input("Enter the directory path you want to organize: ")
    organize_files(directory_to_organize)
