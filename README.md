# Projeto teste-ml api Facebook


Teste para um job

#
#EXEMPLO DE USO :
#

#Exemplo de envio de dados 
curl --dump-header - -H "Content-Type: application/json" -X POST --data '{"facebookID": "Julinho", "name": "julio", "username": "julim001", "gender": "male"}' http://localhost:8000/person/
Resposta: HTTP 201 


#Exclusão de dados  
curl -i -H "Accept: application/json" -X DELETE http://localhost:8000/person/7/
Resposta: HTTP 204






{
  "name": "Ricardo Kamada",
  "id": "675091159240511"
}



