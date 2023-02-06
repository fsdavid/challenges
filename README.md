# Challanges
  
Repo is used to store the code challenges.

## Requirements
 `Python`, `Docker` and `Docker Compose` are required to run the tests successfully.

## Start 

Run `sh start.sh` to start all three tasks.

(For Windows please use WSL)

## Details

`start.sh` script runs three sub shell scripts.

1. Basic algorithms - executes python unit test to validate the `get_depth` method, which calculates shortest way between two nodes (Root and any child node) in Directed acyclic graph. 
  `get_depth` method has three input parameters 
    - Graph (stored as a binary matrix)
    - Root node index
    - Node index

    If two nodes are not connected, method returns `-1`

2. Web servers - runs docker command to build and run simple nodejs server container. Server have two input parameters: `PORT=3333` and `BASE_URL=''`. 
On docker run we set parameters `PORT=3000` and `BASE_URL='conabio'` and open port `3000:3000`.

    Node.js server contains two routes `/foo` and `/bar` preceded by`/${BASE_URL}`
    After running docker script, endpoints look like: `localhost:3000/conabio/foo` and `localhost:3000/conabio/bar`

3. Containerization - runs `docker-compose up` command, which builds three containers (`mysql`, `servera` and `serverb`), two networks (`dbnerwork` and `servicenetwork`) and one named volume (`mysql`):

    1. MySql container - is joined to the `dbnerwork` network.
      
       Uses `.env` file to set up database and `mysql` volume (I belive named volumes for relational databases is a good practice). 
       
       Contains `healthcheck`, for the dependent containers.

    2. Server A - runs `debian` image from custom Dockerfile.
    
       `default-mysql-client` and `inetutils-ping` packages are installed for the testing purposes. Container joins both `dbnerwork` nad `servicenetwork` networks.
      
       Before the startup it pings database server and prints `Server A is connected to Database!`
       
       It depends on `mysql` containers health and itself contains `healthcheck` where mysql connection (Using environment variables) is tested. 

    3. Server B - runs `nginx` image from custom Dockerfile.
      
       Regarding the task, we needed to log that Server B is connected to Server A, so to avoid terminating Nginx processes, custom shell script is attached to `docker-entrypoint.d` file which pings `servera` and among other nginx startup logs, prints `Server B is connected to Server A!`.

       It opens bind mount volume and connects local `./src` folder with containers `/usr/share/nginx/html` as a result of which the local `index.html` will be used inside the container.

       Opens port `3001:80` and accordingly returns `index.html` on the `localhost:3001` call.

       Container joins to `servicenetwork` network and depends on `servera` health.
