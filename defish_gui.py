import cv2
import numpy as np

def nothing(x):
    pass




src1 = cv2.imread("/home/kaczor/fish_eye/wm/wm/1.jpg")
src1 = cv2.resize(src1,None,fx=0.5,fy=0.5)
DIM=(src1.shape[1],src1.shape[0])
print(src1.shape)
cv2.namedWindow("frame")
cv2.createTrackbar("K1", "frame" , 10000, 20000, nothing)
cv2.createTrackbar("K2", "frame" , 10000, 20000, nothing)
cv2.createTrackbar("K3", "frame" , 10000, 20000, nothing)
cv2.createTrackbar("K4", "frame" , 10000, 20000, nothing)
cv2.createTrackbar("fx", "frame" , 1000, 5000, nothing)
cv2.createTrackbar("fy", "frame" , 1000, 5000, nothing)
cv2.createTrackbar("x_0", "frame" , 1000, 5000, nothing)
cv2.createTrackbar("y_0", "frame" , 1000, 5000, nothing)

# Show some stuff
# Wait until user press some key
#cv2.ihow("frame",src1)

#K=np.array([[1791.682925622999, 0.0, 2297.5185706646316], [0.0, 1784.9089352893657, 1722.882566975389], [0.0, 0.0, 1.0]])
#D=np.array([[0.2963401210229542], [0.2581938559803338], [-0.13324780972622483], [0.010901962925226178]])

K=np.array([[1.0, 0.0, 1.0], 
[0.0, 1.0, 1.0], 
[0.0, 0.0, 1.0]])

D=np.array([[0.0], [0.0], [0.0], [0.0]])

#src1 = cv2.fisheye.undistortImage(src1,K,D)

while True:
    key = cv2.waitKey(27)
    print(D)
    D[0] = [(cv2.getTrackbarPos("K1","frame")-10000) / 10000]
    D[1] = [(cv2.getTrackbarPos("K2","frame")-10000) / 10000]
    D[2] = [(cv2.getTrackbarPos("K3","frame")-10000) / 10000]
    D[3] = [(cv2.getTrackbarPos("K4","frame")-10000) / 10000]

    K[0][0] = (cv2.getTrackbarPos("fx","frame")) 
    K[1][1] = (cv2.getTrackbarPos("fy","frame")) 
    K[0][2] = (cv2.getTrackbarPos("x_0","frame")) 
    K[1][1] = (cv2.getTrackbarPos("y_0","frame")) 

    #print(k1)

    map1, map2 = cv2.fisheye.initUndistortRectifyMap(K, D, np.eye(3), K, DIM, cv2.CV_16SC2)
    undist = cv2.remap(src1, map1, map2, interpolation=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT)
    
    #undist = cv2.fisheye.undistortImage(src1,K,D)

    #undist=src1
    #print(int(undist.shape[0]/8),int(undist.shape[1]/8))
    #undist = cv2.resize(undist,(int(undist.shape[1]/8),int(src1.shape[0]/8)),interpolation = cv2.INTER_AREA)
    undist = cv2.resize(undist,(int(undist.shape[1]/4),int(src1.shape[0]/4)),interpolation = cv2.INTER_AREA)

    cv2.imshow("frame",undist)

    if key == 27:
        break


cv2.destroyAllWindows()