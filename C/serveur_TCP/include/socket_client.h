#ifndef SOCKET_CLIENT_H
#define SOCKET_CLIENT_H

struct sockaddr_in init_socket(int *fd);
struct sockaddr_in init_addr(void);
void connect_socket(int fd, struct sockaddr_in *addr);
void manage_socket(int fd);

#endif
