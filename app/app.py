from flask import Flask, request, render_template
import numpy as np
from PIL import Image
import tensorflow as tf

app = Flask(__name__)

# Load TFLite model
interpreter = tf.lite.Interpreter(model_path="VGG19_model.tflite")
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Class names mapping
class_names = [
    'Corn Common Rust', 'Corn Gray Leaf', 'Corn Healthy', 'Corn Northern Leaf Blight',
    'Potato Early Blight', 'Potato Healthy', 'Potato Late Blight',
    'Rice Brown Spot', 'Rice Healthy', 'Rice Leaf Blast', 'Rice Neck Blast',
    'Wheat Brown Rust', 'Wheat Healthy', 'Wheat Yellow Rust'
]

# Utility: preprocess image
def preprocess_image(image):
    input_shape = input_details[0]['shape']
    height, width = input_shape[1], input_shape[2]
    image = image.resize((width, height))
    image = np.array(image, dtype=np.float32)

    if image.max() > 1:
        image = image / 255.0

    image = np.expand_dims(image, axis=0)
    return image

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return "No file uploaded."

    file = request.files['file']
    if file.filename == '':
        return "No file selected."

    image = Image.open(file.stream).convert('RGB')
    img_array = preprocess_image(image)

    interpreter.set_tensor(input_details[0]['index'], img_array)
    interpreter.invoke()
    output_data = interpreter.get_tensor(output_details[0]['index'])
    predicted_class = np.argmax(output_data)
    predicted_name = class_names[predicted_class]  # Map index to name

    return render_template('result.html', prediction=predicted_name)

if __name__ == '__main__':
    app.run(debug=True)
