# import cv2
# import dlib
# import numpy as np

# def face_swap(source_path, target_paths, output_paths):
#     # Load Dlib's face detector and shape predictor
#     detector = dlib.get_frontal_face_detector()
#     predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

#     # Read the source image
#     source_img = cv2.imread(source_path)

#     # Convert the source image to grayscale
#     source_gray = cv2.cvtColor(source_img, cv2.COLOR_BGR2GRAY)

#     # Detect faces in the source image
#     source_faces = detector(source_gray)

#     # If no face is detected in the source image, return
#     if len(source_faces) == 0:
#         print("No face detected in the source image.")
#         return

#     # Get the landmarks of the first face detected in the source image
#     source_face = source_faces[0]
#     source_landmarks = predictor(source_gray, source_face)
#     source_points = np.array([[p.x, p.y] for p in source_landmarks.parts()])

#     # Loop through each target image
#     for i, target_path in enumerate(target_paths):
#         # Read the target image
#         target_img = cv2.imread(target_path)

#         # Convert the target image to grayscale
#         target_gray = cv2.cvtColor(target_img, cv2.COLOR_BGR2GRAY)

#         # Detect faces in the target image
#         target_faces = detector(target_gray)

#         # If no face is detected in the target image, skip to the next target
#         if len(target_faces) == 0:
#             print(f"No face detected in the target image {target_path}.")
#             continue

#         # Get the landmarks of the first face detected in the target image
#         target_face = target_faces[0]
#         target_landmarks = predictor(target_gray, target_face)
#         target_points = np.array([[p.x, p.y] for p in target_landmarks.parts()])

#         # Calculate the convex hull of the target face
#         target_convexhull = cv2.convexHull(target_points)

#         # Create a mask for the target face
#         target_mask = np.zeros_like(target_gray)
#         cv2.fillConvexPoly(target_mask, target_convexhull, 255)

#         # Create images of the source and target faces
#         source_face_img = cv2.bitwise_and(source_img, source_img, mask=target_mask)
#         target_face_img = cv2.bitwise_and(target_img, target_img, mask=cv2.bitwise_not(target_mask))

#         # Combine the source and target faces
#         result_img = cv2.add(source_face_img, target_face_img)

#         # Find the center of the target face
#         target_rect = cv2.boundingRect(target_convexhull)
#         center = (target_rect[0] + target_rect[2] // 2, target_rect[1] + target_rect[3] // 2)

#         # Perform seamless cloning to blend the source and target faces
#         seamless_clone = cv2.seamlessClone(result_img, target_img, target_mask, center, cv2.NORMAL_CLONE)

#         # Save the swapped face image
#         output_path = output_paths[i]
#         cv2.imwrite(output_path, seamless_clone)
#         print(f"Saved swapped face image to {output_path}")

#     print("Face swap process completed.")

# # 예시 사용
# if __name__ == "__main__":
#     # 소스 이미지 경로
#     source_path = "uploads/20240528_203032.jpg"
#     # 대상 이미지 경로
#     target_paths = ["static/predefined/image1.jpg", "static/predefined/image3.jpg"]
#     # 결과 이미지 저장 경로
#     output_paths = ["result1.jpg", "result2.jpg"]
#     # 얼굴 교체 함수 호출
#     face_swap(source_path, target_paths, output_paths)
