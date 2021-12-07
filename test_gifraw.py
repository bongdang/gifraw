# -*- coding:utf-8 -*-
"""
This Sample is for using GifRaw Demo. quick and dirty.
There are no width, filename, freespace,... etc checks.
Notice that all process is for getting transparent color.
"""

# Just import Main Class for Demo
from gifraw import GifRaw

def new_resize(fname: str, resized: int, saveto: str) -> None:
    """
    Resize pixel size is width.
    Show Some GIF file informations and ALPHA Colors of each frames.
    """
    import io
    import imageio
    from PIL import Image

    raw_gif = GifRaw(fname)
    
    #print(repr(raw_gif))

    print(f"\n[Input GIF file : {fname}]")
    print(f"BG Color Index = {raw_gif.logical_screen_desc.bg_color_index}")
    print(f"Is Color Table : {raw_gif.logical_screen_desc.has_color_table}")
    print(f"Color Table Size: {raw_gif.logical_screen_desc.color_table_size}")
    if raw_gif.logical_screen_desc.has_color_table:
        print(
            f"BG Color = {raw_gif.global_color_table.entries[0].red, raw_gif.global_color_table.entries[0].blue, raw_gif.global_color_table.entries[0].green}"
        )
    raw_gif.make_raw_image_list()
    if len(raw_gif.raw_img_list) > 1:
        new_frames = []
        idx = 0
        for raw_frame in raw_gif.raw_img_list:
            memio = io.BytesIO(raw_frame)
            outimg = Image.open(memio)
            outimg = outimg.convert("RGBA")
            if idx == 0:
                saved_img = outimg.copy()
            else:
                alpha_color = raw_gif.get_transparent_color(idx)
                print(f"Frame#{idx + 1:03} Alpha Color : {alpha_color}")
                alpha_color.append(255)
                pixdata = outimg.load()
                width, height = outimg.size
                """
                # Code below is important!
                # Changing Alpha color to Transparent color is Soution Key!
                """
                for y in range(height):
                    for x in range(width):
                        if pixdata[x, y] == tuple(alpha_color):
                            pixdata[x, y] = (255, 255, 255, 0)
                saved_img.alpha_composite(outimg)
                outimg = saved_img.copy()
            
            # dirty method 100000 for....
            outimg.thumbnail([resized, 1000000], Image.LANCZOS)
            new_frames.append(outimg)
            idx += 1
        outimg = new_frames[0]

        # using imageio is better! using PILLOW is also availavle. 
        new_fps = raw_gif.get_fps()
        imageio.mimsave(saveto, new_frames, fps=new_fps)


def main(filename:str, resize_to:int, saveto:str) -> None:
    new_resize(filename, resize_to, saveto)
    return


if __name__ == "__main__":
    import sys
    import time
    
    if len(sys.argv) != 4:
        print(f"\nUsage : python3 {sys.argv[0]} gif_filename:str resize_to:int new_gif_filename:str\n")
        exit(1)

    start = time.time()

    main(sys.argv[1], int(sys.argv[2]), sys.argv[3])
    
    print("{0:>16} : {1:.8f} Sec".format("All Process", time.time() - start))
    print("\n[Done!]")
