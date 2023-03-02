import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from PIL import Image


# энтропия

q = 1

if (q == 1):
    a = range(0,1200)
    a = dict.fromkeys(a,0)
    filename = "C:\\Code\\python\\security\\text.txt"
    file_ = open(filename, "r")
    text = file_.read()

    for l in text:
        l = ord(l)
        if l in a:
            a[l] += 1
            
# create list of rgb values of each pixel of the image
else:
    a = range(0,256)
    a = dict.fromkeys(a,0)
    filename = "C:\\Code\\python\\security\\test.png"
    img = Image.open(filename)
    rgb_img = img.convert('RGB')
    rgb_values = []

    for x in range(img.size[0]):
        for y in range(img.size[1]):
            r,g,b = rgb_img.getpixel((x,y))
            rgb_values.append((r,g,b))

    # red = 0, green = 1, blue = 2
    colour = 0
    if colour == 3: 
        print(rgb_values)
    for i in rgb_values:
        if i[colour] not in a:
            a.update({i[colour]:0})
        if i[colour] in a:
            a[i[colour]] += 1

df = pd.DataFrame([(i,a[i]) for i in a.keys()], columns=["code", "times"])

# plot the histogram
sns.barplot(x="code", y="times", data=df)
plt.show()
