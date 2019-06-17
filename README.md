# DjangoAppTest

Practicing my Django web application skills here.

An app to organize project information with a quest theme.

The idea is to include the most pertinent information that would be relevant for including in a portfolio for potential employers or clients interested in getting a snapshot view of the project process. The concept would include a general list view of all projects (aka Quests), and a detailed view of each project. There should also ideally be a Plugger form where visitors can input their own project data to be added into the database, and they can see their project formatted as a quest.

# How to run Program

### Install the virtualenv package
Install the virtualenv package to create and activate a virtual environment
```
pip install virtualenv
```

### Create virtual environment
```
virtualenv venv
```

### Activate the virtual environment

Mac OS / Linux
```
source venv/bin/activate
```

Windows
```
source venv/source/activate

--- or ---

venv\Scripts\activate
```

### Get necessary files to run the program in the virtual environment

pip has the option to install everything needed to run the program with requirements.txt
```
pip install -r requirements.txt
```


### Deactive the virtual environment
```
deactivate
```

### To run the server 

```
python manage.py runserver 8001
```

# Installs
1. django-multiselectfield

## django-multiselectfield
```
pip install django-multiselectfield
```

# Notes

### Requirements.txt

Make sure if there are any installs, plugins, or libraries added to add to the requirements.txt. This cab be done with the following command:
```
pip freeze > requirements.txt
```

### Cleaning the Database

1. Delete db.sqlite3 file
```
rm db.sqlite3
```
2. Migrate the models
```
python manage.py makemigrations quests
```

Results and Warning messages like the following is known and is fine
```
System check identified some issues:
WARNINGS:quests.QuestResult.questpin: (fields.W342) Setting unique=True on a ForeignKey has the same effect as using a OneToOneField.
        HINT: ForeignKey(unique=True) is usually better served by a OneToOneField.
Migrations for 'quests':
  quests\migrations\0002_auto_20190617_0057.py
    - Alter field questpin on questresult
```

3. Perform a sqlmigrate with the number issued after performing makemigrations
```
python manage.py sqlmigrate quests 0001
```
Results should look like the following:
```
WARNINGS:
quests.QuestResult.questpin: (fields.W342) Setting unique=True on a ForeignKey has the same effect as using a OneToOneField.
        HINT: ForeignKey(unique=True) is usually better served by a OneToOneField.
BEGIN;
--
-- Alter field questpin on questresult
--
CREATE TABLE "new__quests_questresult" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "questpin_id" integer NOT NULL UNIQUE REFERENCES "quests_questpin" ("id") DEFERRABLE INITIALLY DEFERRED, "deliverables" varchar(122) NOT NULL);
INSERT INTO "new__quests_questresult" ("id", "deliverables", "questpin_id") SELECT "id", "deliverables", "questpin_id" FROM "quests_questresult";
DROP TABLE "quests_questresult";
ALTER TABLE "new__quests_questresult" RENAME TO "quests_questresult";
COMMIT;
```

4. Perform the final migration check
```
python manage.py migrate
```

Results should look like the following:
```
System check identified some issues:s:

WARNINGS:                         ds.W342) Setting unique=True on a ForeignKey has tquests.QuestResult.questpin: (fielField.ds.W342) Setting unique=True on a ue) is usually better served by a OneToOneField.
ForeignKey has the same effect as
using a OneToOneField.            h, contenttypes, quests, sessions
        HINT: ForeignKey(unique=True) is usually better served by a OneToOneField.Operations to perform:
  Apply all migrations: admin, auth, contenttypes, quests, sessions
Running migrations:
  Applying quests.0002_auto_20190617_0057... OK(mypython)
```

