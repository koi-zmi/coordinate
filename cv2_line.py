# coding:utf-8
#上記の文がコメントを打つ場合には必要・・・らしい。

import cv2
import numpy as np
import argparse

print("-------8----------------")
parser=argparse.ArgumentParser()
parser.add_argument("-n","--numeric_n1")
args = parser.parse_args()

print("-------12----------------")
print(args.numeric_1)

numeric=args.numeric_1
if numeric!=0:
    top_left_x=455
    top_left_y=455
    line_horizon=100
    line_vert=200
    
    '''
    top_left_x=int(input('長方形の左上のx座標:'))
    top_left_y=int(input('長方形の左上のy座標:'))
    line_horizon=int(input('並行線分の大きさ:'))
    line_vert=int(input('垂直線分の大きさ:'))
    '''

#下記の文章は画角の大きさ
img = np.zeros((1000,1000,3),dtype=np.uint8)

#図形は重ねることが出来る
img=cv2.circle(img,(800,800),100,color=(255,200,100),thickness=2)
img=cv2.circle(img,(850,750),100,color=(255,200,100),thickness=-1)

# 線を引く（線を引く画像、座標、線の色、線の太さをパラメータに指定）

#座標の形成
font=cv2.FONT_HERSHEY_SIMPLEX
for i in range(1,20):
    img=cv2.line(img,(i*50,0),(i*50,1000),(255,255,255),1)
    img=cv2.line(img,(0,i*50),(1000,i*50),(255,255,255),1)
    
    '''
    画像への文字入力　[画像，テキスト，位置（左下），フォント，スケール，色，線太さ，種類]
    img = cv2.putText( img, text, org, fontFace, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]] )
    '''
    
    img=cv2.putText(img, str(i*50), (10,i*50+15), font, 0.4, (255,200,100), 1, cv2.LINE_AA)
    img=cv2.putText(img, str(i*50), (i*50+15,40), font, 0.4, (255,200,100), 1, cv2.LINE_AA)
#長方形の左上の座標(top_left_x,top_left_y)と縦横の線分(line_horizen,line_vert)の大きさの指定

img=cv2.circle(img,(top_left_x,top_left_y),5,color=(255,200,100),thickness=-1)#左上
img=cv2.circle(img,(top_left_x+line_horizon,top_left_y),5,color=(255,200,100),thickness=-1)#右上
img=cv2.circle(img,(top_left_x+line_horizon,top_left_y+line_vert),5,color=(255,200,100),thickness=-1)#右下
img=cv2.circle(img,(top_left_x,top_left_y+line_vert),5,color=(255,200,100),thickness=-1)#左下

img=cv2.line(img,(top_left_x,top_left_y),(top_left_x+line_horizon,top_left_y),(255,255,255),1)
img=cv2.line(img,(top_left_x+line_horizon,top_left_y),(top_left_x+line_horizon,top_left_y+line_vert),(255,255,255),1)
img=cv2.line(img,(top_left_x+line_horizon,top_left_y+line_vert),(top_left_x,top_left_y+line_vert),(255,255,255),1)
img=cv2.line(img,(top_left_x,top_left_y+line_vert),(top_left_x,top_left_y),(255,255,255),1)

#status [文字列、品詞、座標[左上],[右上],[右下],[左下],{id}]

cv2.imshow("image",img)
cv2.waitKey()