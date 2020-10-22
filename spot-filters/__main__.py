import cv2
import time
from tasks import *

def main():
    firstImageForPsnrTest = cv2.imread("spot-filters/images/1.jpg")
    secondImageForPsnrTest = cv2.imread("spot-filters/images/2.jpg")
    imageForShadeOfGrayFilter = cv2.imread("images/pic.jpg")
    imageForConverting = cv2.imread("images/pic.jpg")

    result = []

    result.append(task1(firstImageForPsnrTest, secondImageForPsnrTest))
    # result.append(task2(imageForShadeOfGrayFilter))
    # result.append(task3(imageForConverting))
    with open("spot-filters/result/result.txt", "w") as file:
        print(result, file=file)


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

# def task_2(image):
#     task_result = []

#     startTime = time.time()
#     averageResult = average(image)
#     endTime = time.time() - startTime
#     task_result.append(("Конвертация цветного изображения в монохромное изображение по формуле average", endTime, None))
#     cv2.imwrite("result/AverageResult.jpg", averageResult)
    
#     startTime = time.time()
#     grayScaleCV = gray_scale_filter_cv(image)
#     endTime = time.time() - startTime
#     task_result.append(("Конвертация цветного изображения в монохромное изображение с помощью opencv", endTime, None))
#     cv2.imwrite("result/grayScaleCVResult.jpg", grayScaleCV)

#     startTime = time.time()
#     psnrResult = psnr(averageResult, grayScaleCV)
#     endTime = time.time() - startTime
#     task_result.append(("Метрика сходства двух изображений", endTime, "psnr = " + str(psnrResult)))
#     return task_result

# def task_3(image):
#     task_result = []

#     startTime = time.time()
#     hsvImage = rbg2hsv(image)
#     endTime = time.time() - startTime
#     task_result.append(("Преобразование самопальной функцией", endTime, None))
#     cv2.imwrite("result/HsvResult.jpg", hsvImage)

#     startTime = time.time()
#     opencvHsvImage = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
#     endTime = time.time() - startTime
#     task_result.append(("Преобразование opencv функцией", endTime, None))
#     cv2.imwrite("result/opencvHsvResult.jpg", opencvHsvImage)

#     startTime = time.time()
#     rgbIncreaseBrightness = brightnessIncreaseRGB(image, 51)
#     endTime = time.time() - startTime
#     task_result.append(("Увеличения яркости rgb", endTime, None))
#     cv2.imwrite("result/rgbIncreaseBrightness.jpg", rgbIncreaseBrightness)

#     startTime = time.time()
#     hsvIncreaseBrightness = brightnessIncreaseHSV(opencvHsvImage, 20)
#     endTime = time.time() - startTime
#     task_result.append(("Увеличения яркости hsv", endTime, None))
#     cv2.imwrite("result/hsvIncreaseBrightness.jpg", hsvIncreaseBrightness)

#     return task_result

if __name__ == "__main__":
    main()