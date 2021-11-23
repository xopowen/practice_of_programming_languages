((D, B, log = (arg) => console.log(arg)) => {
  const dropZone = D.querySelector("div");
  const input = D.querySelector("input");
  let file;

  D.addEventListener("dragover", (ev) => ev.preventDefault());
  D.addEventListener("drop", (ev) => ev.preventDefault());

  dropZone.addEventListener("drop", (ev) => {
    ev.preventDefault();

    log(ev.dataTransfer);

    file = ev.dataTransfer.files[0];

    log(file);

    handleFile(file);
  });


  dropZone.addEventListener("click", () => {
    input.click();
    input.addEventListener("change", () => {
      log(input.files);

      file = input.files[0];

      log(file);

      handleFile(file);
    });
  });

  const handleFile = (file) => {
    dropZone.remove();
    input.remove();


    if (
      file.type === "text/html" ||
      file.type === "text/css" ||
      file.type === "text/javascript"
    )
      return;

    if (file.type === "application/pdf") {
      createIframe(file);
      return;
    }
    log(file)
    const type = file.name.split(".")[1];
    log(type);
    switch (type) {
      case "cow":
        log(createText(file));
        break;
/*
      default:
        B.innerHTML = `<h3>Unknown File Format!</h3>`;
        const timer = setTimeout(() => {
          location.reload();
          clearTimeout(timer);
        }, 2000);*/
        break;
    }
  };

 async function createText(text) {

  let promise = new Promise((resolve, reject) => {

  let file = input.files[0];
  let reader = new FileReader();

  reader.readAsText(file);

  reader.onload = function() {
  resolve(reader.result);
  };

  reader.onerror = function() {
    console.log(reader.error);
  };

  });

  let result_promise = await promise;
  result_promise =  result_promise.split('\n');
  let list_operators = [];
  let result_promise_length = result_promise.length;
  for (let i = 0; i < result_promise_length; i++) {
      let list = result_promise[i].split(' ');
      let len_list = list.length;
      for (let j = 0; j < len_list; j++) {
          if( list[j] != ""){
          list_operators.push(list[j]);
          }
      }
  }


let ind = 0;
var result_list =  new Array(3000).fill(0);

let cycles = get_list_cycles(list_operators);
let comms_list = ["moo", "mOo", "moO", "mOO", "Moo", "MOo", "MoO", "MOO", "OOO", "MMM", "OOM", "oom"];

let register = 0;
let index = 1000;
let i = 0;


while( i < list_operators.length) {

    if (i+'' == ' '){
        continue;
    }

    let  operant = list_operators[i];
    if (operant == "moo"){
         i = cycles[i+''];
         continue;
    }
    else if (operant == "mOo"){
        index++;
    }
    else if (operant == "moO"){
        index--;
    }
    else if (operant == "mOO"){
        if (result_list[index] == 3 || result_list[index] > 11){

            break;
        }
        else{
            list_operators[i] = comms_list[result_list[index]];
        }
    }
    else if( operant == "Moo"){
        log(String.fromCharCode(result_list[index]));
        if (result_list[index] == 0){
             console.log(index);
            log(String.fromCharCode(result_list[index]));
        }
    }
    else if  (operant == "MOo"){

        result_list[index] --;
        }
    else if (operant == "MoO") {

        result_list[index] ++;

    }
    else if( operant == "MOO"){

        if (result_list[index] == 0){
            i = +get_key(cycles, i)+1;
            continue;
            }
    }
    else if (operant == "OOO") {
        result_list[index] = 0;
    }
     else if (operant == "MMM"){
        if (register == 0){
            register = result_list[index];
        }
        else{
            result_list[index] = register;
            }
     }
     else if (operant == "OOM"){
        log(result_list[index]);
     }
     i++;
}
log(result_list);
}





})(document, document.body);


function get_key(dict,value){
    for(key in dict){
        if(dict[key] == value){

            return key;
        }
    }
    return false;
}


function get_list_cycles(list_operators){
    let cucle = {};
    for(let i = 0;i < list_operators.length; i++){

        if(list_operators[i]=="moo"){
            let n = 0;
            while(true){
                if(list_operators[i-n] == "MOO" && get_key(cucle,i-n) == false){
                    cucle[i+''] = i - n;
                    break;
                }else{
                n++;
                }
                };
        };
    }
    return cucle;
}