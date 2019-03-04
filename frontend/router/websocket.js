var socket = new WebSocket(
    'ws://' + window.location.host + '/ws/user/icoul'
);

socket.onopen = function (e) {
    console.log('connection complete');
}

socket.onclose = function (e) {
    console.log('connection close');
}

socket.onmessage = function (e) {
    console.log(e.message);
}
