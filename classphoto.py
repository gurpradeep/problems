def classPhotos(redShirtHeights, blueShirtHeights):

	if len(redShirtHeights) == 0 or len(blueShirtHeights)==0:
		return False
	
	redShirtHeights.sort(reverse=True)
	blueShirtHeights.sort(reverse=True)
	
	shirtColorInFirstRow='Red' if redShirtHeights[0]<blueShirtHeights[0] else 'Blue'
	
	for idx in range(len(redShirtHeights)):
		redShirtHeight = redShirtHeights[idx]
		blueShirtHeight = blueShirtHeights[idx]
	
		if shirtColorInFirstRow=='Red':
			if redShirtHeight >=blueShirtHeight:
				return False
		else:
			if blueShirtHeight >=redShirtHeight:
				return False
		



redShirtHeights = [5, 8, 1, 3, 4]
blueShirtHeights = [6, 9, 2, 4, 5]
classPhotos(redShirtHeights,blueShirtHeights)    