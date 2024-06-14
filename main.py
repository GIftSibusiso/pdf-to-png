from pdf2image import convert_from_path
import os


existing_folders = []

def create_images(filename):
    pdf_path = "pdfs/" + filename
    images = convert_from_path(pdf_path)
    folder, ext = filename.split(".")

    os.mkdir(folder)

    for i, image in enumerate(images):
        image.save(f"{folder}/page_{i + 1}.png", "PNG")


def remove_images(folder):
    images = os.listdir(folder)

    for image in images:
        os.remove(f"{folder}/{image}")
    
    os.rmdir(folder)


def convert_pdfs():
    pdfs = os.listdir("pdfs")

    if len(pdfs) == 0:
        print("No files were uploaded")

    for pdf in pdfs:
        folder_name = pdf.split(".")[0]
        if not os.path.exists(folder_name):
            create_images(pdf)
        else:
            print(f"'{pdf}' directory already exists as {folder_name}")
            existing_folders.append(pdf)


def are_digits(string: str) -> bool:
    values = string.split(",")

    for value in values:
        if value.strip().isdigit():
            continue

        return False
    
    return True


def duplicated_pdfs():
    if len(existing_folders) == 0:
        print("Successfully added all new pdfs")
        return
    
    print("\nExisting folders")
    for i in range(len(existing_folders)):
        print(f"{i+1}. {existing_folders[i]}")
    
    print("\nEnter pdf number seperated by commas, e.g 1,2,3 or 0 if you don't want to override the document")
    while not are_digits(consent:=input(f"Which pdfs would you like to override?").lower()) :
        pass

    if consent.strip() == "0":
        print("No pdfs were overriden")
        return
    
    for i in [int(value.strip()) for value in consent.split(",")]:
        if i > len(existing_folders) or i < 1:
            print(f"[{i}] Option non existant")
        else:
            folder, ext = existing_folders[i-1].split(".")
            remove_images(folder)
            create_images(existing_folders[i-1])


if __name__ == "__main__":
    if not os.path.exists("pdfs"):
        os.mkdir("pdfs")
        print("Navigate to 'pdf-to-png' folder then add your pdf files to the 'pdfs' folder")
    else:
        convert_pdfs()
        duplicated_pdfs()
