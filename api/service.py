import tensorflow as tf
import numpy as np
import cv2
from PIL import Image
import io
import os
from .dtos import ImageDTO
import json
from sklearn.metrics.pairwise import cosine_similarity

# Lùi 1 cấp từ api/ → biology_recognition/
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# class_dir = os.path.join(BASE_DIR, '..','train')  # Thư mục chứa dữ liệu huấn luyện

# # Lùi thêm 1 cấp để tới thư mục chứa file .keras
# MODEL_PATH = os.path.join(BASE_DIR, '..', 'sgk_classifier_blur_tuned.keras')
# MODEL_PATH = os.path.abspath(MODEL_PATH)  # Chuyển thành đường dẫn tuyệt đối

# # Load mô hình (chỉ load 1 lần)
# model = tf.keras.models.load_model(MODEL_PATH)

# Cấu hình giống lúc train
img_size = (224, 224)

# Tải class names từ file JSON
# json_path = os.path.join(BASE_DIR, '..', 'class_names.json')
# with open(json_path, 'r') as f:
#     class_names = json.load(f)

# biến ảnh thành tensor để dự đoán
def preprocess_image(image_bytes):
    # Đọc ảnh từ bytes (Postman gửi lên)
    image = Image.open(io.BytesIO(image_bytes)).convert('RGB')
    image = image.resize(img_size)
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)  # (1, 224, 224, 3)
    return image


# # Hàm dự đoán lớp của ảnh
# def predict_image_class(image):
#     # image: dạng bytes từ file gửi lên
#     img_tensor = preprocess_image(image)
    
#     preds = model.predict(img_tensor)[0]
#     predicted_index = np.argmax(preds)
#     predicted_class = class_names[predicted_index]
#     confidence = float(preds[predicted_index])

#     return ImageDTO(predicted_class=predicted_class, confidence=confidence)


# === Hàm dùng cosine similarity giữa embedding ảnh test và ảnh huấn luyện ===
# Tải sẵn embeddings & labels
EMBEDDING_PATH = os.path.join(BASE_DIR, '..', 'embeddings', 'embeddings.npy')
LABEL_PATH = os.path.join(BASE_DIR, '..', 'embeddings', 'labels.json')
embeddings = np.load(EMBEDDING_PATH)
with open(LABEL_PATH, 'r') as f:
    embedding_labels = json.load(f)

# Mô hình feature extractor (MobileNetV2)
feature_model = tf.keras.applications.MobileNetV2(
    input_shape=img_size + (3,),
    include_top=False,
    weights='imagenet',
    pooling='avg'
)
feature_model.trainable = False

def predict_image_class_v2(image):
    img_tensor = preprocess_image(image)
    embedding = feature_model.predict(img_tensor)
    sims = cosine_similarity(embedding, embeddings)[0]
    best_idx = int(np.argmax(sims))
    label = embedding_labels[best_idx]
    similarity = float(sims[best_idx])
    return {
        "label": label,
        "similarity": similarity
    }