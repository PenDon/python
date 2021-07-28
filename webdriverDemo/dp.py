from PIL import Image
img1 = Image.open("captchal.png", "r")
img2 = Image.open("captchal1.png", "r")
# img1.show()
# print(img1.size, img2.size)
size = img1.size
width = list(size)[0]
height = list(size)[1]
pix1 = img1.load()
pix2 = img2.load()


# print(pix1[200,10])
# print(pix1[200,10][1])
# pix像素下标从0开始

l = []
for i in range(width):
    for j in range(height):
        if abs(pix1[i, j][1] - pix2[i, j][1]) > 60 :
            l.append(i)
            break
print(l)
img1.paste((0,0,0,255), (77, 0, 78, 150))
img1.paste((0,0,0,255), (l[0], 0, l[0] + 1, 150))
img1.show()
# 每次的滑动块的位置和大小应该是一致的，width为6 ->