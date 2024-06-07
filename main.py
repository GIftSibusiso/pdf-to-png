from pdf2image import convert_from_path
import os

def create_images(filename):
    pdf_path = "pdfs/" + filename
    images = convert_from_path(pdf_path)
    folder, ext = filename.split(".")

    
    if not os.path.exists(folder):
        os.mkdir(folder)
    else: 
        while consent:=input(f"'{filename}' already created\nDo you want to override(y/n): ").lower() not in ["y", "n", "yes", "no"] :
            pass

        if consent in ["no", "n"]:
            return 
        
        remove_images(folder)

    for i, image in enumerate(images):
        image.save(f"{folder}/page_{i + 1}.png", "PNG")


def remove_images(folder):
    images = os.listdir(folder)

    for image in images:
        os.remove(f"{folder}/{image}")


def convert_pdfs():
    pdfs = os.listdir("pdfs")

    if len(pdfs) == 0:
        print("No files were uploaded")

    for pdf in pdfs:
        create_images(pdf)


if __name__ == "__main__":
    if not os.path.exists("pdfs"):
        os.mkdir("pdfs")
        print("Navigate to 'pdf-to-png' folder then add your pdf files to the 'pdfs' folder")
    else:
        convert_pdfs()
