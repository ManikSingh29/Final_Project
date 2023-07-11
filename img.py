from simple_image_download import simple_image_download as sid
response = sid.simple_image_download
keyword = ["satellite images of buildings"]
for i in keyword:
    response().download(i,50)