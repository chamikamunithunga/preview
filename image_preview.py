import cv2
import os

def preview_image(image_path):
    # Check if the file exists
    if not os.path.exists(image_path):
        print(f"Error: The file {image_path} does not exist.")
        return




    

    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Unable to load the image. Please ensure it is a valid image file.")
        return

    # Display the image in a window
    cv2.imshow("Image Preview", image)

    # Wait for a key press to close the window
    print("Press any key in the preview window to close.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Prompt user for the image file path
    image_path = input("Enter the path to your image file: ")
    preview_image(image_path)
