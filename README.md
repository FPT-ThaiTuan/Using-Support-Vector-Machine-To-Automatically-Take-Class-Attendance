1. Abstract 
- Attendance marking in a classroom during a lecture is not only an onerous task but also a time consuming one at that. Due to an unusually high number of students present during the lecture there will always be a probability of proxy attendance(s).Attendance marking with conventional methods has been an area of challenge. The growing need of efficient and automatic techniques of marking attendance is a growing challenge in the area of face recognition. In recent years, the problem of automatic attendance marking has been widely addressed through the use of standard biometrics like fingerprint and Radio frequency Identification tags etc., However,these techniques lack the element of reliability. In this proposed project an automated attendance marking and management system is proposed by making use of face detection and recognition algorithms. Instead of using the conventional methods, this proposed system aims to develop an automated system that records the student’s attendance by using facial recognition technology. The main objective of this work is to make the attendance marking and management system efficient, time saving, simple and easy. Here faces will be recognized using face recognition algorithms. The processed image will then be compared against the existing stored record and then attendance is marked in the database accordingly. Compared to the existing system's traditional attendance marking system, this system reduces the workload of people. This proposed system will be implemented with 4 phases such as Image Capturing, Segmentation of group image and Face Detection, Face comparison and Recognition, Updating of Attendance in database.

2. Data Preparation : 
- For our group's project, the preparation of data was collected from taking pictures of students in class AI1601. And here is the step-by-step implementation of data preparation.
- First, our team designed a program with the support of two libraries Open CV and OS Module in python language. With the Open CV library, it will support us to access the optional camera on the device to take each picture in each frame of the video. And the OS Module library helps us check if the path of the directory containing the collected data exists or not.
- Specifically, the program does the first thing to enter the ID of each student, it is also the folder name in the dataset. The next job is to take 100 pictures and save it to the folder created in the dataset.

3. Method
- Face images
- Detect face
- Embed face
- Train a classifier

4. Conclusion and Perspectives 
- This system  aims  to  build  an  effective  class  attendance system using face recognition techniques. The proposed system will be able to mark the attendance via face Id. It will detect faces via webcam and then recognize the faces. After recognition,  it  will  mark  the  attendance  of  the  recognized student and update the attendance record.

- There is no need for specialized hardware for installing the system as it only uses a computer and a camera. The camera plays a crucial role in the working of the system hence the image quality and performance of the camera in real time scenario must be tested especially if the system is operated from a live camera feed. As long as the picture capture conditions (e.g., light, face, distance and expressions) are constant, face recognition accuracy is approximately 80%. The training dataset should be updated timely to match with students’ changes.

