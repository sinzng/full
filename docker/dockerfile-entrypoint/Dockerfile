# Base image
FROM ubuntu:latest 

# nginx install
RUN apt -y update && apt -y upgrade

# server execution
ENTRYPOINT ["top"]
CMD ["-d", "10"]
