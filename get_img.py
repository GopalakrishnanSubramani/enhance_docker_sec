img_name =  "docker_img_list.txt"
docker_images = {}

with open(f"{img_name}",'r') as f:
    line = f.readlines()
    for index,l in enumerate(line):
        docker_images.update({f"image_{index}":l.strip()})
