## Start locall application


#### Clone project

`git clone git@gitlab.com:stellen-anzeiger/analytics-engine-ng.git`


#### Start with Docker

`docker-compose build`

`docker-compose up`

##### Load fixtures 

`docker-compose run web python manage.py loaddata fixtures/fixture.json`

##### Start working with project

Open your browser and paste to the address-field:

`0.0.0.0:8000` - for browsing
`0.0.0.0:8000/admin` - for admin interface
`0.0.0.0:8000/graphql` - to take actions with GraphQl queries 
