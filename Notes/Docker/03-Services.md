# Docker - Services

In distributed application, different pieces of the application are called **"services"**.

> If you imagine a video sharing site, it probably includes a service for storing application data in a database. A service for video transcoding in the background after a user uploads something, a service for the front-end and so on ..

Services are really just "*containers in production*". A service only runs one image, but it defines the way that image runs - what ports it should use, how many replicas of the container should run.. etc.

**Scaling a service** changes **the number of container instances running** that piece of software, assigning more computing resources to the service in the process. 

To define, run and scale we write `docker-compose.yml`

### Writing `docker-compose.yml` -

```yaml
version: "3"
services:
  web:
    # replace username/repo:tag with your name and image details
    image: pskanade/get-started:part2
    deploy:
      replicas: 5
      resources:
        limits:
          cpus: "0.1"
          memory: 50M
      restart_policy:
        condition: on-failure
    ports:
      - "4000:80"
    networks:
      - webnet
networks:
  webnet:
```

Above file tells the Docker to do the following :

1. Pull the image uploaded in step 2 from the registry.
2. Run 5 instances of that image as a service call `web`, limiting each one to use, at most 10% of the CPU and 50 MB of RAM.
3. immediately restart containers if one fails.
4. Map port 4000 on the host to web's port 80.
5. Define the `webnet` network with the default settings ( which is a load-balanced overlay network )



#### Run : new load-balanced application

1. Just run for time being - if you don't run this, then you'll get `this is not a swarm manager`

   ```bash
   docker swarm init
   ```

   **Results on my machine**

   ```bash
   root@in-ibmibm3287:~/projects/doc_app# docker swarm init
   Swarm initialized: current node (nsmo9khx69ikkj2x6vbpezxjv) is now a manager.
   
   To add a worker to this swarm, run the following command:
   
       docker swarm join --token SWMTKN-1-3yxrrynl4d9k2d56sg45g1rg8um4oq1whkh8s1z9tc8rud1lp0-dgvv12sxsw3bbcid0qee25k7p 10.53.16.54:2377
   
   To add a manager to this swarm, run 'docker swarm join-token manager' and follow the instructions.
   ```

2. Now we are ready to run our service. You need to give your application a name. 

   ```bash
   docker stack deploy -c docker-compose.yml <application_name>
   ```

   **Results on my machine**

    ```bash
   root@in-ibmibm3287:~/projects/doc_app# docker stack deploy -c docker-compose.yml getstartedlab
   Creating network getstartedlab_webnet
   Creating service getstartedlab_web
   
   root@in-ibmibm3287:~/projects/doc_app# docker service ls
   ID                  NAME                MODE                REPLICAS            IMAGE                        PORTS
   xaw48gk83vh8        getstartedlab_web   replicated          5/5                 pskanade/get-started:part2   *:4000->80/tcp
   
   root@in-ibmibm3287:~/projects/doc_app# docker ps
   CONTAINER ID        IMAGE                        COMMAND             CREATED             STATUS              PORTS               NAMES
   3fdc7811fbba        pskanade/get-started:part2   "python app.py"     10 seconds ago      Up 7 seconds        80/tcp              getstartedlab_web.3.jyibpb8nn6udji663pgm03ofs
   2cb29394e92c        pskanade/get-started:part2   "python app.py"     10 seconds ago      Up 8 seconds        80/tcp              getstartedlab_web.1.n22iia7odkma2y1vp60r0qov2
   e908b85b8a0d        pskanade/get-started:part2   "python app.py"     10 seconds ago      Up 7 seconds        80/tcp              getstartedlab_web.2.yz5znn88odjzr0xaydnhocsvi
   3674b741eb56        pskanade/get-started:part2   "python app.py"     11 seconds ago      Up 6 seconds        80/tcp              getstartedlab_web.5.wystt3hgictm8w80xv3imm9n9
   117417aaf645        pskanade/get-started:part2   "python app.py"     11 seconds ago      Up 7 seconds        80/tcp              getstartedlab_web.4.7qnb4f2w1wmy5legzbmy6b2jf
   
   root@in-ibmibm3287:~/projects/doc_app# docker service ps getstartedlab_web
   ID                  NAME                  IMAGE                        NODE                DESIRED STATE       CURRENT STATE           ERROR               PORTS
   n22iia7odkma        getstartedlab_web.1   pskanade/get-started:part2   in-ibmibm3287       Running             Running 5 minutes ago
   yz5znn88odjz        getstartedlab_web.2   pskanade/get-started:part2   in-ibmibm3287       Running             Running 5 minutes ago
   jyibpb8nn6ud        getstartedlab_web.3   pskanade/get-started:part2   in-ibmibm3287       Running             Running 5 minutes ago
   7qnb4f2w1wmy        getstartedlab_web.4   pskanade/get-started:part2   in-ibmibm3287       Running             Running 5 minutes ago
   wystt3hgictm        getstartedlab_web.5   pskanade/get-started:part2   in-ibmibm3287       Running             Running 5 minutes ago
   
    ```

   A single container running in a service is called a **task**. Each task has unique ID.

   > If we hit http://10.53.16.54:4000/ URL several times the Hostname will keep changing in round robin fashion - TA...DA .. ! Load balancing .. !



##### Scale the application

We can scale the application by changing the `replicas` value in `docker-compose.yml` saving the change, and re-running the `docker stack deploy` command.



#### Take down the app and the swarm

* Take down the app

  ```bash
  docker stack rm getstartedlab
  
  # my machine
  root@in-ibmibm3287:~/projects/doc_app# docker stack rm getstartedlab
  Removing service getstartedlab_web
  Removing network getstartedlab_webnet
  ```

* Take down the swarm

  ```bash
  docker swarm leave --force
  
  # my machine
  root@in-ibmibm3287:~/projects/doc_app# docker swarm leave --force
  Node left the swarm.
  ```



### Commands

```bash
docker stack ls                                            # List stacks or apps
docker stack deploy -c <composefile> <appname>  # Run the specified Compose file
docker service ls                 # List running services associated with an app
docker service ps <service>                  # List tasks associated with an app
docker inspect <task or container>                   # Inspect task or container
docker container ls -q                                      # List container IDs
docker stack rm <appname>                             # Tear down an application
docker swarm leave --force      # Take down a single node swarm from the manager
```



### Summary 

> To recap, while typing `docker run` is simple enough, the true implementation of a container in production is running it as a service. Services codify a container’s behavior in a Compose file, and this file can be used to scale, limit, and redeploy our app. Changes to the service can be applied in place, as it runs, using the same command that launched the service: `docker stack deploy`. 

