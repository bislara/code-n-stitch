import os
import cv2
import typer

FILE_IN = ''
FILE_OUT = ''


def cartoonize(img_path: str, output_path:str = '', gui: bool = False):
   
   num_down = 3
   num_bilateral = 7 

   img=cv2.imread(img_path)
   # Image copy to work in
   img_copy = img

   edge = cv2.Canny(img_copy, 100, 200)
   
   # Scaling on pyramidal scaling
   for _ in range(num_down):
      img_copy = cv2.pyrDown(img_copy)

   for _ in range(num_bilateral):
      img_copy = cv2.bilateralFilter(img_copy, d=9, sigmaColor=9, sigmaSpace=7)

   for _ in range(num_down):
      img_copy = cv2.pyrUp(img_copy)

   # Blur Colors
   img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
   img_blur = cv2.medianBlur(img_gray, 7)

   # Draw Contours
   contours, _ = cv2.findContours(edge,
                                 cv2.RETR_EXTERNAL,
                                 cv2.CHAIN_APPROX_NONE)
   cv2.drawContours(img_copy, contours, -1, 0, thickness=1.5)

   if output_path != '':
      cv2.imwrite(output_path, img_copy)
   if gui:
      show_image(img_copy)


def show_image(image):
   cv2.namedWindow("cartoonized_window", cv2.WINDOW_KEEPRATIO)
   cv2.imshow("cartoonized_window", image)
   wait_time = 1000
   while cv2.getWindowProperty('cartoonized_window', cv2.WND_PROP_VISIBLE) >= 1:
      keyCode = cv2.waitKey(wait_time)
      if (keyCode & 0xFF) == ord("q"):
         cv2.destroyAllWindows()
         break

def main(input: str, output: str = '', gui: bool = False):
    if not os.path.isfile(input):
        raise Exception('File {} does not exist.'.format(input))
    if not input.lower().endswith(('.png', '.jpg', '.jpeg')):
        raise Exception('File type is not an image')
    FILE_IN = input
    if output != '':
        FILE_OUT = output
    else:
        new_path = input.split('.')
        new_path[-2] += '-cartoon'
        FILE_OUT = '.'.join(new_path)
    cartoonize(FILE_IN, FILE_OUT, gui)

if __name__ == "__main__":
    typer.run(main)