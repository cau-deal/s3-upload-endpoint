from flask import Flask, render_template, flash, request
from flask_wtf import Form
from flask_wtf.file import FileField
from tools import s3_upload

app = Flask(__name__)
app.config.from_object('config')


class UploadForm(Form):
    example = FileField('Example File')

@app.route("/upload", methods=['POST'])
def upload_file():
    file = request.files['file']
    type = request.form['type']
    output = s3_upload(file, upload_dir=type)
    return output


@app.route("/upload1", methods=['POST'])
def upload_file1():
    file = request.files['file']
    type = request.form['type']
    output = s3_upload(file, upload_dir=type)
    return output

@app.route("/upload2", methods=['POST'])
def upload_file2():
    file = request.files['file']
    type = request.form['type']
    output = s3_upload(file, upload_dir=type)
    return output

@app.route("/upload3", methods=['POST'])
def upload_file3():
    file = request.files['file']
    type = request.form['type']
    output = s3_upload(file, upload_dir=type)
    return output

@app.route("/upload4", methods=['POST'])
def upload_file4():
    file = request.files['file']
    type = request.form['type']
    output = s3_upload(file, upload_dir=type)
    return output

@app.route("/upload5", methods=['POST'])
def upload_file5():
    file = request.files['file']
    type = request.form['type']
    output = s3_upload(file, upload_dir=type)
    return output

@app.route("/upload6", methods=['POST'])
def upload_file6():
    file = request.files['file']
    type = request.form['type']
    output = s3_upload(file, upload_dir=type)
    return output





if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=5000
    )
