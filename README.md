# TIN Verification API

This API fetches the TIN (Taxpayer Identification Number) Details.

## Table of Contents

- [Features](#Features)
- [Installation](#Installation)
- [Usage](#Usage)
- [Endpoints](#EndPoints)
- [State Codes](#StateCodes)
- [Support](#Support)
- [Contribution](#Contribution)

## Features

- It Maintains session information for handling dynamic captcha url.
- Sends TIN and captcha to get the TIN Details
- Return all the details related to taxpayer in JSON Format.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/shubham-dube/TIN-Verification-API.git
   cd TIN-Verification-API
   
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   venv\Scripts\activate # On Linux use `source venv/bin/activate`
   
3. Install the dependencies:
   ```bash
   pip install flask requests uuid base64 bs4 re html

4. Run the Application:
   ```bash
   python app.py
 *The API will be available at http://127.0.0.1:5000 .*
 
## Usage
- Fetch the captcha and show it to the user with two inputs to enter captcha and TIN number
- Send the TIN entered and captcha along with the session id recieved.
- You will get all the Details related to that TIN in JSON Format.
  
## EndPoints

### Fetching Captcha

**Endpoint:** `/api/v1/getCaptcha`

**Method:** `GET`

**Description:** `This Endpoint the captcha as a base64 image format encoding`

**Response**
```json
{
  "sessionId": true,
  "image": 'data:image/png;base64, captchaBase64 '
}
```
**Status Codes**
- 200 OK : `Captcha Fetched`

### Get Vehicle Challan Details

**Endpoint:** `/api/v1/getTINdetails`

**Method:** `POST`

**Description:** `Submits the TIN and captcha along with session id to retrieve the TIN Details`

**Request Body:**
```json
{
  "sessionId": "OBTAINED ON FETCHING CAPTCHA",
  "TIN": "19200204057",
  "captcha": "your_captcha_here"
}
```
**Response**
```json
{
    "CSTNumber": "19200204057",
    "PAN": "AABCC0202E",
    "TIN": "19200204057",
    "dateOfRegistration": "10/03/03",
    "dealerAddress": "247 DIAMOND HARBOUR ROAD PO-PAILAN         KOLKATA PAILAN  700104",
    "dealerName": "CRADEL PHARMACEUTICALS P LTD",
    "registrationStatus": "Active",
    "state": "West Bengal",
    "validAsOn": "10/02/15"
}
```
**Status Codes**
- 200 OK : `Data Retrieved Successfuly`
  
## Support
For Support Contact me at itzshubhamofficial@gmail.com
or Mobile Number : `+917687877772`

## Contribution

We welcome contributions to improve this project. Here are some ways you can contribute:

1. **Report Bugs:** If you find any bugs, please report them by opening an issue on GitHub.
2. **Feature Requests:** If you have ideas for new features, feel free to suggest them by opening an issue.
3. **Code Contributions:** 
    - Fork the repository.
    - Create a new branch (`git checkout -b feature-branch`).
    - Make your changes.
    - Commit your changes (`git commit -m 'Add some feature'`).
    - Push to the branch (`git push origin feature-branch`).
    - Open a pull request.

4. **Documentation:** Improve the documentation to help others understand and use the project.
5. **Testing:** Write tests to improve code coverage and ensure stability.

Please make sure your contributions adhere to our coding guidelines and standards.
