import cv2
import mediapipe as mp
import math
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)
x=(1,2)
thumb_tip = 4

def hand_pos(right_lm_list,left_lm_list):
    pos=[]
    try:
         if (max(abs(right_lm_list[0].x -right_lm_list[9].x),abs(right_lm_list[0].x -right_lm_list[12].x))>=.13):
            pos.append("RSIDE")
         else:
            pos.append("RUP")
         try:
            if (max(abs(left_lm_list[0].x -left_lm_list[9].x),abs(left_lm_list[0].x -left_lm_list[12].x))>=.13):
                pos.append("LSIDE")
            else:
                pos.append("LUP")
         except: pass
    except:
            if (max(abs(left_lm_list[0].x -left_lm_list[9].x),abs(left_lm_list[0].x -left_lm_list[12].x))>=.13):
                pos.append("LSIDE")
            else:
                pos.append("LUP")
            try:
                if (max(abs(right_lm_list[0].x -right_lm_list[9].x),abs(right_lm_list[0].x -right_lm_list[12].x))>=.13):
                   pos.append("RSIDE")
                else:
                    pos.append("RUP")
            except: pass
    return pos
                    ###########################################################################
                    ###########################################################################
                    ###########################################################################

def fingers(right_lm_list, left_lm_list):
    fingers_top_R = []
    fingers_top_L = []
    fingers_middle_R = []
    fingers_middle_L = []
    fingers_end_R = []
    fingers_end_L = []

    try:
        fingers_top_R.extend([
            (right_lm_list[4].x, right_lm_list[4].y),
            (right_lm_list[8].x, right_lm_list[8].y),
            (right_lm_list[12].x, right_lm_list[12].y),
            (right_lm_list[16].x, right_lm_list[16].y),
            (right_lm_list[20].x, right_lm_list[20].y)
        ])
    except IndexError:
        pass

    try:
        fingers_top_L.extend([
            (left_lm_list[4].x, left_lm_list[4].y),
            (left_lm_list[8].x, left_lm_list[8].y),
            (left_lm_list[12].x, left_lm_list[12].y),
            (left_lm_list[16].x, left_lm_list[16].y),
            (left_lm_list[20].x, left_lm_list[20].y)
        ])
    except IndexError:
        pass

    try:
        fingers_middle_R.extend([
            (right_lm_list[3].x, right_lm_list[3].y),
            (right_lm_list[7].x, right_lm_list[7].y),
            (right_lm_list[11].x, right_lm_list[11].y),
            (right_lm_list[15].x, right_lm_list[15].y),
            (right_lm_list[19].x, right_lm_list[19].y)
        ])
    except IndexError:
        pass

    try:
        fingers_middle_L.extend([
            (left_lm_list[3].x, left_lm_list[3].y),
            (left_lm_list[7].x, left_lm_list[7].y),
            (left_lm_list[11].x, left_lm_list[11].y),
            (left_lm_list[15].x, left_lm_list[15].y),
            (left_lm_list[19].x, left_lm_list[19].y)
        ])
    except IndexError:
        pass

    try:
        fingers_end_R.extend([
            (right_lm_list[2].x, right_lm_list[2].y),
            (right_lm_list[6].x, right_lm_list[6].y),
            (right_lm_list[10].x, right_lm_list[10].y),
            (right_lm_list[14].x, right_lm_list[14].y),
            (right_lm_list[18].x, right_lm_list[18].y)
        ])
    except IndexError:
        pass

    try:
        fingers_end_L.extend([
            (left_lm_list[2].x, left_lm_list[2].y),
            (left_lm_list[6].x, left_lm_list[6].y),
            (left_lm_list[10].x, left_lm_list[10].y),
            (left_lm_list[14].x, left_lm_list[14].y),
            (left_lm_list[18].x, left_lm_list[18].y)
        ])
    except IndexError:
        pass

    return fingers_top_R, fingers_top_L, fingers_middle_R, fingers_middle_L, fingers_end_R, fingers_end_L
                    ###########################################################################
                    ###########################################################################
                    ###########################################################################

