# Hadoop_tutorial
* Enviroment : docker, hadoop version 2.6.1

## Hadoop Install
* Create docker images
* apt-get install software-properties-common
* add-apt-repository ppa:webupd8team/java
* apt-get update
* wget http://mirror.apache-kr.org/hadoop/common/hadoop-2.6.1/hadoop-2.6.1.tar.gz

##  My dockerhub

* My hadoop dockerhub (tkd1496)
  * Pull the images : docker pull tkd1496/ubuntu:hadoop
  * docker run -i -t -h (hostname) --name (name) -p (web port)50070 tkd1496/ubuntu:hadoop
  * My experiments was consist of master, 2 slave and so on
 
## Hadoop commands
 
* hadoop file system commands
    * hadoop fs -ls / 
    * hadoop fs -put (local file) (hadoop file system)

* Create a Class
    * hadoop com.sun.tools.javac.Main (Java File Name)
   
* Create a jar file
    * jar cf (Jar file name) (Class File name)

* Hadoop execute commands
    * hadoop jar (Jar file name) (Class File Name) (input) (output)
   
* ex) If you want to skip patterns when wordcount is executed, 
    * hadoop fs -put patterns.txt  /
    * hadoop jar (jar file) (Wordcount class file) -Dwordcount.case.sensitive=true (input) (output) -skip /patterns.txt
