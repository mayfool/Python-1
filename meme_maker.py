import sys

from PIL import ImageDraw, ImageFont, Image


def input_par():
    print('Enter the text to insert in image: ')
    text = str(input())
    print('Enter the desired size: ')
    size = int(input())
    print('Enter the color for the text(r, g, b): ')
    color_value = [int(i) for i in input().split(' ')]
    return text, size, color_value
    pass


def main():
    path_to_image = "file";
    image_file = Image.open(path_to_image + '.jpg')
    image_file = image_file.convert("RGBA")
    pixdata = image_file.load()

    print(image_file.size)
    text, size, color_value = input_par()

    font = ImageFont.truetype("C:\\Windows\\Fonts\\ARIALN.ttf", size=size)

    # Clean the background noise, if color != white, then set to black.
    # change with your color
    for y in range(100):
        for x in range(100):
            pixdata[x, y] = (255, 255, 255, 255)
    #image_file.show()

    # Drawing text on the picture
    draw = ImageDraw.Draw(image_file)
    draw.text((50, 50), text, (color_value[0], color_value[1], color_value[2]),font=font)
    draw = ImageDraw.Draw(image_file)

    print('Enter the file name: ')
    file_name = str(input())
    image_file.save(file_name + ".jpg")
    pass


if __name__ == '__main__':
    main()