def fingers_crossed_R(fingers,fingers_top_R,fingers_end_R,right_lm_list,left_lm_list):
    if (len(fingers_top_R)!=0):
        for i in fingers:
            if (math.sqrt(pow(right_lm_list[0].x-fingers_top_R[i][0],2)+pow(right_lm_list[0].y-fingers_top_R[i][1],2))
                >math.sqrt(pow(right_lm_list[0].x-fingers_end_R[i][0],2)+pow(right_lm_list[0].y-fingers_end_R[i][1],2))):
                return False
    return True and (len(fingers_top_R)!=0)

def fingers_crossed_L(fingers,fingers_top_L,fingers_end_L,right_lm_list,left_lm_list):
    if (len(fingers_top_L)!=0):
        for i in fingers:
              if (math.sqrt(pow(left_lm_list[0].x-fingers_top_L[i][0],2)+pow(left_lm_list[0].y-fingers_top_L[i][1],2))
                >math.sqrt(pow(left_lm_list[0].x-fingers_end_L[i][0],2)+pow(left_lm_list[0].y-fingers_end_L[i][1],2))):
                return False
     
    return True and (len(fingers_top_L)!=0)
                    ###########################################################################
                    ###########################################################################
                    ###########################################################################
def Fingers_straight_R(fingers,fingers_top_R,fingers_end_R,right_lm_list,left_lm_list):
    if (len(fingers_top_R)!=0):
        for i in fingers:
               if (math.sqrt(pow(right_lm_list[0].x-fingers_top_R[i][0],2)+pow(right_lm_list[0].y-fingers_top_R[i][1],2))
                <math.sqrt(pow(right_lm_list[0].x-fingers_end_R[i][0],2)+pow(right_lm_list[0].y-fingers_end_R[i][1],2))):
                return False
    return True and (len(fingers_top_R)!=0)

def Fingers_straight_L(fingers,fingers_top_L,fingers_end_L,right_lm_list,left_lm_list):
    if (len(fingers_top_L)!=0):
        for i in fingers:
              if (math.sqrt(pow(left_lm_list[0].x-fingers_top_L[i][0],2)+pow(left_lm_list[0].y-fingers_top_L[i][1],2))
                <math.sqrt(pow(left_lm_list[0].x-fingers_end_L[i][0],2)+pow(left_lm_list[0].y-fingers_end_L[i][1],2))):
                return False
     
    return True and (len(fingers_top_L)!=0)
                    ###########################################################################
                    ###########################################################################
                    ###########################################################################
def Like_Sign(fingers_top_R,fingers_top_L,fingers_middle_R,fingers_middle_L,fingers_end_R,fingers_end_L,pos,right_lm_list,left_lm_list):
            
            if (fingers_crossed_R([1,2,3,4],fingers_top_R,fingers_end_R,right_lm_list,left_lm_list) and
                 pos[0]=="RSIDE" and 
                 fingers_top_R[0][1]<fingers_middle_R[0][1] and 
                 fingers_end_R[0][1]>fingers_middle_R[0][1] and 
                 abs(fingers_end_R[0][1]-fingers_top_R[0][1])>.09):
                return True

            if (fingers_crossed_L([1,2,3,4],fingers_top_L,fingers_end_L,right_lm_list,left_lm_list) and
                 (pos[0]=="LSIDE" or (len(pos)>1 and pos[1]=="LSIDE" )) and 
                 fingers_top_L[0][1]<fingers_middle_L[0][1] and 
                 fingers_end_L[0][1]>fingers_middle_L[0][1] and
                 abs(fingers_end_L[0][1]-fingers_top_L[0][1])>.09):
                return True
            return False
                    ###########################################################################
                    ###########################################################################
                    ###########################################################################
