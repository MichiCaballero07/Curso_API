import request


if __name__ == '__main__':
    '''se genera una variable llamada url y va a almacenar la url'''
    url = 'https://www.google.com.co/'
    '''se ejecuta el metodo get este va a recibir un 
    parametro en string donde le indiquemos la url,
    nos va a retornar un objeto de tipo response
    '''
    response = request.get(url)
    
    print(response)