import cv2
import time
from tasks import *

def main():
    PsnrTestImage = cv2.imread("spot-filters/images/1.jpg")
    PsnrTestImage2 = cv2.imread("spot-filters/images/2.jpg")
    imageForShadeOfGrayFilter = cv2.imread("spot-filters/images/pic.jpg")
    imageForConverting = cv2.imread("spot-filters/images/pic.jpg")

    result = []

    result.append(task1(PsnrTestImage, PsnrTestImage2))
    result.append(task2(imageForShadeOfGrayFilter))
    result.append(task3(imageForConverting))
    with open("spot-filters/result/result.txt", "w") as file:
        print(result, file=file)

def brightnessIncreaseRGB(img, value=30):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)

    lim = 255 - value
    v[v > lim] = 255
    v[v <= lim] += value

    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return img

def brightnessIncreaseHSV(image, numberOfIncrease):
    result = np.array(image)
    for i in range(np.shape(image)[0]):
        for j in range(np.shape(image)[1]):
            if result[i][j][2] + numberOfIncrease > 100:
                result[i][j][2] = 100
            elif result[i][j][2] + numberOfIncrease < 0:
                result[i][j][2] = 0
            else:
                result[i][j][2] = result[i][j][2] + numberOfIncrease


def task1(image1, image2):
    task_result = []

    startTime = time.time()
    psnrResult = psnr(image1, image2)
    endTime = time.time() - startTime
    task_result.append(("Метрика сходства двух изображений", endTime, "psnr = " + str(psnrResult)))
    return task_result

def task2(image):
    task_result = []
    imgUMat = np.float32(image)

    startTime = time.time()
    averageResult = average(imgUMat)
    endTime = time.time() - startTime
    task_result.append(("Конвертация цветного изображения в монохромное изображение по формуле average", endTime, None))
    cv2.imwrite("spot-filters/result/AverageResult.jpg", averageResult)
    
    startTime = time.time()
    grayScaleCV = gray_scale_filter_cv(image)
    endTime = time.time() - startTime
    task_result.append(("Конвертация цветного изображения в монохромное изображение с помощью opencv", endTime, None))
    cv2.imwrite("spot-filters/result/grayScaleCVResult.jpg", grayScaleCV)

    startTime = time.time()
    psnrResult = psnr(averageResult, grayScaleCV)
    endTime = time.time() - startTime
    task_result.append(("Метрика сходства двух изображений", endTime, "psnr = " + str(psnrResult)))
    return task_result

def task3(image):
    task_result = []

    startTime = time.time()
    hsvImage = rgb2hsv(image)
    endTime = time.time() - startTime
    task_result.append(("Преобразование самопальной функцией", endTime, None))
    cv2.imwrite("spot-filters/result/HsvResult.jpg", hsvImage)

    startTime = time.time()
    opencvHsvImage = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    endTime = time.time() - startTime
    task_result.append(("Преобразование opencv функцией", endTime, None))
    cv2.imwrite("spot-filters/result/opencvHsvResult.jpg", opencvHsvImage)

    startTime = time.time()
    rgbIncreaseBrightness = brightnessIncreaseRGB(image, 51)
    endTime = time.time() - startTime
    task_result.append(("Увеличения яркости rgb", endTime, None))
    cv2.imwrite("spot-filters/result/rgbIncreaseBrightness.jpg", rgbIncreaseBrightness)

    startTime = time.time()
    hsvIncreaseBrightness = brightnessIncreaseHSV(opencvHsvImage, 20)
    endTime = time.time() - startTime
    task_result.append(("Увеличения яркости hsv", endTime, None))
    cv2.imwrite("spot-filters/result/hsvIncreaseBrightness.jpg", hsvIncreaseBrightness)

    return task_result

if __name__ == "__main__":
    main()