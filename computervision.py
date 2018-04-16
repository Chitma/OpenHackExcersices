from azure.cognitiveservices.vision.customvision.prediction import prediction_endpoint
from azure.cognitiveservices.vision.customvision.prediction.prediction_endpoint import models

# Now there is a trained endpoint that can be used to make a prediction
prediction_key = "7faf6f48fb2348e39ead68418edcd511";
project_id = "fb602e52-d90b-4c40-984c-577cba439ad1";
iteration_id = "94d5fc8a-7964-4f47-84ec-b7357728b937";

predictor = prediction_endpoint.PredictionEndpoint(prediction_key)


#test_img_url = base_image_url + "Images/Test/test_image.jpg"
#results = predictor.predict_image_url(project.id, iteration.id, url=test_img_url)

# Alternatively, if the images were on disk in a folder called Images alongside the sample.py, then
# they can be added by using the following.
#
# Open the sample image and get back the prediction results.
with open("C:\\Users\\Manish\\Desktop\\gear_images\\insulated_jackets\\10167913x1063714_zm.jpeg", mode="rb") as test_data:
    results = predictor.predict_image(project_id, test_data.read(), iteration_id)

# Display the results.
for prediction in results.predictions:
    print ("\t" + prediction.tag + ": {0:.2f}%".format(prediction.probability * 100))