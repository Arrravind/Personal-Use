from PIL import Image

def resize_image(sizel, size2) :
    image = Image.open('d:\\MOVIES\\TAMIL\\jpg.jpg')

    print("Current size : {",image.size,"}" )

    resized_image = image.resize(( sizel, size2))
    
    resized_image.save('image' + str(size1) + '.png')

    print("After Resized :{",resized_image.size,"}")

size1 = int(input('Enter Width: '))
size2 = int(input('Enter Length: '))
resize_image(size1, size2)
