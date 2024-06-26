# Data Scraping and Sentiment Analysis of YouTube Video Comments

This project allows users to perform sentiment analysis on YouTube video comments. It involves three main parts: an HTML form for input, a Google Sheets backend for data storage and comment retrieval, and a Python program for sentiment analysis.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The project consists of:
1. An HTML form to input YouTube video IDs.
2. Google Sheets and Google Apps Script to fetch and store YouTube comments.
3. A Python backend program to analyze comment sentiments using the TextBlob library.

## Features

- **HTML Form**: Collects YouTube video IDs from users.
- **Google Sheets Integration**: Uses Google Apps Script and the YouTube API to fetch and store comments.
- **Sentiment Analysis**: Analyzes the sentiments of comments and presents the results as percentages.

## Technologies Used

- HTML/JavaScript
- Google Sheets & Google Apps Script
- YouTube API
- Python
- TextBlob

## Setup Instructions

1. **HTML Form**: Create an HTML form to collect YouTube video IDs.
2. **Google Sheets**: Set up a Google Sheet and link it with a Google Apps Script to fetch comments using the YouTube API.
3. **Python Program**: Install the required Python libraries (`gspread`, `oauth2client`, `pandas`, `textblob`), and create a script to fetch comments from Google Sheets and perform sentiment analysis.

## Usage

1. Submit a YouTube video ID via the HTML form.
2. Google Sheets will fetch and store the comments.
3. Run the Python script to analyze the sentiments of the comments.

## Contributing

Contributions are welcome! Please create an issue or submit a pull request.

---

This README provides an overview of the Data Scraping and Sentiment Analysis project, including setup instructions and usage guidelines.
