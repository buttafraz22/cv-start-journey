import cv2 as cv

# img = cv.imread('img/img.jpg')
capture = cv.VideoCapture('img/video.mkv')   # 0 for webcam


def rescale_frame(frame_param, scale=0.50):
    width = int(frame_param.shape[1] * scale)
    height = int(frame_param.shape[0] * scale)

    dimensions = (width, height)
    return cv.resize(frame_param, dimensions, interpolation=cv.INTER_AREA)


def change_res(width, height):
    capture.set(3, width)
    capture.set(4, height)


while True:
    is_true, frame = capture.read()
    change_res(int(frame.shape[1] * 0.20), int(frame.shape[0] * 0.20))
    frame_new = rescale_frame(frame)

    cv.imshow('Video', frame_new)

    if cv.waitKey(20) and 0xFF == ord('q'):
        break


capture.release()
cv.destroyAllWindows()
