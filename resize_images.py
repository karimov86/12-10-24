from pathlib import Path
from PIL import Image

if __name__ == '__main__':
    size = (1920, 1080)  # Background size
    character_size = (1200, 1200)
    images_dir = Path('./images')  # Directory containing original images
    new_dir = Path('./resized')   # Directory for resized images
    new_dir.mkdir(parents=True, exist_ok=True)

    for img_path in images_dir.iterdir():
        if img_path.is_file():  # Ensure it's a file
            try:
                with Image.open(img_path) as img:
                    img = img.convert("RGBA")  # Ensure consistent format (optional)
                    # img = img.resize(size)
                    img.thumbnail(character_size)  # Resize without preserving the aspect ratio
                    resized_path = new_dir / img_path.name  # New file path
                    img.save(resized_path, format="PNG", quality=85)  # Save resized image
                    print(f"Resized: {img_path.name}")
            except Exception as e:
                print(f"Failed to process {img_path.name}: {e}")