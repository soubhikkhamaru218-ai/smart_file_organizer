
from pathlib import Path
import shutil

# Folder containing the files to organize
source_folder = Path("test_files")

# File extensions and their categories
categories = {
    ".pdf": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    ".xlsx": "Documents",
    ".pptx": "Documents",

    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".webp": "Images",

    ".mp4": "Videos",
    ".mkv": "Videos",
    ".mov": "Videos",

    ".mp3": "Audio",
    ".wav": "Audio",
    ".m4a": "Audio",

    ".zip": "Archives",
    ".rar": "Archives",
    ".7z": "Archives",

    ".py": "Code",
    ".html": "Code",
    ".css": "Code",
    ".js": "Code",
}

# Check whether the source folder exists
if not source_folder.exists():
    print("Error: test_files folder does not exist.")

else:
    # Display files that will be organized
    print("\nSMART FILE ORGANIZER")
    print("-" * 30)

    files_found = 0

    for file in source_folder.iterdir():
        if file.is_file():
            files_found += 1

            category = categories.get(file.suffix.lower(), "Others")
            print(f"{file.name}  ->  {category}")

    if files_found == 0:
        print("No files found in the folder.")

    else:
        # Ask for permission before moving files
        choice = input("\nMove these files? Type YES to continue: ")

        if choice == "YES":

            moved_count = 0

            for file in source_folder.iterdir():

                if not file.is_file():
                    continue

                category = categories.get(
                    file.suffix.lower(), "Others"
                )

                # Create the category folder
                destination_folder = source_folder / category
                destination_folder.mkdir(exist_ok=True)

                # Choose a destination that does not overwrite a file
                destination = destination_folder / file.name
                number = 1

                while destination.exists():
                    destination = destination_folder / (
                        f"{file.stem}_{number}{file.suffix}"
                    )
                    number += 1

                try:
                    shutil.move(str(file), str(destination))
                    print(f"Moved: {file.name} -> {category}")
                    moved_count += 1

                except OSError as error:
                    print(f"Could not move {file.name}: {error}")

            print(f"\nFinished! Files moved: {moved_count}")

        else:
            print("Cancelled. No files were moved.")
