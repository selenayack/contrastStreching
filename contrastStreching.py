import numpy as np
import cv2
import pylab as plt
import matplotlib.image as mpimg
from math import log10, sqrt
import matplotlib.pyplot as plt

#bir görüntünün yogunluk degerlerini dinamik aralığa yayarak genişleterek kontrast iyileştirir,
# görüntünün maksimum yoğunluk değeri ile minimum yoğunluk değeri arasındaki farkı artırır,geri kalanı bu aralığa dağıtır
#histogram eşitleme uniform şekilde histogramı düzleştirmeye odaklanır

img = cv2.imread("./4.png",0)
#cv2.imwrite('1gray.jpg',imge)

x1 = np.min(img)#resimdeki en küçük ve en büyük piksel degerleri
x2 = np.max(img)

y1 = input("araligin minimum degerini girin : ")
y2 = input("araligin maksimum degerini girin : ")

index = len(img[0])#matris boyutu
oindex = len(img)
size = index*oindex

myimage = cv2.imread("./4.png",0)
i = j = 0
for i in range(oindex):
    for j in range(index):
        myimage[i][j] = ((img[i][j]-int(x1))*(((int(y2)-int(y1))/(int(x2)-int(x1)))+int(y1)))




#cv2.imshow('original',img)
#cv2.imshow('contrast streching',myimage)
#cv2.imwrite('lenastreching.jpg',myimage)




def PSNR(original, compressed):
    mse = np.mean((original - compressed) ** 2)
    if(mse == 0):
        return 100
    max_pixel = 255.0
    psnr = 20 * log10(max_pixel / sqrt(mse))
    return psnr
  
def main():
     original = cv2.imread("./4.png")
     compressed = cv2.imread("./4streching.jpg")
 
     value = PSNR(original, compressed)
     print(f"PSNR value is {value} dB")

     yanyana=np.hstack((original,compressed))

     histr = cv2.calcHist([original],[0],None,[256],[0,256])
     plt.plot(histr)
     plt.show()
    
     histr2 = cv2.calcHist([compressed],[0],None,[256],[0,256])
     plt.plot(histr2)
     plt.show()

     plt.imshow(yanyana,cmap="gray")
     plt.show()
 

    
       

if __name__ == "__main__":
    main()

cv2.waitKey(0)
cv2.destroyAllWindows()

