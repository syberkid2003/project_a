import cv2 , os
import face_recognition
from django.conf import settings
from test.models import Cheat_sheet
from io import BytesIO
from django.shortcuts import  redirect

face_detection_videocam = cv2.CascadeClassifier(os.path.join(
			settings.BASE_DIR,'face/haarcascade_frontalface_default.xml'))

class VideoCamera(object):
	def __init__(self):
		self.video = cv2.VideoCapture(0)

	def __del__(self):
		self.video.release()

	def get_frame(self):
		success, image = self.video.read()
		# We are using Motion JPEG, but OpenCV defaults to capture raw images,
		# so we must encode it into JPEG in order to correctly display the
		# video stream.

		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		faces_detected = face_detection_videocam.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
		for (x, y, w, h) in faces_detected:
			cv2.rectangle(image, pt1=(x, y), pt2=(x + w, y + h), color=(255, 0, 0), thickness=2)
		frame_flip = cv2.flip(image,1)
		ret, jpeg = cv2.imencode('.jpg', frame_flip)
		return jpeg.tobytes()

prev_face_x, prev_face_y = None, None

class FaceTracker:
    def __init__(self, name, hall, sub, sub_id):
        self.camera = cv2.VideoCapture(0)
        self.prev_face_x = None
        self.prev_face_y = None
        self.name = name
        self.hall = hall
        self.sub = sub
        self.sub_id = sub_id

    def __del__(self):
        self.camera.release()

    def track_faces(self, frame):
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        box = face_recognition.face_locations(frame_rgb)
        if len(box) == 1:
            curr_face_x = (box[0][3] + box[0][1]) / 2
            curr_face_y = (box[0][0] + box[0][2]) / 2
            if self.prev_face_x is not None and self.prev_face_y is not None:
                if curr_face_x != self.prev_face_x  or curr_face_y != self.prev_face_y:
                    cv2.putText(frame, "don't look out side!", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                    
                
            self.prev_face_x = curr_face_x
            self.prev_face_y = curr_face_y
        elif len(box) > 1:
            # Display message if two or more faces are detected
            cv2.putText(frame, "Why did the second person watch?!", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        else:
            # Display message if no face is recognized
            cv2.putText(frame, "Sit Properly!", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        cheat_data = Cheat_sheet(name=self.name, hall_ticket=self.hall, test=self.sub, test_id=self.sub_id)
        frame_bytes = cv2.imencode('.jpg', frame)[1].tobytes()
        frame_io = BytesIO(frame_bytes)
        cheat_data.pic.save(f"{self.name}_cheat.jpg", frame_io)
        cheat_data.save()
        return frame

    def gen(self):
        while True:
            success, frame = self.camera.read()
            if not success:
                break

            # Resize frame for better performance
            frame = cv2.resize(frame, (640, 480))

            # Track faces in the frame
            frame_with_tracking = self.track_faces(frame)

            # Encode the frame as JPEG
            ret, jpeg = cv2.imencode('.jpg', frame_with_tracking)
            if not ret:
                break

            # return redirect("user_home")
            # Convert the JPEG bytes to bytes-like object
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n\r\n')




