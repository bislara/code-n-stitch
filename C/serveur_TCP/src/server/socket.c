#include <stdio.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <errno.h>
#include <string.h>
#include <stdlib.h>
#include "socket_server.h"
#include "global.h"

void init_socket(int *fd)
{
	struct sockaddr_in addr;

	addr.sin_family = AF_INET;
	addr.sin_port = htons(PORT);
	addr.sin_addr.s_addr = htonl(IP);
	*fd = socket(AF_INET, SOCK_STREAM, 0);
	bind_s(fd, &addr);
}

void bind_s(int *fd, struct sockaddr_in *addr)
{
	if (bind(*fd, (struct sockaddr *)addr, sizeof(*addr)) == -1)
	{
		printf("Error in bind_s function during bind set-up\n");
		printf("errno code: %d\n", errno);
		printf("errno text: %s\n", strerror(errno));
		exit(EXIT_FAILURE);
	}
	printf("Socket succesfully binded.\n");
	if (listen(*fd, 5) == -1)
	{
		printf("Error un bind_s function during listen set-up\n");
		exit(EXIT_FAILURE);
	}
	printf("Socket is listening.\n");
}

void manage_socket(int clientfd, struct sockaddr_in *client)
{
	char buffer[SIZE];
	char response[SIZE];

	system("clear");
	printf("---New Socket Created !---\n");
	printf("You are in communication with %s\n",\
			inet_ntoa(client->sin_addr));
	write(clientfd, "Hey, I listen you !\n", 20);
	while (1)
	{
		memset(buffer, 0, SIZE);
		memset(response, 0, SIZE);
		if (read(clientfd, buffer, SIZE) <= 0)
			break ;
		printf("Client: %s\n", buffer);
		printf("Response: ");
		fgets(response, SIZE, stdin);
		write(clientfd, response, strlen(response));
	}
	printf("The client closed the session.\n");
	close(clientfd);
}
