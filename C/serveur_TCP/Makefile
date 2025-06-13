CC := gcc
CFLAGS := -Wall -Wextra -Werror -g -I include
SOURCE_DIR = src
OBJ_DIR := obj
BIN_DIR := .

SERVER_EXE := $(BIN_DIR)/server
SERVER_SRC := $(wildcard $(SOURCE_DIR)/server/*.c)
SERVER_OBJ := $(patsubst $(SOURCE_DIR)/server/%.c, \
					$(OBJ_DIR)/server/%.o, $(SERVER_SRC))

CLIENT_EXE := $(BIN_DIR)/client
CLIENT_SRC := $(wildcard $(SOURCE_DIR)/client/*.c)
CLIENT_OBJ := $(patsubst $(SOURCE_DIR)/client/%.c, \
			  		$(OBJ_DIR)/client/%.o, $(CLIENT_SRC))

all: $(SERVER_EXE) $(CLIENT_EXE)

# $^ represent all prerequists and $@ represent the target
$(SERVER_EXE): $(SERVER_OBJ)
	$(CC) $^ -o $@

$(OBJ_DIR)/server/%.o: $(SOURCE_DIR)/server/%.c
	$(CC) $(CFLAGS) -c $< -o $@

$(CLIENT_EXE): $(CLIENT_OBJ)
	$(CC) $^ -o $@

$(OBJ_DIR)/client/%.o: $(SOURCE_DIR)/client/%.c
	$(CC) $(CFLAGS) -c $< -o $@ 

clean:
	@-rm $(SERVER_EXE) $(OBJ_DIR)/server/* 2> /dev/null
	@-rm $(CLIENT_EXE) $(OBJ_DIR)/client/* 2> /dev/null
	@echo "clean done !"
