var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);

app.get('/', function(req, res){
  res.sendFile(__dirname + '/index.html');
});

app.get("/Features/TabooChecker.js", function(req,res){
  res.sendFile(__dirname+'/Features/TabooChecker.js')
});

io.on('connection', function(socket){
  console.log('a user connected');
  socket.on('disconnect', function(){
    console.log('user disconnected');
  });
});

io.on('connection', function(socket){
  socket.on('input', function(text){
    io.emit('input',text);
  });
});

http.listen(3000, function(){
  console.log('listening on *:3000');
});
