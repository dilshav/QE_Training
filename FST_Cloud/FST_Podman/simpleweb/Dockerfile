#Set the base image
FROM docker.io/node:18-alpine

#Set the working directory
WORKDIR /usr/app
#WORKDIR will do following
#mkdir /usr/app -p
#cd /usr/app

#Copy the package.json to the container
COPY ./package.json ./

#Install the dependencies 
RUN npm install

#Copy the remaining files into the container
COPY ./ ./

#Multiple commands to be run
#ENTRYPOINT .sh
#Command to start the Node Server
CMD ["npm","run","start"]