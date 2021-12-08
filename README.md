# gifraw
GIF file raw reading library.

# Simple Usage
'''

    from gifraw import GifRaw

    # open gif file
    raw_gif = GifRaw('test.gif')
    # make image frames(writable single gif file) list
    raw_gif.make_raw_image_list()

    # handle each images... and make new image frames
    ....

    # get fps for imageio
    new_fps = raw_gif.get_fps()
    # use imageio for animated gif file save
    imageio.mimsave(saveto, new_frames, fps=new_fps)

'''

# Made for Animated GIF resizing
Because lack of PILLOW/imageio resizing gif, wrote this code.
See test_gifraw.py for demo.

# The key point is...
getting transparent color index and its colors. the gifraw module is for it.

# And, Generator
Frankly speeking, without generator gif file handling is more easier. but, for someone this approching will be an interesting issue.

# Don't forget
This is for demo. hope helping you.
