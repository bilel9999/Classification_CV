from flask import Flask, render_template, request, redirect, send_from_directory, url_for
from pyresparser import ResumeParser
import os
import joblib
import encoding


app = Flask(__name__)

loaded_model = joblib.load('random_forest_model.joblib')



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return render_template('CLASSIFICATION.html', result="No file provided")

    file = request.files['file']

    if file.filename == '':
        return render_template('CLASSIFICATION.html', result="No selected file")

    try:
        # Save the uploaded file to a temporary location
        upload_folder = 'uploads'
        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)

        file_path = os.path.join(upload_folder, file.filename)
        file.save(file_path)

        # Extract text using ResumeParser
        text = extract_text_from_resume(file_path)
        text["file_path"] = file_path
        
        # Return result to the template
        return render_template('CLASSIFICATION.html', result=text, filename=file.filename) 
    except FileNotFoundError:
        return render_template('CLASSIFICATION.html', result="File not found")
    except PermissionError:
        return render_template('CLASSIFICATION.html', result="Permission error while saving file")
    except Exception as e:
        return render_template('CLASSIFICATION.html', result=f"Error processing file: {str(e)}")

# Add a new route to serve the uploaded PDF file
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory('uploads', filename)

# Your existing route for classification page
@app.route('/go_to_classification')
def go_to_classification():
    return render_template('CLASSIFICATION.html')


def extract_text_from_resume(file_path):
    print("path" , file_path)
    data = ResumeParser(file_path).get_extracted_data()

    Keywords = ["education",
                "summary",
                "accomplishments",
                "executive profile",
                "professional profile",
                "personal profile",
                "work background",
                "academic profile",
                "other activities",
                "qualifications",
                "Experience",
                "interests",
                "skills",
                "achievements",
                "publications",
                "publication",
                "certifications",
                "workshops",
                "projects",
                "internships",
                "trainings",
                "hobbies",
                "overview",
                "objective",
                "position of responsibility",
                "jobs"
                ]

    keys = []
    for key in Keywords:
        
        if key in list(data.keys()):
            keys.extend(data[key])
    test_data = " , ".join(keys)
    test_data = test_data.lower()
    test = encoding.encode_text(test_data)
    
    test = test.reshape(1, -1)
    l = ['big data', 'cyber', 'data science', 'embeded', 'iot', 'mobile', 'software engineering', 'web']

    
    test=loaded_model.predict_proba(test)
    test=test.tolist()[0]
    x = list(zip(test,l))
    x = sorted(x , reverse=True)
    
    d={}
    d["data"] = test_data
    d["prediction"]= x
    d["name"]= data["name"]
    d["email"]= data["email"]
    d["mobile_number"]= data["mobile_number"]
    
    return d


if __name__ == '__main__':
    app.run(debug=True)