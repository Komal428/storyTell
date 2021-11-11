This repo uses Docker

**Build**

docker build -t storyTell_Image .

**Run**

docker run -d --name container -p 8080:8080 storyTell_Image

**Served Swagger**

http://localhost:8080/docs


**Pyhton files**

messge.py file has 2 end points

1. For creating messge and getting url to the message

2. For getting message if client has messge id

Run test.py to check the correctness of  sloution

