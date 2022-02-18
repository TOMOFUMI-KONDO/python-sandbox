from PIL import Image, ImageFont, ImageDraw
import cv2
import numpy as np


def img_add_msg(img, message):
  font = ImageFont.truetype(font='/Library/Fonts/Arial Unicode.ttf', size=24)
  img_pil = Image.fromarray(img)

  draw = ImageDraw.Draw(img_pil)
  draw.text((50, 50), message, font=font, fill=(255, 255, 255, 0))

  img_cv2 = np.array(img_pil)
  return img_cv2


def main():
  img = cv2.imread('image/source.jpg', 1)  # load color image

  print('Input embed text: ', end="")
  message = input()

  img_embed_text = img_add_msg(img, message)
  cv2.imwrite('image/output.jpg', img_embed_text)


if __name__ == "__main__":
  main()
