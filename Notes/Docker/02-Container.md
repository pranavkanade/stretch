# Docker - Container

**Question : ** What is needed for python application ... ?

All of that can be made portable !!

> With Docker, you can just grab a portable Python runtime as an image, no installation necessary. Then, your build can include the base Python image right alongside your app code, ensuring that your app, its dependencies, and the runtime, all travel together. 

Docker provides the mechanism to do so with something called - `Dockerfile`. It is used to define the container image.

### How ?

> `Dockerfile` defines what goes on in the environment inside your container. Access to resources like networking interfaces and disk drives is virtualized inside this environment, which is isolated from the rest of your system, so you need to map ports to the outside world, and be specific about what files you want to “copy in” to that environment. However, after doing that, you can expect that the build of your app defined in this `Dockerfile` behaves exactly the same wherever it runs. 

##### Step - 1

* Create an empty directory.
* Create new file - `Dockerfile`
* Copy following contents to that file -

```dockerfile
# Use an official Python runtime as a parent image
FROM python:3.5-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]
```

* There are more files  - `app.py` and `requirements.txt`

##### Step - 2   - The app itself

>  When the above `Dockerfile` is built into an image, `app.py` and`requirements.txt` is present because of that `Dockerfile`’s `ADD` command, and the output from `app.py` is accessible over HTTP thanks to the `EXPOSE` command. 

`requirements.txt`

```text
Flask
Redis
```

`app.py`

```python
from flask import Flask
from redis import Redis, RedisError
import os
import socket

# Connect to Redis
redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__)

@app.route("/")
def hello():
    try:
        visits = redis.incr("counter")
    except RedisError:
        visits = "<i>cannot connect to Redis, counter disabled</i>"

    html = "<h3>Hello {name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>" \
           "<b>Visits:</b> {visits}"
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname(), visits=visits)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
```

##### Step - 3 - Build the app

```bash
docker build -t friendlyhello .
docker image ls
```

##### Step - 4: Run the app

Run the app, mapping your machine's port 4000 to the container's published port 80 using `-p`.

```bash
docker run -p 4000:80 friendlyhello
```

> Visit http://localhost:4000

###### Alternate

```bash
# Run the application in detached mode
docker run -d -p 4000:80 friendlyhello
docker ps
docker container stop d179caf89728
```



#### Share your image

To display the portability of the docker, let's upload our built image and run it somewhere else.

1. Signup - https://hub.docker.com

2. ```bash
   docker login
   ```

3. Tag the image - tagging is used to provide different versions of the images.

   ```bash
   # Command to tag
   docker tag image username/repository:tag_name
   
   docker tag friendlyhello pskanade/get-started:part2
   
   # this created a new image with tag
   docker image ls
   ```

4. Publish the image

   ```bash
   docker push username/repository:tag
   
   # my command
   docker push pskanade/get-started:part2
   ```

5. Pull and run the image

   ```bash
   docker run -p 4000:80 pskanade/get-started:part2
   ```



### Commands

```bash
docker build -t friendlyhello .  # Create image using this directory's Dockerfile
docker run -p 4000:80 friendlyhello  # Run "friendlyname" mapping port 4000 to 80
docker run -d -p 4000:80 friendlyhello         # Same thing, but in detached mode
docker container ls                                # List all running containers
docker container ls -a             # List all containers, even those not running
docker container stop <hash>           # Gracefully stop the specified container
docker container kill <hash>         # Force shutdown of the specified container
docker container rm <hash>        # Remove specified container from this machine
docker container rm $(docker container ls -a -q)         # Remove all containers
docker image ls -a                             # List all images on this machine
docker image rm <image id>            # Remove specified image from this machine
docker image rm $(docker image ls -a -q)   # Remove all images from this machine
docker login             # Log in this CLI session using your Docker credentials
docker tag <image> username/repository:tag  # Tag <image> for upload to registry
docker push username/repository:tag            # Upload tagged image to registry
docker run username/repository:tag                   # Run image from a registry
```