def DisLike_Sign(fingers_top_R,fingers_top_L,fingers_middle_R,fingers_middle_L,fingers_end_R,fingers_end_L,pos,right_lm_list,left_lm_list):
            if (fingers_crossed_R([1,2,3,4],fingers_top_R,fingers_end_R,right_lm_list,left_lm_list) and
                 pos[0]=="RSIDE" and 
                 fingers_top_R[0][1]>fingers_middle_R[0][1] and 
                 fingers_end_R[0][1]<fingers_middle_R[0][1] and 
                 abs(fingers_end_R[0][1]-fingers_top_R[0][1])>.09):
                return True
            if (fingers_crossed_L([1,2,3,4],fingers_top_L,fingers_end_L,right_lm_list,left_lm_list) and
                 (pos[0]=="LSIDE" or len(pos)>1) and 
                 fingers_top_L[0][1]>fingers_middle_L[0][1] and 
                 fingers_end_L[0][1]<fingers_middle_L[0][1] and
                 abs(fingers_end_L[0][1]-fingers_top_L[0][1])>.09):
                 return True
            return False
                    ###########################################################################
                    ###########################################################################
                    ###########################################################################
def Bird_Sign(fingers_top_R,fingers_top_L,fingers_middle_R,fingers_middle_L,fingers_end_R,fingers_end_L,pos,right_lm_list,left_lm_list):
    try:
        if (Fingers_straight_L([1,2,3,4],fingers_top_L,fingers_end_L,right_lm_list,left_lm_list) and
            Fingers_straight_R([1,2,3,4],fingers_top_R,fingers_end_R,right_lm_list,left_lm_list) and 
                 pos[0]=="RSIDE" and 
                 fingers_top_R[0][1]<fingers_middle_R[0][1] and 
                 fingers_end_R[0][1]>fingers_middle_R[0][1] and
                 pos[1]=="LSIDE" and 
                 fingers_top_L[0][1]<fingers_middle_L[0][1] and 
                 fingers_end_L[0][1]>fingers_middle_L[0][1] and
                 abs(fingers_end_L[0][0]-fingers_end_R[0][0])<.109 and
                 abs(fingers_end_L[0][1]-fingers_end_R[0][1])<.109):
                return True
    except:
        return False
    return False
                    ###########################################################################
                    ###########################################################################
                    ###########################################################################

while cap.isOpened:
    ret, img = cap.read()
    img = cv2.resize(img, (1024, 768))
    img = cv2.flip(img, 1)
    results = hands.process(img)
    if results.multi_hand_landmarks:
        right_lm_list = []
        left_lm_list = []
        for hand_landmark, hand in zip(results.multi_hand_landmarks, results.multi_handedness):
            if hand.classification[0].label == "Right":
                for id, lm in enumerate(hand_landmark.landmark):
                    right_lm_list.append(lm)
            elif hand.classification[0].label == "Left":
                for id, lm in enumerate(hand_landmark.landmark):
                    left_lm_list.append(lm)
            pos=hand_pos(right_lm_list,left_lm_list)

            (fingers_top_R,fingers_top_L,fingers_middle_R,fingers_middle_L,fingers_end_R,fingers_end_L)=fingers(right_lm_list,left_lm_list)
                    ###########################################################################
            if (len(left_lm_list)!=0):
                cv2.putText(img, "L", (20, 760), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
                      ###########################################################################
            if (len(right_lm_list)!=0):
                cv2.putText(img, "R", (1000, 760), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
                    ###########################################################################
            if (Like_Sign(fingers_top_R,fingers_top_L,fingers_middle_R,fingers_middle_L,fingers_end_R,fingers_end_L,pos,right_lm_list,left_lm_list)):
                cv2.putText(img, "Like", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
                    ###########################################################################
            if (DisLike_Sign(fingers_top_R,fingers_top_L,fingers_middle_R,fingers_middle_L,fingers_end_R,fingers_end_L,pos,right_lm_list,left_lm_list)):
                cv2.putText(img, "DisLike", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
                    ###########################################################################
            if (Bird_Sign(fingers_top_R,fingers_top_L,fingers_middle_R,fingers_middle_L,fingers_end_R,fingers_end_L,pos,right_lm_list,left_lm_list)):
                cv2.putText(img, "Bird", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
                    ###########################################################################
            mp_draw.draw_landmarks(img, hand_landmark,
                                mp_hands.HAND_CONNECTIONS,
                                mp_draw.DrawingSpec((0, 0, 255), 6, 3),
                                mp_draw.DrawingSpec((0, 255, 0), 4, 2)
                                )
    cv2.imshow("Hand Sign Detection", img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()