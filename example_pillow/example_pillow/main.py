from PIL import Image

SOURCE_IMAGE = "../assets/source.jpg"
OVERLAY_IMAGE = "../assets/overlay.png"
RESULT_IMAGE = "watermarked_pillow.png"


def main_pil():
    source = Image.open(SOURCE_IMAGE)
    overlay = Image.open(OVERLAY_IMAGE)

    position_x, position_y = (source.width - overlay.width) // 2, (source.height - overlay.height) // 2
    source.paste(overlay, (position_x, position_y), overlay)
    source.save(RESULT_IMAGE)


if __name__ == "__main__":
    main_pil()
