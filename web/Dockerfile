FROM node:9.4.0

#RUN npm install create-react-app --global && create-react-app 100books
#COPY ./src /100books/src
#COPY ./public /100books/public
#RUN yarn build 100books --production

COPY . .
#RUN npm install
#RUN npm install react-cookie --save
#RUN npm install react-cookie
#RUN yarn build --production
#RUN npm install -g serve

EXPOSE 3000

CMD yarn start



# CD inside of this directory-
# BUILD: $ docker build -t react-docker .
# RUN: $ docker run -it --rm -p 3000:3000 -v `pwd`/public:/public -v `pwd`/src:/src --name react react-docker

# For testing:
# RUN: $ docker run -it --rm -p 3000:3000 --name react-demo react-docker bash
