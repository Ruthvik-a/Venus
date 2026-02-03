
async function send(){
  const msg = document.getElementById("msg").value;
  if(!msg) return;
  const model = document.getElementById("model").value;
  const provider = document.getElementById("provider").value;
  addMsg("user", msg);

  const res = await fetch("http://localhost:8000/chat",{
    method:"POST",
    headers:{"Content-Type":"application/json"},
    body: JSON.stringify({message:msg, model:model, provider:provider})
  });
  const data = await res.json();
  addMsg("bot", data.reply);
  document.getElementById("msg").value="";
}

function addMsg(role,text){
  const div = document.createElement("div");
  div.className = "msg "+role;
  div.innerText = (role==="user"?"You: ":"AI: ")+text;
  document.getElementById("chat").appendChild(div);
}
