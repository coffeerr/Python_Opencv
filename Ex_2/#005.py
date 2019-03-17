#005  读取摄像头画面，并保存一帧画面到本地
import cv2

if __name__ =='__main__':
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cv2.imshow("capture", frame)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        cv2.imwrite("./video.jpg", frame)
    cv2.destroyAllWindows()