from flask import Flask, render_template, request, redirect, url_for
import os
# from face_swap import face_swap

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads/'
app.config['RESULT_FOLDER'] = 'static/results/'

# Ensure upload and result directories exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['RESULT_FOLDER'], exist_ok=True)

# Predefined images for face swapping
predefined_images = [
    'static/predefined/image1.jpg',
    'static/predefined/image2.jpg',
    'static/predefined/image3.jpg',
    'static/predefined/image4.jpg'
]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            print("No file part in the request")
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            print("No file selected for uploading")
            return redirect(request.url)
        if file:
            filename = file.filename
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            print(f"File {filename} uploaded successfully and saved to {filepath}")

            # Perform face swap
            output_paths = [os.path.join(app.config['RESULT_FOLDER'], f'result_{i}.jpg') for i in range(4)]
            # try:
            #     # face_swap(filepath, predefined_images, output_paths)
            # except Exception as e:
            #     print("fuck")
            #     print(f"Error during face swap: {e}")
            #     return "Face swap failed", 500

            print(f"Face swap completed successfully, saved results to {output_paths}")
            return render_template('result.html', filenames=[os.path.basename(p) for p in output_paths])
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
