# BD Devs Club Website

### Setup Instructions

#### One time setups

* Install Python 3 - I recommend using pyenv. 

		pyenv install 3.4.3

* This step is optional. You can ignore this one. However, it is a good practice to use a virtualenv. I use virtualenv wrapper to manage virtual environments. 

```
	pip install virtualenv
	pip install virtualenvwrapper
	mkvirtualenv bddevs
	workon bddevs
```
Ubuntu
```
	apt-get install python3-pip
	pip3 install virtualenv
	pip3 install virtualenvwrapper
	export WORKON_HOME=~/Envs
	mkdir -p $WORKON_HOME
	source /usr/local/bin/virtualenvwrapper.sh
	mkvirtualenv bddevs
	workon bddevs
```
Please consult virtualenv docs for more information. 

* Clone the git repo and `cd` into it. 

* Install the project dependencies using pip. 
		
		pip install -r requirements.txt
	
* Update database settings. Open `bddevs/settings.py` file and update the `DATABASES` section. It looks like this: 

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bddevs',
        'USER': 'root',
        'PASSWORD': 'masnun',
        'HOST': '127.0.0.1',
    }
}
```

* Run migrations

		python manage.py migrate

* Load fixtures/initial data

		python manage.py loaddata webinar.json

* Create an admin user

		python manage.py createsuperuser



#### Running Local Server

Now you're ready to launch the local server. Run this command: 

		python manage.py runserver 

You should be able to view the website at: 

<a href="http://localhost:8000/">http://localhost:8000/</a>

And access the admin at: 

<a href="http://localhost:8000/admin/">http://localhost:8000/admin/</a>



