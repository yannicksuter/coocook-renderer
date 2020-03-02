#!/bin/bash
# curl -X POST -F 'title=Barossa Rhubarb & Cinnamon Cake' -F 'origin=http://www.whatkatieate.com/recipes/barossa-rhubarb-cinnamon-cake/' -F "content=`cat ./Barossa_Rhubarb_Cinnamon_Cake.html`" http://localhost:5000/snipped
# curl --data-urlencode content=@Barossa_Rhubarb_Cinnamon_Cake.html -d 'title=Barossa Rhubarb & Cinnamon Cake' -d 'origin=http://www.whatkatieate.com/recipes/barossa-rhubarb-cinnamon-cake/' http://localhost:5000/snipped
# curl -X POST http://localhost:5000/snipped -v --data-urlencode -F content=`cat test.html` -F title="Barossa Rhubarb & Cinnamon Cake" -F origin=http://www.whatkatieate.com/recipes/barossa-rhubarb-cinnamon-cake/
