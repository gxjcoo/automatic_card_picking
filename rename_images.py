import os
import easyocr
from PIL import Image
import tkinter as tk
from tkinter import filedialog, messagebox
import numpy as np
import cv2

def select_directory():
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口
    folder_path = filedialog.askdirectory(title="选择包含图片的文件夹")
    return folder_path if folder_path else None

def extract_text_from_image(image_path):
    # 初始化 EasyOCR
    reader = easyocr.Reader(['ch_sim', 'en'])
    
    # 读取图片
    img = cv2.imread(image_path)
    if img is None:
        raise Exception("无法读取图片")
    
    # 转换为RGB
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # 获取图片尺寸
    height, width = img.shape[:2]
    
    # 定义感兴趣区域
    cost_roi = img_rgb[height//2:, :width//4]  # 下半部分左侧区域用于检测金额
    name_roi = img_rgb[height//2:, width//4:width//2]  # 下半部分中间区域用于检测名称
    
    # 使用OCR识别文本
    cost_result = reader.readtext(cost_roi)
    name_result = reader.readtext(name_roi)
    
    # 提取成本和名称
    cost = None
    name = None
    
    # 从成本区域提取数字
    for detection in cost_result:
        text = detection[1]
        if text.isdigit() and 1 <= int(text) <= 5:
            cost = text
            break
    
    # 从名称区域提取文本
    if name_result:
        name = name_result[0][1]  # 取第一个检测到的文本作为名称
    
    return cost, name

def rename_images(directory):
    # 确保目录存在
    if not os.path.exists(directory):
        print(f"目录不存在: {directory}")
        return
    
    # 获取所有图片文件
    image_files = [f for f in os.listdir(directory) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    
    for image_file in image_files:
        try:
            # 获取完整的图片路径
            image_path = os.path.join(directory, image_file)
            
            # 从图片中提取文本
            cost, name = extract_text_from_image(image_path)
            
            if not cost or not name:
                print(f"无法从图片中提取信息: {image_file}")
                continue
            
            # 构建新文件名
            new_filename = f"{cost}{name}.png"
            new_path = os.path.join(directory, new_filename)
            
            # 如果新文件名已存在，添加数字后缀
            counter = 1
            while os.path.exists(new_path):
                base, ext = os.path.splitext(new_filename)
                new_filename = f"{base}_{counter}{ext}"
                new_path = os.path.join(directory, new_filename)
                counter += 1
            
            # 重命名文件
            os.rename(image_path, new_path)
            print(f"已重命名: {image_file} -> {new_filename}")
        
        except Exception as e:
            print(f"处理文件 {image_file} 时出错: {str(e)}")
            continue

def main():
    print("正在初始化OCR系统...")
    
    # 选择目录
    directory = select_directory()
    if not directory:
        print("未选择目录，程序退出")
        return
    
    print("开始处理图片...")
    # 重命名图片
    rename_images(directory)
    print("处理完成！")

if __name__ == "__main__":
    main()
