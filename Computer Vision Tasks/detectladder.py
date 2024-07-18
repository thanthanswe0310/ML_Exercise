import numpy as np
import cv2
from collections import namedtuple
from decimal import Decimal, ROUND_DOWN


def overlap(rec1, rec2):
    if (rec2.x2 > rec1.x1 and rec2.x2 < rec1.x2) or (rec2.x1 > rec1.x1 and rec2.x1 < rec1.x2):
        x_match = True
    else:
        x_match = False
    if (rec2.y2 > rec1.y1 and rec2.y2 < rec1.y2) or (rec2.y1 > rec1.y1 and rec2.y1 < rec1.y2):
        y_match = True
    else:
        y_match = False
    if x_match and y_match:
        return True
    else:
        return False

def detectLadder(image, model):
    # Inference
    results = model(image)

    # ladder params
    Ladder_height_feet = 5.5
    Ladder_height_pixels = 100
    topx1 = 0
    topy1 = 0
    topx2 = 0
    topy2 = 0
    bottomx2 = 0
    bottomy2 = 0
    bottomx1 = 0
    bottomy1 = 0
    # Farhan Comment end
    text = ""
    centerpersony = 0
    centerladdery = 0

# ['ladder_with_outriggers', 'ladder_without_outriggers', 'worker_with_helmet', 'worker_without_helmet'] 

    # Results
    # print(results.pandas().xyxy[0])
    if np.shape(results.xyxy[0].cpu().numpy())[0] > 0:
        for (x0, y0, x1, y1, confi, clas) in results.xyxy[0].cpu().numpy():
            if confi > 0:
                print(x0, y0, x1, y1, confi, clas)
                box = [int(x0), int(y0), int(x1 - x0), int(y1 - y0)]
                if int(clas) == 0:
                    converted_label = "Ladder_with_Outriggers" 
                    cv2.rectangle(image, box, (0, 0, 255), 2)
                    cv2.putText(image, converted_label, (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                (0, 0, 255), 2)
                elif int(clas) == 1:
                    converted_label = "Ladder_without_Outriggers"
                    cv2.rectangle(image, box, (0, 255, 0), 2)
                    cv2.putText(image, converted_label, (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                (0, 255, 0), 2)
                elif int(clas) == 2:
                    converted_label = "Worker_with_helmet"
                    cv2.rectangle(image, box, (255, 0, 0), 2)
                    cv2.putText(image, converted_label, (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                (255, 0, 0), 2)
               
                elif int(clas) == 3:
                    converted_label = "Worker_without_helmet"
                    cv2.rectangle(image, box, (255, 255, 0), 2)
                    cv2.putText(image, converted_label, (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                (255, 255, 0), 2)

                left_bottom_Y1 = 0
                left_bottom_Y2 = 0
                bboxworkerheight = 0
                Ladder_height_feet = 5.5
                Ladder_height_pixels = 100

                '''#c1, c2 = (int(x0), int(y0)), (int(x1), int(y1)) #farhan Comment start
                topx1 = 0
                topy1 = 0
                topx2 = 0
                topy2 = 0
                bottomx2 = 0
                bottomy2 = 0
                bottomx1 = 0
                bottomy1 = 0
                # Farhan Comment end
                text = ""
                centerpersony = 0
                centerladdery = 0'''

                letfbottomx = topx1
                leftbottomy = bottomy2

                if int(clas) == 1 or int(clas) == 0:
                    c1, c2 = (int(x0), int(y0)), (int(x1), int(y1)) # Farhan Add start
                    topx1 = c1[0]
                    topy1 = c1[1]
                    bottomx1 = c2[0]
                    bottomy1 = c2[1]

                    left_bottom_Y1 = int(y1)
                    top_height_ladder = left_bottom_Y1 - topy1
                    centerladderx = int((topx1 + bottomx2) / 2)  # ladder center x
                    centerladdery = int((topy1 + bottomy2) / 2)  # ladder center y
                    #cv2.circle(image, (centerladderx, centerladdery), radius=2, color=(255, 0, 255),
                                     #thickness=20)  # to check the ladder centroid

                    print("this", top_height_ladder)
                else:
                    c1, c2 = (int(x0), int(y0)), (int(x1), int(y1))  # Add farhan
                    topx2 = c1[0]
                    topy2 = c1[1]
                    bottomx2 = c2[0]
                    bottomy2 = c2[1]    # end Farhan

                    left_bottom_Y2 = int(y1)
                    bboxworkerheight = left_bottom_Y2 - topy1

                    centerpersonx = int((topx1 + bottomx2) / 2)  # ladder center x
                    centerpersony = int((topy1 + bottomy2) / 2)  # ladder center y
                    #cv2.circle(image, (centerpersonx, centerpersony), radius=2, color=(255, 0, 255),
                             #thickness=20)  # to check the person centroid

                    print("sdss", bboxworkerheight)

                RECT_NAMEDTUPLE = namedtuple('RECT_NAMEDTUPLE', 'x1 y1 x2 y2')

                Rect1 = RECT_NAMEDTUPLE(topx1, topy1, bottomx1, bottomy1)
                # print('Rect1',Rect1)
                Rect2 = RECT_NAMEDTUPLE(topx2, topy2, bottomx2, bottomy2)
                # print('Rect2', Rect2)
                overlap_result = overlap(Rect1, Rect2)
                print(overlap_result)

                '''if centerpersony < centerladdery:
                    if converted_label == "Worker_with_helmet" or converted_label == "Ladder_with_Outriggers":
                        text = "Safe"
                    else:
                        text = "Unsafe"
                        '''
                if overlap_result:
                    if centerpersony < centerladdery:
                        if int(clas) != 0:
                            text = "Un-Safe Behaviour"
                        else:
                            if int(clas) == 2:
                                text = "Safe Behaviour"
                            else:
                                text = "Un-Safe Behaviour"

                    ''''  
                    if converted_label == "Worker_with_helmet" and converted_label == "Ladder_without_Outriggers":
                        text = "Un-Safe Behaviour"
                    if converted_label == "Worker_without_helmet" and converted_label == "Ladder_with_Outriggers":
                        text = "Un-Safe Behaviour"
                    if converted_label == "Worker_without_helmet" and converted_label == "Ladder_without_Outriggers":
                        text = "Un-Safe Behaviour"                    '''

                    cv2.putText(image, str(text), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 0, 0), 1)

                #cv2.putText(image, str(text), (25, 25), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)

    return image
