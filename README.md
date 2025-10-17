# 🌿 Crop Disease Detector Web App

> *“The future of farming isn’t in the soil — it’s in the data.”*

An AI-powered web application that detects crop diseases using deep learning. Built with **TensorFlow**, **Flask**, and a fine-tuned **VGG19 model**, this project aims to support farmers and agricultural experts with quick, reliable disease detection directly from leaf images.

---

## 🚀 Features

* 🧠 Deep Learning Model (VGG19) trained on thousands of diseased and healthy crop images
* 🌱 Detects multiple crop diseases with high accuracy
* 💻 Clean and responsive web interface (Flask + HTML/CSS)
* ⚙️ Real-time predictions from uploaded images
* 🧾 Modular and scalable architecture for future model updates

---

## 🗂️ Project Structure

```
Crop Disease Detector Web App/
│
├── app/
│   ├── app.py                # Main Flask application
│   ├── templates/
│   │   ├── index.html        # Upload page
│   │   └── result.html       # Prediction result page               # CSS, images, JS (if any)
│   └── VGG19_model.tflite    # Trained model (excluded from GitHub)
│
├── Notebook/
│   └── crop-disease-detector.ipynb  # Model training and experimentation
│
├── requirements.txt          # Python dependencies  
├── .gitignore                # Ignored large files and dataset  
└── README.md
```

---

## 📊 Dataset

The model was trained on a curated dataset available on Kaggle:
👉 [Crop Disease Dataset on Kaggle](https://www.kaggle.com/datasets/sawabedarain/dataset)

> *“Every pixel has a story; the model just needs to listen.”*

---

## ⚡ Tech Stack
____________________________________________________________
| Layer          | Technologies Used                       |
| -------------- | --------------------------------------- |
| **Frontend**   | HTML, CSS, Flask Templates              |
| **Backend**    | Python (Flask Framework)                |
| **Model**      | TensorFlow / Keras (VGG19 Architecture) |
| **Deployment** | Localhost / Future Cloud Hosting        |
| **Dataset**    | Custom Kaggle Dataset                   |
|__________________________________________________________|

---

## 🧠 How It Works

1. **Upload** a crop image via the web interface
2. **Preprocessing** ensures consistent image dimensions
3. **Model Prediction** classifies disease type
4. **Output Displayed** with user-friendly interpretation

---

## 🔧 Setup Instructions

```bash
# Clone the repository
git clone https://github.com/DarainHyder/Crop-Disease-Detector-Web-App.git
cd Crop-Disease-Detector-Web-App

# Install dependencies
pip install -r requirements.txt

# Run the app
cd app
python app.py
```

Then open your browser at `http://127.0.0.1:5000/`

---

## 🧩 Future Enhancements

* Integration with **live camera feeds** for real-time diagnosis
* Expand to detect **more crop species**
* Deploy on **Streamlit / AWS / Hugging Face Spaces**
* Add **disease treatment recommendations**

---

## 💬 Author

**Syed Darain Hyder Kazmi**
🎓 BS Computer & Information Sciences
🔗 [LinkedIn](https://www.linkedin.com/in/syed-darain-hyder-kazmi-a45a70306) | [GitHub](https://github.com/DarainHyder) | [Kaggle](https://www.kaggle.com/sawabedarain)

> *“Technology grows the fields now — we just plant the code.”*

---

## 🪶 License

This project is licensed under the **MIT License** — free to use, modify, and distribute.

---

*Made with code, caffeine, and a vision for smarter agriculture.* 🌾
