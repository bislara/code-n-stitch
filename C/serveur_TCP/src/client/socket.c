#include <stdio.h>
#include <stdlib.h>
#include <sys/socket.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <netinet/in.h>
#include <string.h>
#include "socket_client.h"
#include "global.h"

struct sockaddr_in init_socket(int *fd)
{
	*fd = socket(AF_INET, SOCK_STREAM, 0);
	if (*fd == -1)
	{
		printf("Error in creation of the socket.\n");
		exit(EXIT_FAILURE);
	}
	return (init_addr());
}

struct sockaddr_in init_addr(void)
{
	struct sockaddr_in addr;

	addr.sin_family = AF_INET;
	addr.sin_port = htons(PORT);
	addr.sin_addr.s_addr = htonl(IP);
	return (addr);
}

void connect_socket(int fd, struct sockaddr_in *addr)
{
	if (connect(fd, (struct sockaddr *)addr, sizeof(*addr)) < 0)
	{
		printf("Error in connection to the socket.\n");
		exit(EXIT_FAILURE);
	}
	system("clear");
	printf("You are connected to the server %s !\n",\
			inet_ntoa(addr->sin_addr));
}

void manage_socket(int fd)
{
	char serveur[SIZE];
	char message[SIZE];

	while (1)
	{
		memset(serveur, 0, SIZE);
		memset(message, 0, SIZE);
		read(fd, serveur, SIZE);
		printf("Serveur: %s\n", serveur);
		printf("Message or \"quit\" command: ");
		fgets(message, SIZE, stdin);
		if (strcmp(message, "quit\n") == 0)
			break ;
		write(fd, message, sizeof(message));
	}
	printf("The connection has been closed.\n");
	close(fd);
}
