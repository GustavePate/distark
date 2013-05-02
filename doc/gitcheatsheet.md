
************************************************************************
#####    VIRTUAL ENV      
************************************************************************
```shell
sudo apt-get install python-virtualenv
cd ~
mkdir eclipsevirtualenv
virtualenv eclipsevirtualenv/ref_env
source eclipsevirtualenv/ref_env/bin/activate

#here we are

pip install yolk
yolk -l
pip install pymongo
yolk -l

#YEAH !!!
```
sudo apt-get install python-dev build-essential python-tk tk-dev libpng12-dev g++
pip install matplotlib libjpeg8 libjpeg-dev libfreetype6 libfreetype6-dev zlib1g-dev

pip install numpy
pip install python-dateutil
pip install reportlab

pip install argparse
pip install pyyaml
pip install matplotlib


si les liens n'existent pas (attention la destination doit etre en .so dans /usr/lib)
sudo ln -s /usr/lib/x86_64-linux-gnu/libjpeg.so /usr/lib/libjpeg.so 
sudo ln -s /usr/lib/x86_64-linux-gnu/libfreetype.so.6 /usr/lib/libfreetype.so
sudo ln -s /usr/lib/x86_64-linux-gnu/libz.so /usr/lib/libz.so

pip install pil

pip install MySQL-python

eclipse->project->properties->new interpreter 


************************************************************************
#####    LANCER EN LIGNE DE COMMANDE
************************************************************************
export PYTHONPATH=/home/guillaume/git/sandbox/src:



************************************************************************
#####     CASSANDRA
************************************************************************
pip install cql
pip install pycassa

 
sudo apt-get install cassandra
cassandra-cli
connect localhost/9160;
CREATE KEYSPACE CassandraTest with placement_strategy = 'org.apache.cassandra.locator.SimpleStrategy'and strategy_options = {replication_factor:1};
use CassandraTest;
CREATE COLUMN FAMILY users	WITH comparator = UTF8Type;
CREATE COLUMN FAMILY test	WITH comparator = IntegerType;

drop KEYSPACE CassandraTest;

http://www.datastax.com/docs/1.1/dml/using_cli
http://code.google.com/a/apache-extras.org/p/cassandra-dbapi2/
https://pycon-2012-notes.readthedocs.org/en/latest/apache_cassandra_and_python.html

operation | cassandra | mysql | mongo
connect | 0.003420 | 0.026010  | 0.001964
create | NA | 0.072727 | 0.218418
read | 0.005036 | 0.051459 | 0.037322
write | 0.000358 | 0.000111 | 0.000241
delete | NA | 0.000014 | 0.000020
drop | NA | 0.025190 | 0.002656


************************************************************************
#####     MONGODB
************************************************************************
sudo pip install pymongo

************************************************************************
#####     MYSQL
************************************************************************
apt-get install python-dev libmysqlclient-dev
pip install MySQL-python

mysql -u root -p

show databases;
use test;
create user "test"@"localhost";
SET password FOR "test"@"localhost" = password('test');
GRANT ALL ON test.* TO "test"@"localhost";
create table testtables(num int,text varchar(30),date long);

************************************************************************
#####     GIT
************************************************************************
```shell
git config --list

git config --global user.name "John Doe"

git clone git://github.com/schacon/grit.git

git clone https://github.com/GustavePate/sandbox.git

git status

git add README

cat .gitignore

# diff not staged <-> staged
git diff


#diff staged <-> last commit ==  next commit
git diff --staged

#committing staged diff
git commit -m "my commit comment"

#commit also not staged files
git commit -a -m "my commit comment"

#supprimer un fichier staged
git rm --cached readme.txt

#deplacer un fichier
git mv test.py hello.py

#listing des commits
git log

#listing des commits avec diff
git log -p


#listing des 2 derniers commits avec diff
git log -p -2

#volume des commitsq
git log --stat

#tout sur une ligne
git log --pretty=oneline
git log --pretty=format:"%h - %an, %ar : %s"

#listing des serveurs
git remote -v

#Tout pousser sur le serveur
git push origin master
```


