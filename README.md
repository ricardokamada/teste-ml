# Projeto teste-ml api Facebook

Teste para um job

#
Instalar as dependências via 
pip install -r requeriments.txt <br />
Frameworks utilizados : <br />
Django==1.9 <br />
django-filter==0.12.0 <br />
djangorestframework==3.3.2 <br />
facebook-sdk==1.0.0a0 <br />
Markdown==2.6.5 <br />
requests==2.9.1 <br />
wheel==0.26.0 <br />

#Exemplo de envio de dados 
curl --dump-header - -H "Content-Type: application/json" -X POST --data '{"facebookID": "12232344232", "name": "julio", "username": "julim001", "gender": "male"}' http://localhost:8000/person/
Resposta: HTTP 201 


#Exclusão de dados  
curl -i -H "Accept: application/json" -X DELETE http://localhost:8000/person/7/
Resposta: HTTP 204


#Listagem de informações coletadas disponives em:<br />
http://localhost:800/graph<br />
{<br />
      "name": "Ricardo Kamada",<br />
      "id": "675091159240511"<br />
}<br />

