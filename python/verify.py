##-----------------------------------------------------------------------------
##  Import
##-----------------------------------------------------------------------------
import argparse
from time import time

from fnc.extractFeature import extractFeature
from fnc.matching import matching
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
#Addition
from fnc.plotgrid import gallery
#from fnc.extractFeature import get_descriptors
#from fnc.extractFeature import removedot


#------------------------------------------------------------------------------
#	Argument parsing
#------------------------------------------------------------------------------
parser = argparse.ArgumentParser()

parser.add_argument("--file", type=str,
                    help="Path to the file that you want to verify.")

parser.add_argument("--temp_dir", type=str, default="./templates/CASIA1/",
					help="Path to the directory containing templates.")

parser.add_argument("--thres", type=float, default=0.38,
					help="Threshold for matching.")

args = parser.parse_args()


##-----------------------------------------------------------------------------
##  Execution
##-----------------------------------------------------------------------------
# Extract feature
start = time()
print('>>> Start verifying {}\n'.format(args.file))
template, mask, file = extractFeature(args.file)

#Addition
img=mpimg.imread(args.file)
#imgplot = plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
#plt.show()

cv2.imshow('Image to be Matched',img)
cv2.waitKey(1000)
#cv2.destroyAllWindows()
#Addition above


# Matching
result = matching(template, mask, args.temp_dir, args.thres)


if result == -1:
	print('>>> No registered sample.')

elif result == 0:
	print('>>> No sample matched.')

else:
	print('>>> {} samples matched (descending reliability):'.format(len(result)))
	a= 750
	b= 20
	for res in result:
		print("\t", res, "\t User ", res[1:3])
	#Addition
		if res[1] != '0':
			img=mpimg.imread('../CASIA1/' +res[1:3]+'/' + res[:-4])
		else:
			img=mpimg.imread('../CASIA1/' +res[2]+'/' + res[:-4])
		winname = 'Image ' + res[:-4] + ': User' + res[1:3]
		cv2.namedWindow(winname)
		cv2.moveWindow(winname,a,b)
		b += 150
		cv2.imshow(winname,img)
		cv2.waitKey(1000)
	cv2.destroyAllWindows()
	#addition above
	


# Time measure
end = time()
print('\n>>> Verification time: {} [s]\n'.format(end - start))
