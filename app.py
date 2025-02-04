from flask import Flask, render_template, Response
import cv2


app = Flask(__name__)
# 0 ensures that we are using our own camera/webcam
camera = cv2.VideoCapture(1)


def generate_frames():
    while True:
        success, frame = camera.read()
        # success is a boolean variable that tells us weather we are able to read from the camera or not.
        if not success:
            break
        else:
            ret, buffer = cv2.imencode(".jpg", frame)
            frame = buffer.tobytes()

        yield (b"--frame\r\r" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/video")
def video():
    return Response(
        generate_frames(), mimetype="multipart/x-mixed-replace; boundry = frame"
    )


if __name__ == "__main__":
    app.run(debug=True)
