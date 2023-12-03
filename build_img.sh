#! /bin/bash

echo "\n*************** Building the Image 1 **************ok*\n"

docker build -t krishgopal37/image_1 ./target_1/

echo "\n*************** Building the Image 2 ***************\n"

docker build -t krishgopal37/image_2 ./target_2/

echo "\n*************** Done *********************\n"

docker images | awk 'NR>1  {print $1}' > docker_img_list.txt
