import requests 
import time
t1=time.perf_counter()

image=requests.get(url="https://images.unsplash.com/photo-1516117172878-fd2c41f4a759?w=1920&h=1080&fit=crop", stream=True)

### even when using the stream we can get the content of the image downloaded directly 
### so whe we is response.content we can say that the use of the stream is useless 
with open("myimage.png", "wb") as f :
     f.write(image.content)

t2=time.perf_counter()

print(f" the time nedded to finish the download is {t2-t1}")

### the output shows that we can download the image with .content even if  the  stream parameter is set to true 


t3=time.perf_counter()
with open("myimage.png", "wb") as f:
    
        for chunk in image.iter_content(chunk_size=8192):
            # Using iter_content() with stream=True downloads the file in small chunks
            # instead of loading the entire image into memory at once.
            # Each chunk is written to disk immediately, which prevents high memory usage
            # and is safer for downloading very large files.
            f.write(chunk)

        print(f"Downloaded and saved to: {"myimage.png"}")
t4=time.perf_counter()

print(f"the code finishes in {t4-t3} when we use the iter_content")
