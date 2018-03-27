#!/usr/bin/env python3
import sys
import os.path

import cv2
import numpy as np

if __name__ == '__main__':

	argv = sys.argv
	argc = len(argv)
	i = 0

	for arg in argv:
		i = i + 1
		if i == 1:
			continue
		
		name, ext = os.path.splitext(arg)
		if ext != '.jpg':
			continue

		img = cv2.imread(arg)
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

		face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

		face = face_cascade.detectMultiScale(gray, 1.1, 3)

		if len(face) > 0:
			j = 0
			for rect in face:
				x = rect[0]
				y = rect[1]
				width = rect[2]
				height = rect[3]
				dst = img[y:y+height, x:x+width]
				dst = cv2.resize(dst, (100, 100))

				print(arg + ': Face detection success!')
				cv2.imwrite('./output/' + name + '_' + str(j) + ext, dst)
				j = j + 1
