import os
from PIL import Image

def images_to_pdfs(images_dir): 
    files = os.listdir(images_dir)
     
    image_files = [f for f in files if f.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif', 'tiff'))]
 
    pdf_dir = os.path.join(images_dir, "pdfs")
    if not os.path.exists(pdf_dir):
        os.makedirs(pdf_dir)
    
    for image_file in image_files:
        image_path = os.path.join(images_dir, image_file)
        output_name = os.path.splitext(image_file)[0] + '.pdf'
        output_path = os.path.join(pdf_dir, output_name)

        with Image.open(image_path) as img:
            img.convert('RGB').save(output_path, 'PDF')

    print(f"{len(image_files)} images converted to PDFs!")

if __name__ == '__main__':
    images_to_pdfs('images')
