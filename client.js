const net = require('net');
const client = new net.Socket();
const port = 7070;
const host = '127.0.0.1';

client.connect(port, host, function() {
    console.log('Conectado');
    client.write("Ola eu sou o cliente " + client.address().address);
});

client.on('data', function(data) {
    console.log('Eu, cliente : ' + data);
});

/*function menu() {
	var lineRead = readlineSync.question("\n\nEnter option (1-abrir, 2-Enviar, 3-Fechar, 4-Sair): ");
	
	switch (lineRead) {
		case "1":
			console.log("Opcao 1 selecionada");
			break;
		case "2":
			console.log("Opcao 1 selecionada");
			break;
		case "3":
			console.log("Opcao 1 selecionada");
			break;
		case "4":
			console.log("Opcao 1 selecionada"); 
			break;
		default:
			menu();
			break;
	}
}*/

client.on('close', function() {
    console.log('Conexao fechada');
});


