# Docker - Concept

> The use of Linux containers to deploy applications is called **containerization**.
>
> Docker is a platform for developers and sys-administrators to **develop, deploy and run** applications with containers.



## Images and Containers

An **Image** is an executable package that includes everything needed to run an application -

​      1. Source Code

​      2. A runtime

​      3. Libraries

​      4. Environment Variables and Configuration files.. etc

A **Container** is a run time instance of an image. - what the image becomes in memory when executed.

> To find list of running docker containers

```bash
docker ps
```



## Containers and Virtual machines

A **Container** runs natively on Linux and shares the kernel of the host machine. It runs a discrete process which is light weight.

A **Virtual Machine** on the other hand runs a full-blown "**guest**" OS, with virtual access to host resources through **`hypervisor`**.



>  [Install Docker - Ubuntu](https://docs.docker.com/install/linux/docker-ce/ubuntu/#install-docker-ce)



#### Commands

1. Check docker version -

```bash
docker --version
# OR
docker info/version    	# gives detailed info 
```

2. Test Docker installation - 

```bash
docker run hello-world
```

3. List the images that are available on your machine -

```bash
docker image ls
```

4. List the containers which are present in any given state -

```bash
docker container ls --all
```

