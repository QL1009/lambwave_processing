import cv2
import numpy as np


# 读取图像
# IMREAD_GRAYSCALE参数表示将图像转换为灰度图像，以便于后续处理
image = cv2.imread('Files/S/4.jpg', cv2.IMREAD_GRAYSCALE)

# 显示原始图像
# 使用imshow()函数显示原始的C扫描图像，方便观察图像内容
cv2.imshow('原始C扫图像', image)
cv2.waitKey(0)

# 定义高斯核大小和标准差
kernel_size = 3
sigma = 0.5

# 生成高斯核
kernel = np.zeros((kernel_size, kernel_size))
center = kernel_size // 2
for i in range(kernel_size):
    for j in range(kernel_size):
        x = i - center
        y = j - center
        kernel[i, j] = np.exp(-(x ** 2 + y ** 2) / (2 * sigma ** 2))
kernel /= kernel.sum()

# 显示生成的高斯核,以便观察核的形状和权重分布
print("高斯卷积核:")
print(kernel)

# 进行卷积运算
filtered_image = cv2.filter2D(image, -1, kernel)

# 显示滤波后的图像
cv2.imshow('高斯滤波后的C扫图像', filtered_image)
cv2.waitKey(0)

# 检测灰度集中的位置（缺陷区域）
defect_threshold = 4  # 缺陷灰度阈值
defect_mask = np.where(filtered_image < defect_threshold, 255, 0).astype(np.uint8)

# 在原始图像上涂黑缺陷区域,通过逻辑与运算实现。
defect_area = cv2.bitwise_and(image, image, mask=defect_mask)

# 涂白非缺陷区域 通过逻辑取反操作实现
non_defect_area = cv2.bitwise_not(defect_mask)
non_defect_area_image = cv2.bitwise_and(image, image, mask=non_defect_area)
result = non_defect_area

# 显示最终经边界化处理的去噪图像
cv2.imshow('边界处理后的去噪图像', result)
cv2.waitKey(0)

# 保存处理后的图像
output_path = 'Files/E/C_scan_processed.jpg'
cv2.imwrite(output_path, result)
print(f"处理后的C扫描图像已保存至 {output_path}")

# 释放资源
cv2.destroyAllWindows()
