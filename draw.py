from PIL import Image, ImageDraw

def create_images():
    # 24 rows, 20 cols = 480 checkboxes + empty
    for num in range(0,481):
        create_image(num)

def create_image(num):
    img = Image.new('L', (600,800), color = 255)
    d = ImageDraw.Draw(img)

    x0 = 10
    y0 = 18
    w = 25
    px = 4
    py = 7


    for rowId in range(0,24):
        for colId in range(0,20):
            fill = 0 if num > ((rowId*20) + colId) else 255
            x = x0 + colId * (w +px)
            y = y0 + rowId * (w+py)
            # draw outine by default and only fill if needed
            d.rectangle((x+1,y+1, x+w-1, y+w-1), fill=fill, outline = 0, width=1)
    
    img.save( f'{num}.png')
        

if __name__ == '__main__':
    create_images()
    