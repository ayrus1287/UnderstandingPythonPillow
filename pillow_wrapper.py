from PIL import Image, ImageTk, ImageEnhance, ImageOps, ImageFilter, ImageDraw, ImageFont


class PillowWrapper(object):
    """
    A wrapper for the pillow package
    """

    def __init__(self, path=None):
        """
        Parameters:
        -----------
        path: Path of the image stored in your machine
        """
        self.path = path
        self.image = None
        self.imageOriginal = None
        self.baseWidth = None

    def openImage(self, path):
        """
        Open an image using the given path.

        Parameters:
        -----------
        path: str

        Returns:
        --------
        render: PIL.ImageTk.PhotoImage
        """
        self.path = path
        self.image = self.imageOriginal = Image.open(self.path)
        self.baseWidth = self.image.width

        render = ImageTk.PhotoImage(self.image)
        return render

    def reset(self):
        self.image = self.imageOriginal

        render = ImageTk.PhotoImage(self.image)
        return render

    def thumbNail(self, ):
        """
        Resize the image.

        Parameters:
        -----------

        Returns:
        --------
        render: PIL.ImageTk.PhotoImage
        """
        # Size tuple(width, height)
        self.image = self.image.resize((200, 200))

        render = ImageTk.PhotoImage(self.image)
        return render

    def cropImage(self):
        """
        Crop the image.

        Returns:
        --------
        render: PIL.ImageTk.PhotoImage
        """
        # tuple of coordinates of the box in the image to crop (left, upper, right, lower)
        box = (200, 300, 700, 600)
        self.image = self.image.crop(box)

        render = ImageTk.PhotoImage(self.image)
        return render

    def rotateRight(self):
        """
        Rotate the image to the right by 90 degrees.

        Returns:
        --------
        render: PIL.ImageTk.PhotoImage
        """
        self.image = self.image.rotate(-90)

        render = ImageTk.PhotoImage(self.image)
        return render

    def rotateLeft(self):
        """
        Rotate the image to the left by 90 degrees.

        Returns:
        --------
        render: PIL.ImageTk.PhotoImage
        """
        self.image = self.image.rotate(90)

        render = ImageTk.PhotoImage(self.image)
        return render

    def flip(self):
        """
        Flip the image from left to right

        Returns:
        --------
        render: PIL.ImageTk.PhotoImage
        """
        # You can use PIL.Image.FLIP_LEFT_RIGHT, PIL.Image.FLIP_TOP_BOTTOM, PIL.Image.ROTATE_90,
        # PIL.Image.ROTATE_180, PIL.Image.ROTATE_270 PIL.Image.TRANSPOSE or PIL.Image.TRANSVERSE.
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)

        render = ImageTk.PhotoImage(self.image)
        return render

    def blackAndWhite(self):
        """
        Change the mode of the image to greyScale
        It supports conversions between L (greyscale), RGB, and CMYK (cyan, magenta, yellow and black inks) modes.
        Returns:
        --------
        render: PIL.ImageTk.PhotoImage
        """
        self.image = self.image.convert('L')

        render = ImageTk.PhotoImage(self.image)
        return render

    def save(self):
        """
        Zoom out on an Image.

        Returns:
        --------
        render: PIL.ImageTk.PhotoImage
        """
        # set the base width of the result
        path = 'C:\\Users\\admin\\Desktop\\modified.jpg'
        self.image.save(path)

    # ------------------------------------------------------------------------------------------------------------------
    # Some Cool things you can do
    # ------------------------------------------------------------------------------------------------------------------

    def zoomInImage(self):
        """
        Zoom in on an Image.

        Returns:
        --------
        render: PIL.ImageTk.PhotoImage
        """
        self.baseWidth += 50
        img = self.image
        # determining the height ratio
        wpercent = (self.baseWidth / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        # resize image and save
        img = img.resize((self.baseWidth, hsize), Image.ANTIALIAS)

        render = ImageTk.PhotoImage(img)
        return render

    def zoomOutImage(self):
        """
        Zoom out on an Image.

        Returns:
        --------
        render: PIL.ImageTk.PhotoImage
        """
        # set the base width of the result
        self.baseWidth -= 50
        img = self.image
        # determining the height ratio
        wpercent = (self.baseWidth / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        # resize image and save
        img = img.resize((self.baseWidth, hsize), Image.ANTIALIAS)

        render = ImageTk.PhotoImage(img)
        return render

    def addBorder(self):
        """
        Add borders to the image

        Returns:
        --------
        render: PIL.ImageTk.PhotoImage
        """
        color = "green"
        # top, right, bottom, left
        border = (20, 10, 20, 10)
        self.image = ImageOps.expand(self.image, border=border, fill=color)

        render = ImageTk.PhotoImage(self.image)
        return render

    def addBlurredEdges(self):
        """
        Add blurred edges

        Returns:
        --------
        render: PIL.ImageTk.PhotoImage
        """
        # blur radius and diameter
        radius, diameter = 20, 40
        # open an image
        img = self.image
        # Paste image on white background
        background_size = (img.size[0] + diameter, img.size[1] + diameter)
        background = Image.new('RGB', background_size, (255, 255, 255))
        background.paste(img, (radius, radius))
        # create new images with white and black
        mask_size = (img.size[0] + diameter, img.size[1] + diameter)
        mask = Image.new('L', mask_size, 255)
        black_size = (img.size[0] - diameter, img.size[1] - diameter)
        black = Image.new('L', black_size, 0)
        # create blur mask
        mask.paste(black, (diameter, diameter))
        # Blur image and paste blurred edge according to mask
        blur = background.filter(ImageFilter.GaussianBlur(radius / 2))
        background.paste(blur, mask=mask)

        render = ImageTk.PhotoImage(background)
        return render

    def addWaterMark(self):
        """
        Add watermark to an image

        Returns:
        --------
        render: PIL.ImageTk.PhotoImage
        """
        img = self.image

        # get image size
        img_width, img_height = img.size

        # 5 by 4 water mark grid
        wm_size = (int(img_width * 0.20), int(img_height * 0.25))
        wm_txt = Image.new("RGBA", wm_size, (255, 255, 255, 0))

        # set text size, 1:40 of the image width
        font_size = int(img_width / 40)

        # load font e.g. gotham-bold.ttf
        font = ImageFont.truetype("arial.ttf", font_size)
        d = ImageDraw.Draw(wm_txt)
        wm_text = "@Surya"

        # centralize text
        left = (wm_size[0] - font.getsize(wm_text)[0]) / 2
        top = (wm_size[1] - font.getsize(wm_text)[1]) / 2

        # RGBA(0, 0, 0, alpha) is black
        # alpha channel specifies the opacity for a colour
        alpha = 75

        # write text on blank wm_text image
        d.text((left, top), wm_text, fill=(0, 0, 0, alpha), font=font)
        # uncomment to rotate watermark text
        # wm_txt = wm_txt.rotate(15,  expand=1)
        # wm_txt = wm_txt.resize(wm_size, Image.ANTIALIAS)

        for i in range(0, img_width, wm_txt.size[0]):
            for j in range(0, img_height, wm_txt.size[1]):
                img.paste(wm_txt, (i, j), wm_txt)

        render = ImageTk.PhotoImage(img)
        return render

    def increaseContrast(self):
        """
        Increase Contrast of the image.

        Returns:
        --------
        render: PIL.ImageTk.PhotoImage
        """
        im = self.image

        # image brightness enhancer
        enhancer = ImageEnhance.Contrast(im)

        '''
        factor = 1  # gives original image
        im_output = enhancer.enhance(factor)

        factor = 0.5  # decrease constrast
        im_output = enhancer.enhance(factor)
        '''

        factor = 1.5  # increase contrast
        im_output = enhancer.enhance(factor)

        render = ImageTk.PhotoImage(im_output)
        return render
