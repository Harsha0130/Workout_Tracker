# Exercise Tracker

This project tracks exercises and records workout data using the Nutritionix API and Sheety API.

- This project is part of the "100 Days of Code: The Complete Python Pro Bootcamp for 2023" course by Dr. Angela Yu. -- (Day-38)

## Project Overview

### Purpose

Developed a Python script to log exercises and store workout data in a Google Sheet. Users input exercise details, which are processed to record the exercise name, duration, and calories burned.

### API Integration

Integrated the Nutritionix API (`https://trackapi.nutritionix.com/v2/natural/exercise`) to fetch exercise data by providing user details like gender, height, weight, and age.

### Exercise Data Analysis

The script sends a query to the Nutritionix API and processes the response to extract relevant exercise information. It then logs this information, including the exercise name, duration, and calories burned, into a Google Sheet via the Sheety API.

### Sheety Integration

Utilized Sheety's REST API to update the Google Sheet with the exercise data. Each entry includes the date, time, exercise name, duration, and calories burned.

## Prerequisites

Ensure you have Python installed and install the following library:

- requests

## Usage

Replace placeholders in the script with your API credentials:
   - Replace `API_ID` with your Nutritionix API ID.
   - Replace `API_KEY` with your Nutritionix API Key.
   - Replace `Authorization` header value in `header2` with your Sheety API credentials.
