from tkinter import *
from tkinter import filedialog
from understandingPillow.pillow_wrapper import PillowWrapper


class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        # widget can take all window
        self.pack(fill=BOTH, expand=1)
        self.img = None
        self.pillowWrapper = PillowWrapper()

        # Buttons
        uploadButton = Button(root, text='Upload', command=self.uploadBtnAction)
        exitButton = Button(self, text="Exit", command=self.clickExitButton)
        thumbnailButton = Button(self, text="Thumb", command=self.thumbnailBtnAction)
        originalButton = Button(self, text="Original", command=self.originalSizeBtnAction)
        rotateRightButton = Button(self, text="Rotate -->", command=self.rotateRightBtnAction)
        rotateLeftButton = Button(self, text="Rotate <--", command=self.rotateLeftBtnAction)
        flipButton = Button(self, text="Flip", command=self.flipBtnAction)
        blackAndWhiteButton = Button(self, text="BnW", command=self.blackAndWhiteBtnAction)
        zoomInButton = Button(self, text="Zoom In", command=self.zoomInBtnAction)
        zoomOutButton = Button(self, text="Zoom Out", command=self.zoomOutBtnAction)

        addBorderButton = Button(self, text="Add Border", command=self.addBorderBtnAction)
        addBlurredEdgesButton = Button(self, text="Blurred Edges", command=self.addBlurredEdgesBtnAction)
        addWaterMarkButton = Button(self, text="Water Mark", command=self.addWaterMarkBtnAction)
        increaseContrastButton = Button(self, text="Beautify", command=self.increaseContrastBtnAction)
        saveButton = Button(self, text="Save", command=self.saveBtnAction)

        # Button coordinates in the UI.
        uploadButton.place(x=0, y=0)
        thumbnailButton.place(x=60, y=0)
        originalButton.place(x=120, y=0)
        rotateRightButton.place(x=180, y=0)
        rotateLeftButton.place(x=260, y=0)
        flipButton.place(x=340, y=0)
        blackAndWhiteButton.place(x=380, y=0)
        zoomInButton.place(x=440, y=0)
        zoomOutButton.place(x=500, y=0)
        addBorderButton.place(x=580, y=0)
        addBlurredEdgesButton.place(x=670, y=0)
        addWaterMarkButton.place(x=760, y=0)
        increaseContrastButton.place(x=840, y=0)
        saveButton.place(x=900, y=0)
        exitButton.place(x=1000, y=0)

    def clickExitButton(self):
        exit()

    def uploadBtnAction(self, event=None):
        filename = filedialog.askopenfilename()
        imagePath = filename.replace('/', '\\')
        render = self.pillowWrapper.openImage(imagePath)
        self._renderImage(render)

    def thumbnailBtnAction(self, event=None):
        render = self.pillowWrapper.thumbNail()
        self._renderImage(render)

    def originalSizeBtnAction(self, event=None):
        render = self.pillowWrapper.reset()
        self._renderImage(render)

    def rotateRightBtnAction(self, event=None):
        render = self.pillowWrapper.rotateRight()
        self._renderImage(render)

    def rotateLeftBtnAction(self, event=None):
        render = self.pillowWrapper.rotateLeft()
        self._renderImage(render)

    def flipBtnAction(self, event=None):
        render = self.pillowWrapper.flip()
        self._renderImage(render)

    def blackAndWhiteBtnAction(self, event=None):
        render = self.pillowWrapper.blackAndWhite()
        self._renderImage(render)

    def zoomInBtnAction(self, event=None):
        render = self.pillowWrapper.zoomInImage()
        self._renderImage(render)

    def zoomOutBtnAction(self, event=None):
        render = self.pillowWrapper.zoomOutImage()
        self._renderImage(render)

    def addBorderBtnAction(self, event=None):
        render = self.pillowWrapper.addBorder()
        self._renderImage(render)

    def addBlurredEdgesBtnAction(self, event=None):
        render = self.pillowWrapper.addBlurredEdges()
        self._renderImage(render)

    def addWaterMarkBtnAction(self, event=None):
        render = self.pillowWrapper.addWaterMark()
        self._renderImage(render)

    def increaseContrastBtnAction(self, event=None):
        render = self.pillowWrapper.increaseContrast()
        self._renderImage(render)

    def saveBtnAction(self, event=None):
        self.pillowWrapper.save()

    def _renderImage(self, render):
        if self.img is not None:
            self.img.destroy()
        self.img = Label(self, image=render)
        self.img.image = render
        self.img.place(x=250, y=100)


root = Tk()
app = Window(root)
root.wm_title("Understanding Pillow")
root.geometry("320x200")
root.mainloop()
