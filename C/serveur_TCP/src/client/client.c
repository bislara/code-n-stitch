#include <stdio.h>
#include <stdlib.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <errno.h>
#include <string.h>
#include "socket_client.h"
#include "global.h"

int main(void)
{
	int fd;
	struct sockaddr_in addr;

	while (1)
	{
		addr = init_socket(&fd);
		connect_socket(fd, &addr);
		manage_socket(fd);
		printf("Do you want to try another connection ? (y/n): ");
		if (fgetc(stdin) == 'n')
			break ;
		fgetc(stdin);
	}
}
