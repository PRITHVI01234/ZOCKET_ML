# Zocket Machine Learning (Computer Vision) Hackathon - Ad Creative Recognition

## Project Overview:

Welcome to the Zocket Machine Learning (Computer Vision) Hackathon! In this exciting competition, I had the opportunity to showcase my skills in developing a model for Ad Creative Recognition using a pre-trained VGG16 model in Computer Vision. The primary goal of the project was to leverage transfer learning techniques to automatically recognize and categorize ad creatives, enhancing the efficiency of advertising processes.

## Project Details:

- **Name:** R Prithvi Ragavendiran
- **College:** Chennai Institute of Technology

## Model Description:

The developed model utilizes the pre-trained VGG16 architecture for image recognition tasks. By fine-tuning the model on a dataset of ad creatives, it learned to extract relevant features and categorize ads based on their content. This approach eliminates the need for OCR, providing an efficient and effective solution for ad creative recognition.

## Key Features:

- **Transfer Learning:** Leveraging the pre-trained VGG16 model for feature extraction.
- **Visual Element Identification:** Implementing transfer learning techniques to identify and classify visual elements within the ad creative.
- **Content Categorization:** Using the fine-tuned model to categorize ads based on their content.

## Technologies Used:

- Python
- TensorFlow
- Keras (for VGG16 model)
- OpenCV
- Other relevant machine learning and computer vision libraries.

## Running the Model:

To run the ad recognition model and explore the results using the Ad Streamlit file, follow these steps:

1. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

2. **Load the Model:**
    ```python
    from tensorflow.keras.models import model_from_json, save_model
    
    # Load the architecture from the JSON file
    with open('model_architecture.json', 'r') as json_file:
        loaded_model = model_from_json(json_file.read())

    # Load the weights
    loaded_model.load_weights('model_weights.h5')

    # Save the entire model (architecture and weights) as an HDF5 file
    save_model(loaded_model, 'ad_recognition_model.h5')
    ```

3. **Run the Ad Streamlit File:**

    ```bash
    streamlit run AD.py 
    ```

4. **Input the Path to the Ad Creative Image when Prompted.**

   Choose the image you want to do predictions on by choosing the image from your desktop or anyother

5. **Explore the Results:**

   The Ad Streamlit file will display the results and insights provided by the model.

## Acknowledgments:

I would like to express my gratitude to Zocket for organizing this hackathon and providing a platform for showcasing innovative solutions in the field of computer vision and machine learning. Additionally, I appreciate the support and guidance from my peers and mentors throughout the development process.

Feel free to reach out for any inquiries or collaborations!

**Happy Hacking!**

## Acknowledgments:

A big thank you to Zocket for hosting this hackathon and providing a platform for innovation in computer vision and machine learning. Special appreciation for the continuous support from my peers and mentors throughout development.

Zocket, a trailblazer in ad creation (ad creation in 30 seconds!), served as a major inspiration for this project.

```python
# Feel the gratitude
print("Thank you, Zocket!")

