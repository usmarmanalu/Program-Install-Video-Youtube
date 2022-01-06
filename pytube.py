from pytube import YouTube

link = input("URL Youtube : ")
yt = YouTube(link)

videos = yt.streams.all()
video = list(enumerate(videos))
for i in video:
    print(i)
    
    
print(" ")
print("pengaturan durasi dan layout video : ")
dnoption = int(input("masukkan pengaturan : "))
dnvideo = videos[dnoption]
dnvideo.download()


print("dwonload sukses")
