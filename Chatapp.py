#flask vais ser o framework web para python a ser usado na aplicação
from flask import Flask, render_template
#flask_socketio vai ser a biblioteca usada para podemos usar sockets
from flask_socketio import SocketIO, emit

#instanciando objeto flask
app = Flask(__name__)

app.config[ 'SECRET_KEY' ] = 'asbuicfbeygd837gdwudb'
#instanciando objeto socket
socketio = SocketIO( app )

@app.route( '/' )
def index():
    #template é o html que vai ser renderizado
    return render_template('./ChatAppPage.html')

#função para o recebeminto/maipulação do objeto enviado do cliente em JavaScript
@socketio.on( 'evento' )
def lidando_com_o_evento( json ):
    print( 'Recebido: ' + str( json ) )
    #servidor enviando resposta ao evento que enviou o objeto
    socketio.emit( 'resposta', json )

#função para rodar a aplicação
if __name__ == '__main__':
    socketio.run( app, debug = True )

    