import datetime
import functools

s = datetime.datetime.utcnow()
import pyvips
print("PyVips module loaded in", datetime.datetime.utcnow() - s)

SOURCE_IMAGE = "../assets/source.jpg"
OVERLAY_IMAGE = "../assets/overlay.png"
RESULT_IMAGE = "watermarked.png"


def main_vips():
    source = pyvips.Image.new_from_file(SOURCE_IMAGE)
    overlay = pyvips.Image.new_from_file(OVERLAY_IMAGE)

    position_x, position_y = (source.width - overlay.width) // 2, (source.height - overlay.height) // 2

    watermarked = source.composite2( overlay, "over", x=position_x, y=position_y)
    watermarked.write_to_file(RESULT_IMAGE)


def watermark_only():
    source = pyvips.Image.new_from_file(SOURCE_IMAGE)
    overlay = pyvips.Image.new_from_file(OVERLAY_IMAGE)

    position_x, position_y = (source.width - overlay.width) // 2, (source.height - overlay.height) // 2

    import timeit
    to_test = functools.partial(source.composite2, overlay, "over", x=position_x, y=position_y)
    res = timeit.timeit(to_test, number=100000)
    print(res)

if __name__ == "__main__":
    main_vips()
    watermark_only()
