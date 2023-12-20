import cv2

# Load image
image = cv2.imread('image.jpg')

# Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Perform Canny edge detection
edges = cv2.Canny(blur, 50, 150)

# Show original and edge-detected images
cv2.imshow('Original Image', image)
cv2.imshow('Edge Detected Image', edges)

# Wait for a key press and then exit
cv2.waitKey(0)
cv2.destroyAllWindows()
