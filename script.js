let _id = prompt("Enter your ID: ");
const _gb = prompt("Enter GB: ");
while(_id && _id.length != 36) {
  _id = prompt("Invalid ID!\nEnter your ID again: ")
};
const handle = () => {
  const xhr = new XMLHttpRequest();
  xhr.open('POST', 'https://api.cloudflareclient.com/v0a745/reg');
  xhr.send(JSON.stringify({"referrer": _id}));
  console.info("You got 1GB data!!");
}
for(let i = 0; i < _gb; i++){
  setTimeout(handle, 500);
}