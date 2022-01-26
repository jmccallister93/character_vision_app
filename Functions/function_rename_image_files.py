import os
 
# Function to rename multiple files
def main():
   
    folder = "C:/Users/Jared/Downloads/ImageAssistant_Batch_Image_Downloader/Renamed"
    for count, filename in enumerate(os.listdir(folder)):
        dst = f"character22 {str(count)}.jpg"
        src =f"{folder}/{filename}"  # foldername/filename, if .py file is outside folder
        dst =f"{folder}/{dst}"
         
        # rename() function will
        # rename all the files
        os.rename(src, dst)
 
# Driver Code
if __name__ == '__main__':
     
    main()
