import os
import shutil

def organize_folder(folder_path):
    file_types = {
        'Images': ['.jpg', '.png', '.jpeg', '.gif'],
        'Documents': ['.pdf', '.docx', '.txt', '.csv'],
        'Videos': ['.mp4', '.avi', '.mov']
    }

    for filename in os.listdir(folder_path):
        file_ext = os.path.splitext(filename)[1]
        for folder, extensions in file_types.items():
            if file_ext.lower() in extensions:
                folder_dir = os.path.join(folder_path, folder)
                os.makedirs(folder_dir, exist_ok=True)
                shutil.move(os.path.join(folder_path, filename), folder_dir)

if __name__ == "__main__":
    folder_path = input("Enter the folder path to organize: ")
    organize_folder(folder_path)
    print(f"Folder '{folder_path}' has been organized.")
