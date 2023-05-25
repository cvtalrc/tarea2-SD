var amqp = require('amqplib/callback_api');
const readline = require("readline");
const fs = require("fs");

const rabbitSettings = {
  protocol: 'amqp',
  hostname: 'localhost',
  port: 5672,
  username: 'Fer',
  password: 'ferfer',
  vhost: '/',
  authMechanism: ['PLAIN', 'AMQPLAIN', 'EXTERNAL']
}
const readLineAsync = () => {
  const rl = readline.createInterface({
    input: process.stdin
  });
  
  return new Promise((resolve) => {
    rl.prompt();
    rl.on('line', (line) => {
      rl.close();
      resolve(line);
    });
  });
};

function generateRandomString(length) {
  var characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
  var result = '';

  for (var i = 0; i < length; i++) {
    var randomIndex = Math.floor(Math.random() * characters.length);
    result += characters.charAt(randomIndex);
  }

  return result;
}


function generarDatos(id, queue) {
  // Generar los datos según tus necesidades
  const trafico = (Math.random() * ( 94 - 5 ) + 5 );
  const velocidad_promedio = ~~(Math.random() * ( 120 - 20 ) + 20);
  const accidentes = ~~(Math.random() * ( 5 - 0 ) + 1)
  //var data_size = Math.floor(Math.random() * (1000 - 700 + 1)) + 700;
  //var data = generateRandomString(data_size);
  const datos = {
    //'id' : id,
    //'category': queue,
    // 'trafico' : trafico,
    // 'velocidad_promedio' : velocidad_promedio,
    // 'accidentes' : accidentes,
    'timestamp': new Date().getTime(),
    'values': { //'id' : id,
                //'category': queue,
                'velocidad': velocidad_promedio,
                'accidentes': accidentes,
                //'data': data
              },
  
  };
  return JSON.stringify(datos);
}

 function enviarDatos(id) {
  
  amqp.connect(rabbitSettings, function(error0, connection) {
    if (error0) {
        throw error0;
    }
    connection.createChannel(async function(error1, channel) {
        if (error1) {
            throw error1;
        }

        console.log('Queue:  ');
        var queue = await readLineAsync();
        //console.log(`Conectado a ${queue}`);  

        setInterval(async () => {
          const datos = generarDatos(id, queue);
          channel.prefetch(1); //no envía más mensajes si un consumer está procesando el mensaje
          channel.assertQueue(queue, {
            durable: true
          });

          channel.sendToQueue(queue, Buffer.from(datos), {
            persistent: true
          });
          const content = datos.toString();
          console.log(`Enviando:`, content);
          // fs.appendFile('mensajes_enviados.txt', 'Ok\n', (error) => {
          //   if(error){
          //     throw error;
          //   }
          // });
          //console.log(" [x] Sent %s", datos);
        }, 400); // Intervalo de 1 segundo:1000
    });
    setTimeout(function() {
        connection.close();
        process.exit(0);
    }, 10000); //intervalo para cerrar el canal
  });
}

enviarDatos(process.pid);
