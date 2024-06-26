import  boto3

#crear cliente para dynamo
dynamodb = boto3.resource('dynamodb' , region_name = 'us-east-1') 

tabla = dynamodb.Table('tabla-yonny-orozco')

#leer un elemento de la tabla
response = tabla.get_item(Key={'id' : '2'})

print(response['Item'])

#leer todos los elementos de la tabla
response = tabla.scan()

print(response['Items'])

#insertar elementos en una tabla
tabla.put_item(Item=item)
{
    "id" : "3",
    "nombre" :"diego",
}




