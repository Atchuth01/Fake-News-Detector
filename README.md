# Fake-News-Detector
 Detects whether the news is fake or real.

# AI-Powered Fake News Detection Using Streamlit

## 📌 Project Overview
This project implements an **AI-powered fake news detection system** using **FastText** for text classification and **Streamlit** for a simple and interactive web interface. Users can input a news article, and the model will predict whether the news is **real or fake**.

---

## 🚀 Features
- **FastText-based fake news classification**
- **Interactive web interface with Streamlit**
- **Fast and lightweight deployment**
- **Real-time predictions** with confidence scores

---

## 🛠 Tech Stack
- **Python**
- **FastText** (for NLP text classification)
- **Streamlit** (for web-based UI)
- **Pandas** (for data preprocessing)

---

## 📂 Project Structure
```
FakeNewsDetection/
│── fasttext_model.bin      # Pre-trained FastText model
│── cleaned_train.csv       # Training dataset
│── cleaned_test.csv        # Testing dataset
│── app.py                  # Streamlit application
│── requirements.txt        # Required dependencies
│── README.md               # Project documentation
```

---

## 📥 Installation & Setup
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/FakeNewsDetection.git
cd FakeNewsDetection
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Streamlit App
```bash
streamlit run app.py
```

---

## 🏗 How It Works
1. User inputs a news article.
2. The model **processes the text** and classifies it as **Real News** or **Fake News**.
3. The prediction and confidence score are displayed.

---

## 🎯 Example Predictions
| News Article | Prediction | Confidence |
|-------------|------------|------------|
| "COVID-19 vaccine is ineffective, claims new study." | Fake News | 98.5% |
| "NASA successfully lands rover on Mars." | Real News | 99.2% |
| "Government bans social media platforms permanently." | Fake News | 97.8% |

---

## 🌍 Deployment (Optional)
To deploy the model online, you can use:
- **Streamlit Cloud**
- **Heroku**
- **AWS/GCP**

Example Streamlit Cloud Deployment:
```bash
streamlit share
```

---

## 💡 Future Improvements
- Integrate **more advanced NLP models** (e.g., BERT, RoBERTa)
- Improve dataset quality and size
- Add **multi-language support**

---

## 🤝 Contributing
Pull requests are welcome! Feel free to improve the UI, model accuracy, or deployment options.

---

## 📜 License
MIT License. See `LICENSE` for more details.

---

### 📬 Contact
📩 Email: your.email@example.com  
🔗 GitHub: [YourGitHubProfile](https://github.com/yourusername)

