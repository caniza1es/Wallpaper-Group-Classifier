import cv2
import imagehash
from PIL import Image
import numpy as np

def LoadImage(image_path:str):
    img = cv2.imread(image_path,cv2.IMREAD_COLOR)
    assert img is not None
    return img

def FindContourns(img):
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imgray, 127, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    return contours,hierarchy

def has_nth_order(image, i):
    pil_image = Image.fromarray(image)
    rotated_image = pil_image.rotate(360/i)
    hash_original = imagehash.average_hash(pil_image)
    hash_rotated = imagehash.average_hash(rotated_image)
    similarity = 1 - (hash_original - hash_rotated) / len(hash_original.hash) ** 2
    return similarity > 0.64

def has_axis_reflection(image, n=30):
    sift = cv2.SIFT_create()  # Updated this line
    mimage = np.fliplr(image)
    kp1, des1 = sift.detectAndCompute(image, None)
    kp2, des2 = sift.detectAndCompute(mimage, None)
    
    for p, mp in zip(kp1, kp2):
        p.angle = np.deg2rad(p.angle)
        mp.angle = np.deg2rad(mp.angle)
    
    bf = cv2.BFMatcher()
    matches = bf.knnMatch(des1, des2, k=2)
    
    count = 0
    
    for match, match2 in matches:
        point = kp1[match.queryIdx]
        mirpoint = kp2[match.trainIdx]
        mirpoint2 = kp2[match2.trainIdx]
        mirpoint2.angle = np.pi - mirpoint2.angle
        mirpoint.angle = np.pi - mirpoint.angle
        
        if mirpoint.angle < 0.0:
            mirpoint.angle += 2 * np.pi
        if mirpoint2.angle < 0.0:
            mirpoint2.angle += 2 * np.pi
            
        mirpoint.pt = (mimage.shape[1] - mirpoint.pt[0], mirpoint.pt[1])
        
        if np.sqrt((point.pt[0] - mirpoint.pt[0]) ** 2 + (point.pt[1] - mirpoint.pt[1]) ** 2) < 4.0:
            count += 1

    return count >= n

def has_reflection(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    flipped_image = cv2.flip(gray_image, 1)
    diff = cv2.absdiff(gray_image, flipped_image)
    mean_diff = np.mean(diff)
    threshold = 34  
    return mean_diff < threshold

def has_glidereflection(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    flipped_image = cv2.flip(gray_image, 1)
    M = np.float32([[1, 0, 100], [0, 1, 0]])
    shifted_image = cv2.warpAffine(flipped_image, M, (image.shape[1], image.shape[0]))
    diff = cv2.absdiff(gray_image, shifted_image)
    mean_diff = np.mean(diff)
    threshold = 78
    return mean_diff < threshold

def has_axisglide(image):
    pass
