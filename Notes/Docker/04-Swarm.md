# Docker - Swarm

#### What is next step ?

Deploy your application onto a cluster, running it on multiple machines. *Multi-container, multi-machine applications are made possible by joining multiple machines into a **Dockerized** cluster call **SWARM***



#### Swarm Clusters 

> A swarm is a group of machines that are running Docker and joined into a cluster.

Once swarm cluster is ready, one can use docker commands as it is. The commands will now be executed on **Cluster** by a **Swarm Manager**. The machine can be physical or virtual. Each machine in a swarm is referred to as **nodes**.

The task distribution strategies can be specified by user in compose file.

> e.g. "Emptiest node", "Global"

**Swarm managers are the only machines in  a swarm that can execute commands.**  It also authorizes other machines to join the swarm as **worker**.

> Up until now, you have been using Docker in a single-host mode on your local machine. But Docker also can be switched into **swarm mode**, and that’s what enables the use of swarms. Enabling swarm mode instantly makes the current machine a swarm manager. From then on, Docker runs the commands you execute on the swarm you’re managing, rather than just on the current machine. 



#### Setting up your swarm

##### Swarm manager

```bash
~ # hostname -i                                                                                                root@in-ibmibm3287
10.53.16.54
------------------------------------------------------------
~ # docker swarm init --advertise-addr 10.53.16.54                                                             root@in-ibmibm3287
Swarm initialized: current node (77dgwsdz7dctkfrpv0jbg6ryd) is now a manager.

To add a worker to this swarm, run the following command:

    docker swarm join --token SWMTKN-1-2g8qxgpe38598c26o993ewix7z5k9w5vj3a1u3vcgw2bd8jrk4-1olnf1egnsud97du2mw50xxzc 10.53.16.54:2377

To add a manager to this swarm, run 'docker swarm join-token manager' and follow the instructions.

------------------------------------------------------------
```



##### My Machine

````bash
pskanade@ptl2275 ~
  % docker swarm join --token SWMTKN-1-2g8qxgpe38598c26o993ewix7z5k9w5vj3a1u3vcgw2bd8jrk4-1olnf1egnsud97du2mw50xxzc 10.53.16.54:2377
This node joined a swarm as a worker.
````



##### More Results

```bash
------------------------------------------------------------
~ # docker node ls                                                                                             root@in-ibmibm3287
ID                            HOSTNAME                STATUS              AVAILABILITY        MANAGER STATUS      ENGINE VERSION
77dgwsdz7dctkfrpv0jbg6ryd *   in-ibmibm3287           Ready               Active              Leader              18.06.1-ce
ioyl9cls74oiez7sfzlx5r6er     linuxkit-025000000001   Ready               Active                                  18.06.0-ce
------------------------------------------------------------
```



##### Present replicated containers - 

```bash
------------------------------------------------------------
~/projects/doc_app # docker stack ps getstartedlab                                                             root@in-ibmibm3287
ID                  NAME                      IMAGE                        NODE                    DESIRED STATE       CURRENT STATE            ERROR                              PORTS
9lm1xzbr2f0q        getstartedlab_web.1       pskanade/get-started:part2   in-ibmibm3287           Running             Running 2 minutes ago                                       
mtlgo7h03qc1         \_ getstartedlab_web.1   pskanade/get-started:part2   linuxkit-025000000001   Shutdown            Rejected 3 minutes ago   "No such image: pskanade/get-s…"   
srs6nx2gworl         \_ getstartedlab_web.1   pskanade/get-started:part2   linuxkit-025000000001   Shutdown            Rejected 3 minutes ago   "No such image: pskanade/get-s…"   
3y7x5elcirob        getstartedlab_web.2       pskanade/get-started:part2   in-ibmibm3287           Running             Running 3 minutes ago                                       
f0xhrn2pvzqi         \_ getstartedlab_web.2   pskanade/get-started:part2   linuxkit-025000000001   Shutdown            Rejected 3 minutes ago   "No such image: pskanade/get-s…"   
i5s8thgpng70        getstartedlab_web.3       pskanade/get-started:part2   in-ibmibm3287           Running             Running 3 minutes ago                                       
c8513kzhdgca        getstartedlab_web.4       pskanade/get-started:part2   in-ibmibm3287           Running             Running 2 minutes ago                                       
31q40hye4guz         \_ getstartedlab_web.4   pskanade/get-started:part2   linuxkit-025000000001   Shutdown            Rejected 3 minutes ago   "No such image: pskanade/get-s…"   
y78hqlgev4kb         \_ getstartedlab_web.4   pskanade/get-started:part2   linuxkit-025000000001   Shutdown            Rejected 3 minutes ago   "No such image: pskanade/get-s…"   
zltnbkrrplpb        getstartedlab_web.5       pskanade/get-started:part2   in-ibmibm3287           Running             Running 3 minutes ago                                       
------------------------------------------------------------
```



##### Final action - 

1. Take down the stack 
2. Leave the swarm

##### Summary

> In part 4 you learned what a swarm is, how nodes in swarms can be managers or workers, created a swarm, and deployed an application on it. You saw that the core Docker commands didn’t change from part 3, they just had to be targeted to run on a swarm master. You also saw the power of Docker’s networking in action, which kept load-balancing requests across containers, even though they were running on different machines. Finally, you learned how to iterate and scale your app on a cluster.
>
> Here are some commands you might like to run to interact with your swarm and your VMs a bit:



##### Commands

```bash
docker-machine create --driver virtualbox myvm1 # Create a VM (Mac, Win7, Linux)
docker-machine create -d hyperv --hyperv-virtual-switch "myswitch" myvm1 # Win10
docker-machine env myvm1                # View basic information about your node
docker-machine ssh myvm1 "docker node ls"         # List the nodes in your swarm
docker-machine ssh myvm1 "docker node inspect <node ID>"        # Inspect a node
docker-machine ssh myvm1 "docker swarm join-token -q worker"   # View join token
docker-machine ssh myvm1   # Open an SSH session with the VM; type "exit" to end
docker node ls                # View nodes in swarm (while logged on to manager)
docker-machine ssh myvm2 "docker swarm leave"  # Make the worker leave the swarm
docker-machine ssh myvm1 "docker swarm leave -f" # Make master leave, kill swarm
docker-machine ls # list VMs, asterisk shows which VM this shell is talking to
docker-machine start myvm1            # Start a VM that is currently not running
docker-machine env myvm1      # show environment variables and command for myvm1
eval $(docker-machine env myvm1)         # Mac command to connect shell to myvm1
& "C:\Program Files\Docker\Docker\Resources\bin\docker-machine.exe" env myvm1 | Invoke-Expression   # Windows command to connect shell to myvm1
docker stack deploy -c <file> <app>  # Deploy an app; command shell must be set to talk to manager (myvm1), uses local Compose file
docker-machine scp docker-compose.yml myvm1:~ # Copy file to node's home dir (only required if you use ssh to connect to manager and deploy the app)
docker-machine ssh myvm1 "docker stack deploy -c <file> <app>"   # Deploy an app using ssh (you must have first copied the Compose file to myvm1)
eval $(docker-machine env -u)     # Disconnect shell from VMs, use native docker
docker-machine stop $(docker-machine ls -q)               # Stop all running VMs
docker-machine rm $(docker-machine ls -q) # Delete all VMs and their disk images
```

