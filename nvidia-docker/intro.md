Docker is very useful, every programmer knows it. You can even choose how many CPU to allocate to the container by using the `docker run --cpus=<value>` command. Unfortunately, for those who frequently works with machine learning, Docker doesn't support GPU natively. 

The good news is, Nvidia released its own docker called [Nvidia Docker][]. They later even released the Nvidia Container Runtime integration library which more flexible -- it supports Docker Compose, LXC, CRI-O and allows GPU as a first-class resource in Kubernetes and Swarm. 

This tutorial teaches you how to utilize Nvidia Docker to run machine learning on Docker.