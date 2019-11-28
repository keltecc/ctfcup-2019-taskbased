FROM ubuntu:16.04

RUN apt update && \
    apt install -y socat

RUN mkdir -p /var/task/

ADD flag.txt /tmp/
ADD files /var/task/

RUN chmod 444 /tmp/flag.txt && \
    chmod 111 /var/task/files

USER nobody

ENTRYPOINT ["socat", "TCP-LISTEN:31337,reuseaddr,fork", "EXEC:/var/task/files,pty,echo=0"]
