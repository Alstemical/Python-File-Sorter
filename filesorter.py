import os
import shutil

def organize_files():
    """Organize files in a directory into subfolders based on file type."""

    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
        'Documents': ['.pdf', '.docx', '.doc', '.txt', '.pptx', '.xlsx'],
        'Audio': ['.mp3', '.wav', '.flac', '.aac'],
        'Video': ['.mp4', '.mov', '.avi', '.mkv', '.wmv'],
        'Code': ['.py', '.js', '.html', '.css', '.c', '.cpp'],
        'Archives': ['.zip', '.rar', '.tar', '.gz']
    }

    try:
        source_dir = input("Enter the path of the directory to organize: ")

        if not os.path.isdir(source_dir):
            print("Error: The specified path does not exist.")
            return

    except Exception as e:
        print(f"an error occurred: {e}")
        return

    for folder_name in file_types.keys():
        dest_path = os.path.join(source_dir, folder_name)
        os.makedirs(dest_path, exist_ok=True)
        print(f"Created directory: {dest_path}")

    for filename in os.listdir(source_dir):

        if os.path.isdir(os.path.join(source_dir, filename)):
            continue

        # Get the file's extension
        file_extension = os.path.splitext(filename)[1].lower()

        # Assume a 'Misc' folder for files with unknown extensions
        destination_folder = 'Misc'

        # Find the correct folder based on the file extension
        for folder_name, extensions in file_types.items():
            if file_extension in extensions:
                destination_folder = folder_name
                break

        # Construct the full paths for the source and destination
        source_path = os.path.join(source_dir, filename)
        dest_path = os.path.join(source_dir, destination_folder)
        final_dest_path = os.path.join(dest_path, filename)

        try:
            # Move the file to its new location
            shutil.move(source_path, final_dest_path)
            print(f"moved '{filename}' to '{destination_folder}'")
        except Exception as e:
            print(f"Failed to move '{filename}': {e}")

    print("\nFile organization complete!")

organize_files()