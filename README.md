
# Fire & Air Quality Detection System

This project is designed to detect fire using satellite imagery and air quality data for different regions. The system includes a mobile application, an API for handling data, and AI-based detection models.

## Table of Contents
- [Installation](#installation)
- [Mobile Application Setup](#mobile-application-setup)
- [API Setup](#api-setup)
- [AI Detection Setup](#ai-detection-setup)
- [MongoDB Integration](#mongodb-integration)
- [Air Quality Detection](#air-quality-detection)
- [Testing & Usage](#testing-usage)
- [Model Training](#model-training)

## Installation

To get started with the project, clone the repository and install dependencies for both the mobile application and the server.

```bash
git clone https://github.com/devmksaif/FIRE_AIRQUALITY_DETECTION_AI_TSYP.git
cd FIRE_AIRQUALITY_DETECTION_AI_TSYP
```

### Prerequisites
- Node.js (for Expo)
- Python 3.x (for running the server)
- MongoDB (for storing detections)

## Mobile Application Setup

1. **Navigate to the mobile application directory**:
   ```bash
   cd MOBILE_APPLICATION
   ```

2. **Install dependencies using yarn**:
   ```bash
   yarn install
   ```

3. **Run the application using Expo**:
   ```bash
   npx expo start
   ```

This will start the mobile application, and you'll be able to access it via the Expo client on your mobile device or in the browser.

## API Setup

1. **Navigate to the API workspace directory**:
   ```bash
   cd AESS_WORKSPACE
   ```

2. **Install Python dependencies** (make sure to create a virtual environment if needed):
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the API**:
   ```bash
   python server.py
   ```

This will start the API server, and it will be accessible for the mobile application to send and fetch data.

## AI Detection Setup

 

1. **Run the last block of `satellite.ipynb`**:
   Open `satellite.ipynb` in Jupyter Notebook or Jupyter Lab and execute the last block to test the detection system. This will send detection data to the MongoDB database.

## MongoDB Integration

Ensure that MongoDB is running and accessible. The detection data from the AI models will be stored in the database.

1. **Start MongoDB** if it's not already running:
   ```bash
   mongod
   ```

2. **Verify the database**:
   You can use MongoDB’s client tools to ensure the data is being stored in the database correctly.

## Air Quality Detection

Air quality data is updated every 24 hours depending on the region. The API will fetch this data periodically and store it in the MongoDB database.

### Input Features
The following input features are used to predict air quality:

- **PM25**: Particulate Matter (PM) of 2.5 micrometers or smaller.
- **PM10**: Particulate Matter (PM) of 10 micrometers or smaller.
- **Temperature**: The temperature of the region.
- **NO2**: Nitrogen Dioxide concentration.
- **CO**: Carbon Monoxide concentration.
- **O3**: Ozone concentration.

The input data is combined into a matrix `X` for the regression task:

```python
X = combined_data[["PM25", "PM10", "Temperature", "NO2", "CO", "O3"]].values
```

### Output Variables
The system predicts the following output values:

- **AQI_PM10**: Air Quality Index for PM10.
- **AQI_PM25**: Air Quality Index for PM2.5.
- **AQI_NO2**: Air Quality Index for NO2.
- **AQI_O3**: Air Quality Index for O3.
- **AQI_CO**: Air Quality Index for CO.
- **AQI_Max**: Maximum AQI value.

The output is represented by the matrix `y`:

```python
y = combined_data[["AQI_PM10", "AQI_PM25", "AQI_NO2", "AQI_O3", "AQI_CO", "AQI_Max"]].values
```

This is a **multi-output regression** problem where multiple AQI values are predicted for different pollutants based on the input features.

## Testing & Usage

1. **Test the fire detection system** by running the last block of `satellite.ipynb`, which will send the AI detection results to MongoDB.
   
2. **Test the air quality detection** by ensuring the server fetches and updates the air quality data every 24 hours.

3. **Check the mobile app** for recent fire and air quality detection updates.

## Model Training

### Fire Detection (Satellite Imagery)

The fire detection system uses **YOLOv8 S** (You Only Look Once version 8, small model) for detecting fires in satellite imagery. YOLOv8 is a state-of-the-art object detection algorithm known for its speed and accuracy, making it ideal for detecting fires from satellite images in real-time.

- **Training Dataset**: The model was trained on a large dataset of satellite images containing labeled fire regions.
- **Model Type**: YOLOv8 S (small) for faster inference on resource-constrained devices.
  
### Air Quality Detection

The air quality detection system uses **TensorFlow** for processing and analyzing air quality data. TensorFlow, a powerful machine learning library, was used to train a model that predicts air quality levels based on region-specific parameters.

- **Training Dataset**: The model was trained on historical air quality data, including measurements such as PM2.5, CO2, and other air pollutants.
- **Model Type**: TensorFlow-based neural network for regression tasks, predicting air quality scores based on location data.
  
### Multi-Output Regression

The air quality model is designed as a multi-output regression task. It predicts multiple air quality index values (AQI) for different pollutants (PM10, PM25, NO2, O3, CO) based on the environmental data (temperature, CO, NO2, etc.) in real-time.

## Additional Notes
- Ensure all dependencies are installed before running the project.
- The system relies on MongoDB for data storage, so make sure it is correctly configured and running.
- The air quality detection system runs on a 24-hour cycle, and the application fetches updated information from the server regularly.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

 Wildfire and Air Quality Detection Application User Manual

## Overview

This application provides two main features:

1. **Wildfire Detection** - Displays the latest fire detection using satellite imagery.
2. **Air Quality Detection** - Displays the Air Quality Index (AQI) for various pollutants and provides real-time AQI updates.

The application is designed to track fire occurrences and monitor air quality, offering real-time insights and predictions to users.

---

## Features

### 1. **Wildfire Tab**: 
- **Description**: This tab shows the latest fire detection using satellite imagery. The AI model analyzes satellite images to detect fire incidents and provides real-time updates.
- **How to Use**:
  - Navigate to the **Wildfire Tab** in the app.
  - You will see the most recent fire detection events, including information such as fire location, timestamp, and detection confidence.

### 2. **Air Quality Tab**:
- **Description**: This tab shows the average Air Quality Index (AQI) for the country and provides insights into various air pollutants.
- **How to Use**:
  - Navigate to the **Air Quality Tab** in the app.
  - The **Average AQI** for the country will be displayed, providing a general view of air quality.
  - Additionally, specific AQI values for the following pollutants are shown:
    - **AQI_PM10**: Air Quality Index for PM10.
    - **AQI_PM25**: Air Quality Index for PM2.5.
    - **AQI_NO2**: Air Quality Index for NO2.
    - **AQI_O3**: Air Quality Index for O3.
    - **AQI_CO**: Air Quality Index for CO.
    - **AQI_Max**: Maximum AQI value observed.

### 3. **Location Tab**:
- **Description**: This tab shows your current location and the corresponding AQI for the area.
- **How to Use**:
  - Navigate to the **Location Tab** in the app.
  - Your current location is displayed on a map.
  - The app fetches the real-time AQI for your location and provides details on the air quality based on various pollutants.

---

## AQI Definitions

The Air Quality Index (AQI) is a numerical scale used to represent the quality of air in a specific area. The app monitors the following pollutants:

- **PM10**: Particulate matter with a diameter of 10 micrometers or less.
- **PM2.5**: Fine particulate matter with a diameter of 2.5 micrometers or less.
- **NO2**: Nitrogen Dioxide, a gas that can irritate the respiratory system.
- **CO**: Carbon Monoxide, a colorless, odorless gas that can be harmful at high concentrations.
- **O3**: Ozone, which can irritate the respiratory system.
- **AQI_Max**: The maximum AQI value for all monitored pollutants in the region.

---

## Application Workflow

1. **Wildfire Detection**:
   - The **satellite imagery detection** model is based on **YOLOv8 S**, which detects fire incidents in real-time using satellite images.
   - Once a fire is detected, the data is sent to a **MongoDB database**, and the mobile application fetches the most recent detection data for display.

2. **Air Quality Detection**:
   - Air quality data is fetched using real-time monitoring from various sensors.
   - The model for air quality prediction is trained using **TensorFlow**, based on the following inputs:
     - **PM25**, **PM10**, **Temperature**, **NO2**, **CO**, **O3**
   - The output provides AQI values for each pollutant and the maximum AQI observed.

---

## Conclusion

This application helps users stay informed about wildfire incidents and monitor air quality. With real-time data updates and easy navigation, it ensures that users can make informed decisions about their health and safety.

