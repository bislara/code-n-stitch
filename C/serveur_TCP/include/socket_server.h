#ifndef SOCKET_SERVER_H
#define SOCKET_SERVER_H

void init_socket(int *fd);
void bind_s(int *fd, struct sockaddr_in *addr);
void manage_socket(int clientfd, struct sockaddr_in *client);

#endif
