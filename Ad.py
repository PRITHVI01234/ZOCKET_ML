import streamlit as st
from keras.preprocessing import image
from keras.models import load_model
import pandas as pd
import base64

# Load your model
model = load_model("Ident.h5")

# File path for storing predictions
history_file_path = "prediction_historysd.csv"

# Function to encode image as base64
def encode_image_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        encoded_img = base64.b64encode(img_file.read()).decode("utf-8")
    return f"data:image/png;base64,{encoded_img}"

class History:
    def __init__(self):
        self.container = self.load_history()

    def load_history(self):
        try:
            history_df = pd.read_csv(history_file_path)
            if not history_df.empty:
                return list(zip(history_df["Image Name"], history_df["Prediction"], history_df["Classification"], history_df["Confidence"]))
        except (FileNotFoundError, pd.errors.EmptyDataError):
            pass
        return list()

    def save_history(self):
        history_df = pd.DataFrame(self.container, columns=["Image Name", "Prediction", "Classification", "Confidence"])
        history_df.to_csv(history_file_path, index=False)

    def clear(self):
        self.container = list()
        self.save_history()

    def display(self):
        if not self.container:
            st.sidebar.warning("No history available.")
        else:
            st.sidebar.subheader("Prediction History")
            for idx, (image_name, prediction, classification, confidence) in enumerate(self.container, 1):
                st.sidebar.markdown(f"**Prediction {idx}:**")
                st.sidebar.text(f"Image Name: {image_name}")
                st.sidebar.text(f"Prediction: {prediction}")
                st.sidebar.text(f"Classification: {classification}")
                st.sidebar.text(f"Confidence: {confidence:.2f}")
                st.sidebar.markdown("---")

    def add(self, image_name, prediction, classification, confidence):
        self.container.append((image_name, prediction, classification, confidence))
        self.save_history()

# Create an instance of the History class
ImageHistory = History()

# Your predict function
def predict(image_path):
    # Placeholder: Replace with your actual implementation
    # Load and preprocess the image
    img = image.load_img(image_path, target_size=(200, 200))
    img_array = image.img_to_array(img)
    img_array = img_array.reshape((1, 200, 200, 3))
    img_array /= 255.0

    # Make a prediction
    prediction = model.predict(img_array)

    # Extract the confidence score
    confidence_score = prediction[0][0]

    # Convert the prediction to a binary label (0 or 1)
    predicted_label = int(round(confidence_score))

    # Placeholder: Add your logic for creative vs non-creative classification
    classification = "Ad Creative" if predicted_label == 0 else "Non-Ad Creative"

    return predicted_label, classification, confidence_score

# Your Streamlit app code
st.set_page_config(
    page_title="Ad - Creative Classifier",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Encode background image to Base64
background_image_path = "5f3c36ed97b4991975c3c818_creative intelligence.jpg"
background_image_base64 = encode_image_to_base64(background_image_path)

st.markdown(
    f"""
    <style>
        body {{
            background-image: url('{background_image_base64}');
            background-size: 100% 100px;
            font-family: 'Arial', sans-serif;
        }}
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Ad - Creative Classifier")

st.sidebar.image("zocket12-transformed-transformed.png", use_column_width=True)
st.sidebar.title("Ad - Creative Classifier")
st.sidebar.subheader("A Profound Submission in Ad-Creative Detection and Feature Extraction")
st.sidebar.write("Mod By Prithvi Ragavendiran R")

header_image_path = "5f3c36ed97b4991975c3c818_creative intelligence.jpg"
st.image(header_image_path, use_column_width=True, caption="Ad - Creative Classifier")

uploaded_image = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])

if uploaded_image:
    st.image(uploaded_image, caption="Uploaded Image.", use_column_width=True)

    if st.button("Continue to Prediction"):
        image_name = uploaded_image.name
        image_path = "temp_image.jpg"
        with open(image_path, "wb") as f:
            f.write(uploaded_image.getbuffer())

        prediction, classification, confidence_score = predict(image_path)

        st.subheader("Prediction Result:")
        label = "Creative" if prediction == 0 else "Non-Creative"
        st.success(f"This image is predicted to be {label} with confidence score: {confidence_score:.2f}.")

        # Use the correct method here
        ImageHistory.add(image_name, label, classification, confidence_score)

if st.button("Clear History"):
    ImageHistory.clear()

ImageHistory.display()

