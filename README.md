# TODO list
> This site is designed to help the monitoring of tasks.

This project models a comprehensive system to manage and modify the rask and tags.

### Initial Configuration

To perform the check of functionality you don't need the credentials.


## Developing

Ensure you have Python and Django installed on your system.

```shell
git clone https://github.com/Vasavik-ua/Todo-List.git
cd TODO list/
pip install -r requirements.txt
```


### Building

If you make any migrations or changes to models, run:

```shell
python manage.py makemigrations
python manage.py migrate
```

## Features

Task:
* Represents the job you need to perform.
* Fields: Includes attributes like content, datetime, deadline, progress and tag.
* Relation:
  * Many to many field tag wit Tag features. 
InfoCar:
* Represent where you need to do the task.
* Fields: name of place.


#### Settings
* Add your 'DATABASES' configuration in settings.py to connect to your preferred database.

## Links

- Project homepage: https://github.com/Vasavik-ua/Todo-List.git
- Repository: https://github.com/Vasavik-ua?tab=repositories

