import datetime
import functools

s = datetime.datetime.utcnow()
from PIL import Image
print("Pillow module loaded in", datetime.datetime.utcnow() - s)

SOURCE_IMAGE = "../assets/source.jpg"
OVERLAY_IMAGE = "../assets/overlay.png"
RESULT_IMAGE = "watermarked_pillow.png"


def main_pil():
    source = Image.open(SOURCE_IMAGE)
    overlay = Image.open(OVERLAY_IMAGE)

    position_x, position_y = (source.width - overlay.width) // 2, (source.height - overlay.height) // 2
    source.paste(overlay, (position_x, position_y), overlay)
    source.save(RESULT_IMAGE)


def watermark_only():
    source = Image.open(SOURCE_IMAGE)
    overlay = Image.open(OVERLAY_IMAGE)

    position_x, position_y = (source.width - overlay.width) // 2, (source.height - overlay.height) // 2

    import timeit
    to_test = functools.partial(source.paste, overlay, (position_x, position_y), overlay)
    res = timeit.timeit(to_test, number=100000)
    print(res)


if __name__ == "__main__":
    main_pil()
    watermark_only()
