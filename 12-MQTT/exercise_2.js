var mqtt = require(mqtt);
// Create a client connection
var client = mqtt.connect("mqtt://mqtt.dioty.co:1883", {
username: 'jappiatu@stu.ucc.edu.gh',
password: 'a2375ca4'
})

var topic = '/jappiatu@stu.ucc.edu.gh/DCSIT';

client.on('message', function(topic, message, packet) {
    message = message.toString()
    console.log("Received " + message)
})

client.on('connect', function() { // Check you have a connection
    client.subscribe('/jappiatu@stu.ucc.edu.gh/DCSIT')
})