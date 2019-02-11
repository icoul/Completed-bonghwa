var socket = new WebSocket(
    'ws://' + window.location.host + '/ws/user/'
);

socket.onclose = function (e) {
    console.log('connection close');
}
