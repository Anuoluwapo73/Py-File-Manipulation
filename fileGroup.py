import os  # talks to the operating system
import shutil  # moves files

folder_path = r"C:\Users\Anu_Shoyode\OneDrive\Desktop\Desktop\my_projects\automation\testFiles"

files = os.listdir(folder_path)

rules = {
    ".pdf": "PDFs",
    ".mp4": "Video",
    ".png": "Image"
}

print("Automation started...\n")

for file in files:
    for ext, folder in rules.items():
        if file.endswith(ext):
            target_folder = folder_path + "/"+folder
            os.makedirs(target_folder, exist_ok=True)

            shutil.move(
                folder_path + "/" + file,
                target_folder + "/" + file
            )
            print(f"Moved: {file}")
            break
print("\nAutomation completed.")

# for file in files:
#     if file.endswith(".pdf"):
#         pdf_folder = folder_path + "/PDFs"
#         os.makedirs(pdf_folder, exist_ok=True)
#         shutil.move(
#             folder_path + "/" + file,
#             pdf_folder + "/" + file
#         )
#         print(f"Moved: {file}")
#     elif file.endswith(".mp4"):
#         video_folder = folder_path + "/Video"
#         os.makedirs(video_folder, exist_ok=True)
#         shutil.move(
#             folder_path + "/" + file,
#             video_folder + "/" + file
#         )
#         print(f"Moved: {file}")
#     elif file.endswith(".png"):
#         image_folder = folder_path + "/Image"
#         os.makedirs(image_folder, exist_ok=True)
#         shutil.move(
#             folder_path + "/" + file,
#             image_folder + "/" + file
#         )
#         print(f"Moved: {file}")


# print("\nAutomation completed.")
