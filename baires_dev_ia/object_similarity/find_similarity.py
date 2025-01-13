import numpy as np
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input
from sklearn.metrics.pairwise import cosine_similarity
import os

model = ResNet50(weights='imagenet', include_top=False, pooling='avg')

def extract_features(img_path, model):
    img = image.load_img(img_path, target_size=(224, 224))
    img_data = image.img_to_array(img)
    img_data = np.expand_dims(img_data, axis=0)
    img_data = preprocess_input(img_data)
    features = model.predict(img_data)
    return features.flatten()

image_dir = 'caminho/para/diretorio/de/imagens'

feature_list = []
image_list = []
for img_name in os.listdir(image_dir):
    img_path = os.path.join(image_dir, img_name)
    features = extract_features(img_path, model)
    feature_list.append(features)
    image_list.append(img_name)

feature_array = np.array(feature_list)

def find_similar_images(input_img_path, model, feature_array, image_list, top_n=5):
    input_features = extract_features(input_img_path, model)
    similarities = cosine_similarity([input_features], feature_array)
    similar_indices = similarities.argsort()[0][-top_n:][::-1]
    similar_images = [image_list[i] for i in similar_indices]
    return similar_images

input_image = 'caminho/para/imagem/de/entrada.jpg'
similar_images = find_similar_images(input_image, model, feature_array, image_list)
print("Imagens similares:", similar_images)
