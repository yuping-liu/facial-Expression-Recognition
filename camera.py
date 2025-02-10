import cv2

# 打开摄像头
cap = cv2.VideoCapture(0)  # 参数 0 表示使用默认摄像头

if not cap.isOpened():
    print("无法打开摄像头")
    exit()

# 设置摄像头分辨率（可选）
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)  # 设置宽度
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)  # 设置高度

while True:
    # 读取一帧图像
    ret, frame = cap.read()
    if not ret:
        print("无法接收帧（可能摄像头断开连接）")
        break

    # 显示图像
    cv2.imshow('Camera', frame)

    # 按下 'q' 键退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放资源
cap.release()
cv2.destroyAllWindows()
