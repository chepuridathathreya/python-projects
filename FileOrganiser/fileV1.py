import os
file_types = {
    "jpg": "images",
    "jpeg": "images",
    "png": "images",
    "pdf": "documents",
    "docx": "documents",
    "txt": "documents",
    "mp3": "audio",
    "wav": "audio",
    "mp4": "videos",
    "avi": "videos"
}
files = os.listdir("messyfolder")
print(files)
for file in files:
    extension = file.split(".")[1]
    print(file, extension)
    if extension in file_types:
        folder_name = file_types[extension]
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        os.rename(os.path.join("messyfolder", file), os.path.join(folder_name, file))
