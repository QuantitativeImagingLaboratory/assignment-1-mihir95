class resample:

    def resize(self, image, fx = None, fy = None, interpolation = None):
        """calls the appropriate funciton to resample an image based on the interpolation method
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        interpolation: method used for interpolation ('either bilinear or nearest_neighbor)
        returns a resized image based on the interpolation method
        """

        if interpolation == 'bilinear':
            return self.bilinear_interpolation(image, fx, fy)

        elif interpolation == 'nearest_neighbor':
            return self.nearest_neighbor(image, fx, fy)

    def nearest_neighbor(self, image, fx, fy):
        """resizes an image using bilinear interpolation approximation for resampling
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        returns a resized image based on the nearest neighbor interpolation method
        """

       newW = 0
        newY = 0
        target = Image.new('RGB', (newW, newY), 'white')
        with Image.open("cell2.jpg") as image:
            w, h = image.size
        height, width, channels = scipy.ndimage.imread("cell2.jpg").shape

        for x in range(0, newW):
            for y in range(0, newY):
                srcX = int(round(float(x) / float(newW) * float(w)))
                srcY = int(round(float(y) / float(newY) * float(h)))
                srcX = min(srcX, w - 1)
                srcY = min(srcY, h - 1)
                pixel = image[target, x, y]
        return target


    def bilinear_interpolation(self, image, fx, fy):
        """resizes an image using bilinear interpolation approximation for resampling
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        returns a resized image based on the bilinear interpolation method
        """

        # Write your code for bilinear interpolation here
        rows, cols, colours = image.shape

        n_rows = int(round(rows * fx, 0))
        n_cols = int(round(cols * fy, 0))

        enlarged_img = np.ones((n_rows, n_cols, colours))

        for i in range(n_rows - 1):
            for j in range(n_cols - 1):
                x_coord = j / fx
                y_coord = i / fy

                xc = int(math.ceil(x_coord))
                xf = int(math.floor(x_coord))
                yc = int(math.ceil(y_coord))
                yf = int(math.floor(y_coord))

                W_xc = xc - x_coord
                W_xf = x_coord - xf
                W_yc = yc - y_coord
                W_yf = y_coord - yf

            enlarged_img[i, j, :] = 255 - np.around(W_xc * (W_yc * image[yf, xf, :] + W_yf * image[yc, xf, :]) + W_xf * (
            W_yc * image[yf, xc, :] + W_yf * image[yc, xc, :]), 0)

        return image


