# 🧬 Biological Image Recognition (Django + MobileNetV2)

This project uses MobileNetV2 for biological image recognition. The system is built with Django and provides an API to classify biological images by comparing them to pre-computed embeddings.

## 🔧 Technologies

- Python 3.x  
- Django – Web framework  
- TensorFlow / Keras – Deep learning support  
- MobileNetV2 – Lightweight pre-trained image recognition model

## 🚀 Installation

1. Clone the Repository  
git clone https://github.com/quoc10973/Biological-Recognition.git  
cd Biological-Recognition

2. Install Dependencies  
pip install -r requirements.txt

3. Run the Django Server  
python manage.py migrate          # Apply database migrations  
python manage.py runserver       # Start development server

## 📡 API Usage

Swagger UI: Access the interactive API documentation at:  
http://127.0.0.1:8000/api/docs/

Recognize Image API:  
Endpoint: POST /api/predict-v2/  
Content-Type: multipart/form-data  
Field: image

Example using curl:  
curl -X POST http://127.0.0.1:8000/api/predict-v2/ -F "image=@your_image.jpg"

Example response:  
{  
  "predicted_class": "ADN",  
  "confidence": 0.87  
}

## 📝 Notes

- GPU is recommended for faster inference, but the project works on CPU as well.  
- Place the pre-trained MobileNetV2 model inside the /models/ directory.  
- This backend can be integrated with a frontend system for end-user interaction.  
- Designed for educational and experimental use.


