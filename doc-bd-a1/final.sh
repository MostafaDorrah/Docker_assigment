#!/bin/bash

mkdir -p "${/home/doc-bd-a1}"

txt="/home/doc-bd-a1>/k.txt"
img="</home/doc-bd-a1>/vis.png"
csv="</home/doc-bd-a1>/res_dpre.csv"

docker cp "${fervent_chatelet}:${txt}" "${bd-a1/service-result/}/k.txt"
docker cp "${fervent_chatelet}:${img}" "${bd-a1/service-result/}/vis.png"
docker cp "${fervent_chatelet}:${csv}" "${bd-a1/service-result/}/res_dpre.csv"

docker stop "${fervent_chatelet}"

echo "Done."