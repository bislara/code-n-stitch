#include <stdio.h>
#include <stdlib.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <errno.h>
#include <string.h>
#include "socket_server.h"
#include "global.h"

int main(void)
{
	int fd;
	int clientfd;
	socklen_t len;
	struct sockaddr_in client;

	init_socket(&fd);
	len = sizeof(client);
	while (1)
	{
		 memset(&client, 0, len);
		 clientfd = accept(fd, (struct sockaddr *)&client, &len);
		 if (clientfd == -1)
		  printf("Accept failed !\n");
		 manage_socket(clientfd, &client);
		 printf("Wait another connection ? (y/n) ");
		 if (fgetc(stdin) == 'n')
		  break ;
		 fgetc(stdin);
	}
}
