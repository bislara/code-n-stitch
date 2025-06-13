# Description

This directory correspond of all sources files making the TCP server

# How it work

In Unix world all is considered like a file, a real file, you'r hard drive (sda), special files (like /dev/null), all is a file. (for more precisions you can read [this post.](https://dev.to/eteimz/everything-is-a-file-explained-g2a) 
So a socket too is like a file and we can interact with it like any other file, using [File descriptors.](https://en.wikipedia.org/wiki/File_descriptor)

## Init socket

The first step is to create the file descriptor for the socket (note that we use a pointer because it's his identifier and we want to keep it for read/write/close)
```
*fd = socket(\ // socket is the function in C to create the file descriptor
    AF_INET,\ // AF_INET represent the address family (here IPv4)
    SOCK_STREAM,\ // SOCK_STREAM represent the type (TCP or UDP here it's TCP)
    0); // represent the protocol 0 is used because only protocol is possible with SOCK_STREAM
```
now fd contain a file descriptor to the socket, that's how the socket will be identified by the kernel for our operations.

We also create the address where the server will listen
```
struct sockaddr_in addr;

addr.sin_family = AF_INET; // We specify the address family, the same of the socket
addr.sin_port = htons(PORT); // We use htons to set the bytes of the port in the good order
addr.sin_addr.s_addr = htonl(IP); // htonl is the same as htons but return a long instead of a short
```
see [big_endian](https://en.wikipedia.org/wiki/Endianness) to understand "the good order" of htons

## Bind the socket
Now that we have our socket and our address we want to bind the socket and the address it's going to assign the address to the socket
```
bind(*fd,\ // our file descriptor
    (struct sockaddr *)addr,\ // we cast our addr to (struct sockaddr *) because this is what the function want
    sizeof(*addr)) // we give the size in byte of our address
```

## Listen
Here we have a file descriptor that point to a socket binded with our local address, all is done.
So we can start at listening incoming connections (this is the job of the kernel)
```
listen(*fd\ // our file descriptor
        , 5) // the maximum connection in the queue
```

# Comunnicate in the socket

## Accept connection
Now we can just accept all connections incoming in loop
```
while (1)
	{
	memset(&client, 0, len); // we fill all the client's structure with 0 before accept a new one

	clientfd = accept(\ // the accept function return a new file descriptor that point sepcifically to the connection with our client
                fd,\ // our socket's file descriptor
                (struct sockaddr *)&client,\ client will be filled with all client's info like his IP, etc
                &len); // the len of our client's variable (sizeof(client))
                
	manage_socket(clientfd, &client); // once we accepted the connection we can enter in a loop to discuss with the client
	}
```

## Manage socket
This is a simple function where the server and the client talk each in turn, we read/write in the socket with the file descriptor like in a regular file.


Thanks to read this if I made a mistake please let me know
