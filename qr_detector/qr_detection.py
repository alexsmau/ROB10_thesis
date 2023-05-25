import cv2
import numpy as np
from pyzbar.pyzbar import decode
# import webbrowser

# initialize the cv2 QRCode detector
detector = cv2.QRCodeDetector()
# qr_code = cv2.imread("Google.png")
detected = False
# cv2.imshow("qr", qr_code)


# Detect and decode the QR code

cap = cv2.VideoCapture(0)
i = 0
while True:
    ret, frame = cap.read()

    # print(decode(frame))

    # Try to open the QR message
    # Can detect multiple QR-codes, a way to solve labeling/classification
    # can be done by providing different messaages and if statements
    if detected == False:

        for code in decode(frame):
            qr_link = code.data.decode("utf-8")
            print(code.data)
            print()

            # b = webbrowser.open(qr_link)


            # Draw BBOX
            bbox_points = code.polygon
            # print(bbox_points)

            # See the how are the points and where they belong to
            points = np.array([code.polygon], np.int32)
            # print("points", points)
            # print("POINTS 0.0 ", points[0][0][0])
            # print("POINTS 0.1 ", points[0][0][1])
            # print("POINTS 1.0 ", points[0][1][0])
            # print("POINTS 1.1 ", points[0][1][1])
            # print("POINTS 2.0 ", points[0][2][0])
            # print("POINTS 2.1 ", points[0][2][1])
            # print("POINTS 3.0 ", points[0][3][0])
            # print("POINTS 3.1 ", points[0][3][1])
            # print(' ')
            # print(print("POINTS 1", points[1]))

            # Drawing the boundy box  the center of it and the position of each point
            cv2.polylines(frame, [points], True, (255, 0, 0), 3)
            cv2.putText(frame, "0", (points[0][0][0], points[0][0][1]), cv2.FONT_HERSHEY_SIMPLEX, .5, (0,255,0), 2)
            cv2.putText(frame, "1", (points[0][1][0], points[0][1][1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
            cv2.putText(frame, "2", (points[0][2][0], points[0][2][1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
            cv2.putText(frame, "3", (points[0][3][0], points[0][3][1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

            #Getting the center of the bbx

            center_bbx = [abs((points[0][1][0] + points[0][0][0])/2), abs((points[0][2][1] + points[0][1][1])/2)]
            # print(center_bbx)
            cv2.circle(frame, (int(center_bbx[0]), int(center_bbx[1])), 2, (255, 0, 0), 2)

            # Stop detection
            # detected = True

    # else:
    #     break

    # Save img
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite(f"ss{i}.jpg", frame)
        i+=1


    # Show the image
    cv2.imshow("qr", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # See what the detector provides
    # print('data', data)
    # print()
    # print('bbox', bbox)
    # print()
    # print("_", _)

# cv2.waitKey(0)
cv2.destroyAllWindows()

