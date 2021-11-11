This repo uses Docker

**Build**

docker build -t storyTell_Image .

**Run**

docker run -d --name container -p 8080:8080 storyTell_Image

**Served Swagger**

http://localhost:8080/docs
