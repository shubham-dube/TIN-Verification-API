from flask import Flask, jsonify, Response, make_response, request
import requests
import uuid
import base64
from bs4 import BeautifulSoup
import re
import html

app = Flask(__name__)

captcha = "https://www.tinxsys.com/TinxsysInternetWeb/images/simpleCaptcha.jpg"

sessions = {}

@app.route("/api/v1/getCaptcha", methods=["GET"])
def getCaptcha():
    try:
        session = requests.Session()
        id = str(uuid.uuid4())

        session.verify = False

        session.post("https://www.tinxsys.com/TinxsysInternetWeb/searchByTin_Inter.jsp",data={"backPage": "searchByTin_Inter.jsp"} )
        response = session.get(captcha)
        captchaBase64 = base64.b64encode(response.content).decode("utf-8")

        # # For Testing Purpose only

        # imageString = f'<img src="data:image/png;base64,{captchaBase64}" alt="captcha">'
        # with open('captcha.html','w') as f:
        #     f.write(imageString)   
        #     f.close()

        # #

        sessions[id] = {
            "session": session
        }

        json_response = {
            "sessionId": id,
            "image": "data:image/png;base64," + captchaBase64,
        }

        return jsonify(json_response)
    
    except Exception as e:
        print(e)
        return jsonify({"error": "Error in fetching captcha"})
    

@app.route("/api/v1/getTINdetails", methods=["POST"])
def getTINdetails():
    try:
        sessionId = request.json.get("sessionId")
        TIN = request.json.get("TIN")
        captcha = request.json.get("captcha")

        user = sessions.get(sessionId)

        session = user['session']
        if session is None:
            return jsonify({"error": "Invalid session id"})

        print(TIN)
        print(captcha)
        params = {
            "tinNumber": TIN,
            "answer": captcha,
            "searchBy": "TIN",
            "backPage": "searchByTin_Inter.jsp"
        }

        response = session.get(
            f"https://www.tinxsys.com/TinxsysInternetWeb/dealerControllerServlet?tinNumber={TIN}&answer={captcha}&searchBy=TIN&backPage=searchByTin_Inter.jsp"
        )
        htmlString = response.text
        cleaned_html_string = htmlString.replace('\n', '').replace('\r', '').replace('\t', '').replace('\\', '').replace('\\u00a0', '').replace('\"', '')
        cleaned_html_string = html.unescape(cleaned_html_string)

        soup = BeautifulSoup(cleaned_html_string, 'html.parser')

        mainTable = soup.find_all('table')[2]

        tableRows = mainTable.find_all('tr')

        try:
            tin = tableRows[1].find_all('td')[1].get_text().strip()
            cstNo = tableRows[2].find_all('td')[1].get_text().strip()
            dealerName = tableRows[3].find_all('td')[1].get_text().strip()
            dealerAddress = tableRows[4].find_all('td')[1].get_text().strip().replace('                         ', ' ').replace('               ', '')
            state = tableRows[5].find_all('td')[1].get_text().strip()
            PAN = tableRows[6].find_all('td')[1].get_text().strip()
            dateOfReg = tableRows[7].find_all('td')[1].get_text().strip()
            regStatus = tableRows[8].find_all('td')[1].get_text().strip()
            validAsOn = tableRows[9].find_all('td')[1].get_text().strip()
        except:
            return jsonify({"error": "Invalid Details"})

        TINdetails = {
            "TIN": tin,
            "CSTNumber": cstNo,
            "PAN": PAN,
            "dealerName": dealerName,
            "dealerAddress": dealerAddress,
            "state": state,
            "dateOfRegistration": dateOfReg,
            "registrationStatus": regStatus,
            "validAsOn": validAsOn
        }
        
        return jsonify(TINdetails)
    
    except Exception as e:
        print(e)
        return jsonify({"error": "Error in fetching TIN Details"})


if __name__ == "__main__":
    app.run()
