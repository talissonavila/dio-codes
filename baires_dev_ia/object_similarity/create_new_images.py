import os
import shutil
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
import numpy as np

base_path = 'images_raw/'
output_path = 'dataset/'

classes = ['relógios', 'camisetas']

def create_folders(base_dir, classes):
    for split in ['train', 'val']:
        split_path = os.path.join(base_dir, split)
        os.makedirs(split_path, exist_ok=True)
        for class_name in classes:
            class_path = os.path.join(split_path, class_name)
            os.makedirs(class_path, exist_ok=True)

def organize_dataset(base_path, output_path, classes, test_size=0.2):
    create_folders(output_path, classes)
    for class_name in classes:
        class_path = os.path.join(base_path, class_name)
        images = [os.path.join(class_path, img) for img in os.listdir(class_path)]
        
        train_images, val_images = train_test_split(images, test_size=test_size, random_state=42)
        
        for img_path in train_images:
            shutil.copy(img_path, os.path.join(output_path, 'train', class_name))
        for img_path in val_images:
            shutil.copy(img_path, os.path.join(output_path, 'val', class_name))

def augment_images(base_path, classes, rotations=10):
    datagen = ImageDataGenerator(rotation_range=30, fill_mode='nearest')
    
    for class_name in classes:
        class_path = os.path.join(base_path, 'train', class_name)
        images = os.listdir(class_path)
        
        for img_name in images:
            img_path = os.path.join(class_path, img_name)
            img = load_img(img_path, target_size=(224, 224))
            x = img_to_array(img)
            x = np.expand_dims(x, axis=0)
            
            i = 0
            for batch in datagen.flow(x, batch_size=1, save_to_dir=class_path, save_prefix='aug', save_format='jpg'):
                i += 1
                if i >= rotations:
                    break


if __name__ == '__main__':
    organize_dataset(base_path, output_path, classes)
    print("Dataset organizado com sucesso!")

    augment_images(output_path, classes)
    print("Data augmentation concluído com sucesso!")
