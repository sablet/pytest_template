#!/bin/bash

ori_name=$(basename $(pwd))
cd ..
mv $ori_name $1
cd $1
virtualenv -p /usr/bin/python3 virenv_for_$1
cp setup.py setup_temp.py
sed "s/$ori_name/$1/g" setup_temp.py > setup.py
rm setup_temp.py

# data get

# cd tests/data
# data_url="http://www.post.japanpost.jp/zipcode/dl/roman/ken_all_rome.zip"
# fname=$(basename $data_url)
# wget $data_url
# unzip $fname
# rm $fname
