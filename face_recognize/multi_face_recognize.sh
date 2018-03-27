#/usr/bin/bash

for a in *; do
	python face_recognize.py $a
done
