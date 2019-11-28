CC=gcc
CFLAGS=-Wall -O0
SECFLAGS=-Wl,-z,noexecstack -fstack-protector-all --pie -fPIE -Wl,-z,relro,-z,now
SOURCE=files.c
OUTPUT=files

.PHONY: all clean

all:
	$(CC) $(CFLAGS) $(SECFLAGS) $(SOURCE) -o $(OUTPUT)

clean:
	rm -f $(OUTPUT)
