from flask import Blueprint, render_template, url_for
from pyzbar.pyzbar import decode
import requests
import pytesseract
import pyttsx3
import cv2

main = Blueprint('main', __name__)

def get_products():
    response = requests.get('https://fakestoreapi.com/products?limit=10')
    return response.json()



@main.route('/')
def index():
    return render_template('index.html')

@main.route('/home')
def home():
    products = get_products()
    return render_template('home.html',products=products)


@main.route('/open-camera', methods=['POST'])
def open_camera():
    # # open the camera
    cap = cv2.VideoCapture(0)

    while True:
        _, frame = cap.read()

        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Decode barcodes in the frame
        barcodes = decode(gray)

        # Initialize the Text-to-speech engine
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)

        # Set the volume of the engine
        engine.setProperty('volume', 0.7)

        # Set the voice of the engine
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[10].id)

        # Use OCR to read text from the frame
        # text = pytesseract.image_to_string(gray)

        # If no barcodes are detected, read text from the frame
        if len(barcodes) == 0:
            # Speak the text
            # Use OCR to read text from the frame
            text = pytesseract.image_to_string(gray)
            engine.say(text)

            # Wait until the text is spoken
            engine.runAndWait()

            # Display the extracted text on the frame
            cv2.putText(frame, text, (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

        else:
            # Loop over the detected barcodes
            for barcode in barcodes:
                # Extract the barcode data and type
                data = barcode.data.decode("utf-8")
                type = barcode.type

                text= pytesseract.image_to_string(data)

                # Draw a bounding box around the barcode
                (x, y, w, h) = barcode.rect
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                # Display the barcode data and type on the frame
                cv2.putText(frame, f"{data} ({type})", (x, y - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

                engine.say(text)
                engine.runAndWait()

        # Display the frame
        cv2.imshow("Barcode Scanner", frame)

        # Exit if 'Esc' key is pressed
        if cv2.waitKey(1) == 27:
            break

    # Release the capture and destroy the window
    cap.release()
    cv2.destroyAllWindows()

    return render_template('camera.html')


if __name__ == '__main__':
    main.run(debug=True)
