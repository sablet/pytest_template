#!/bin/bash

ori_name=python_template
cd ..
mv $ori_name $1
cd $1
virtualenv -p /usr/bin/python3 virenv_for_$1
cat setup.py|sed "s/$ori_name/$1/g" > setup.py

# data get
cd tests/data
data_url="http://www.post.japanpost.jp/zipcode/dl/roman/ken_all_rome.zip"
fname=$(basename $data_url)
wget $data_url
unzip $fname
rm $fname