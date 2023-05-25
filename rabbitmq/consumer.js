var amqp = require("amqplib/callback_api");
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

function intensiveOperation(){
  let i = 1e9 * 2
  while(i--){}
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

amqp.connect(rabbitSettings, function (error0, connection) {
  if (error0) {
    throw error0;
  }
  connection.createChannel(async function (error1, channel) {
    if (error1) {
      throw error1;
    }
    const id = process.pid;
    console.log('Queue:  ');
    var queue = await readLineAsync();
    //console.log(`Soy la queue: ${queue}`);
    //console.log(`ID: ${id}`);

    channel.assertQueue(queue, {
      durable: true, //almacena los datos, si hay reinicio los datos no se pierden
    });

    console.log(" [*] Waiting for messages in %s", queue);

    channel.consume(queue, async function(datos) {
      const content = datos.content.toString();

      await intensiveOperation();
      console.log(content);
      channel.ack(datos);
      const data = JSON.parse(content);
      const timeStart = parseFloat(data['timestamp']);
      const timeRecive = parseFloat(new Date().getTime());
      const latency = parseFloat(timeRecive - timeStart) / 1000; //latencia en segundos

      const category = data['category'];
      //console.log('Category:', category);
      //console.log('Latencia:',latency)
      const contenido = latency.toString() + '\n';
      fs.appendFile(category + '3-1-1-3.txt', contenido, (error) => {
          if(error){
            throw error;
          }
      });

    });

  });
});