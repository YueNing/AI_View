#!/bin/bash
# author: naodongbanana
# url:www.github.com/YueNing

# setting the variables
source_url=$1
source_name='sources.zip'
#mysql_root_password=$2
mysql_user_name='mk_user'
mysql_password='test123'
source_dir='my_video_scenes_tmp'

# get the source file id
IFS=? read -a full_id <<< $source_url
id=${full_id[1]:3}


# ini
init(){
	echo 'source ./medienkunst_python3.6_virtualenv/bin/activate' > start.sh
	echo 'cd mk && python3 manage.py runserver' >> start.sh && chmod +x start.sh
} 

# download the system tools
download_system_tools() {
	wget -O gdrive https://docs.google.com/uc?id=0B3X9GlR6EmbnQ0FtZmJJUXEyRTA&export=download &
	wait
	chmod +x ./gdrive &
	sudo apt install python3 virtualenv ffmpeg git subversion
	sudo apt install mysql-server mysql-client
	wait
}
# get the ai system source code
get_source_code() {
	svn export https://github.com/YueNing/AI_View.git/trunk/mk 
	svn export https://github.com/YueNing/AI_View.git/trunk/pre_data
}

#get_source_code
download_source_file() {
	mkdir my_video_scenes_tmp &
	./gdrive download $id  
	wait
	unzip $source_name -d $source_dir && rm $source_name
	wait
	mv my_video_scenes_tmp/data_ai_view.xlsx pre_data
}

#python3 virtualenv
python3_virtualenv() {
	mkdir medienkunst_python3.6_virtualenv && virtualenv --no-site-packages -p /usr/bin/python3.6 medienkunst_python3.6_virtualenv 
	wait
	source ./medienkunst_python3.6_virtualenv/bin/activate
	wait
	pip3 install -r mk/requirements.txt
}

# setting mysql create new user and new database
mysql_setting() {
	MYSQL=`which mysql`
	sudo $MYSQL mk -uroot<< EOF
	GRANT ALL PRIVILEGES ON *.* TO 'mk_user'@'localhost' IDENTIFIED BY 'test123';
	CREATE DATABASE mk;
	FLUSH PRIVILEGES;
EOF
}

substuation_mk_setting() {
	cd mk/static &&
	sed -i '/STATICFILES_DIRS/c\STATICFILES_DIRS = ('"'"$(pwd)"'"',)' ../mk/settings.py &&
	cd ../../
}

django_setting() {
	substuation_mk_setting
	wait
	cd mk && python3 manage.py createsuperuser && python3 manage.py makemigrations && python3 manage.py migrate
	wait
	cd ../pre_data && python3 ./save.py
	wait
	cd ../ && ./start.sh
}

init
download_system_tools
get_source_code
python3_virtualenv
download_source_file
mysql_setting
django_setting

