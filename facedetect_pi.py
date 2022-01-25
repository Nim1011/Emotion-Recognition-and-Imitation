import requests

import facedetect_led

def emodet():
	print("emodet")
	subscription_key = "038cdedae124464087a70ac33d93796a"

	assert subscription_key

	emotion_recognition_url = "https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect?returnfaceAttributes=emotion"

	header = {'Ocp-Apim-Subscription-Key': subscription_key }

	image_url = "https://aka.ms/csnb-emotion-1"

	body = {'url': image_url}

	image_path = "capture.jpg"

	image_data = open(image_path, "rb").read()



	headers  = {'Ocp-Apim-Subscription-Key': subscription_key, "Content-Type": "application/octet-stream" }

	response = requests.post(emotion_recognition_url, headers=headers, data=image_data)

	response.raise_for_status()

	analysis = response.json()

	for face in analysis:

    		temp = (face["faceAttributes"]['emotion'])

    		greatest = 0;

    		for i in temp:

        		if (temp[i]>0) and (temp[i]<=1):

            			items = [(v, k) for k, v in temp.items()]

            			items.sort()

            			items.reverse()

    		print(items[0][1])
    		facedetect_led.serialcom(items[0][1])


