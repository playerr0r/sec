import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from PIL import Image
from math import log


# энтропия

q = 1

if (q == 1):
    # open file in ascii with russian language encoding
    file = "C:\\Code\\python\\security\\sec\\text.txt"
    f = open(file, "r", encoding="cp1251")
    text = f.read()


    # create dict of counts of each symbol
    a = range(0,256)
    a = dict.fromkeys(a,0)

    # count each symbol code
    for i in range(0,len(text)):
        a[ord(text[i])] += 1
    


    df = pd.DataFrame([(i,a[i]) for i in a.keys()], columns=["code", "times"])

    entropy = 0
    for i in range(0,len(df)):
        p = df["times"][i]/len(text)
        if p == 0:
            entropy += 0
        else: entropy += p * log(1/p,2)

    plt.rcParams['figure.figsize'] = [10, 10]
    plt.rcParams['figure.dpi'] = 100

    print("entropy is " + str(entropy))
    sns.barplot(x="code", y="times", data=df)
    plt.show()
            
# create list of rgb values of each pixel of the image
else:
    a = range(0,256)
    a = dict.fromkeys(a,0)
    filename = "C:\\Code\\python\\security\\sec\\blue.bmp"
    img = Image.open(filename)
    rgb_img = img.convert('RGB')
    rgb_values = []

    for x in range(img.size[0]):
        for y in range(img.size[1]):
            r,g,b = rgb_img.getpixel((x,y))
            rgb_values.append((r,g,b))

    df = []
    # create dict of counts of each rgb value
    for i in range(0,3):
        for j in range(0,len(rgb_values)):
            if rgb_values[j][i] in a:
                a[rgb_values[j][i]] += 1
        df.append(pd.DataFrame([(i,a[i]) for i in a.keys()], columns=["code", "times"]))
        a = dict.fromkeys(a,0)
    print(df)

    # count entropy of each colour
    for i in range(0,3):
        entropy = 0
        for j in range(0,len(df[i])):
            p = df[i]["times"][j]/len(rgb_values)
            if p == 0:
                entropy += 0
            else: entropy += p * log(1/p,2)
        print("entropy of colour " + str(i) + " is " + str(entropy))


    plt.rcParams['figure.figsize'] = [10, 10]
    plt.rcParams['figure.dpi'] = 100


    fig, axs = plt.subplots(3)
    fig.suptitle('RGB histograms')
    for i in range(0,3):
        axs[i].bar(df[i]["code"], df[i]["times"])
        # red = 0, green = 1, blue = 2
        axs[i].set_title("colour " + str(i))
    plt.show()
