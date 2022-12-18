var app = new Vue({
  el: '#app',
  data: {
    message: 'Hello Vue!'
  }
})

var token = ""
var stocksList = []

function loginSubmit(){
    var email = document.getElementById("emailInput").value;
    var password = document.getElementById("passwordInput").value;

    $.post( "/login?email=" + email + "&password=" + password, function( data ) {
        //Grab Authentication
        token = data.token

        //Load Storage after getting Auth Token
        loadBox()
      });
}

function loadBox(){
    var boxId = 37

    $.post( "/loadBox?token=" + token + "&boxId=" + boxId, function( data ) {
        console.log(data)
        stocksList = data.stocks
      });
}

//         var id=866;
//         let urlString = window.location.href;
//         let paramString = urlString.split('?')[1];
//         let queryString = new URLSearchParams(paramString);
//         for(let pair of queryString.entries()) {
//             console.log("Key is:" + pair[0]);
//             console.log("Value is:" + pair[1]);
//             id = pair[1] 
//         }
//         console.log(id);

//         $.post( "/read?id=" + id, function( data ) {
//     $( "#id" ).html( data.id );
//     $( "#name" ).html( data.name );
//     $( "#storage" ).html( data.storage.name );
//     $( "#weight" ).html( data.weight + ' ' + data.units );
//   });

//   function makePUTrequest() {

//         var currentWeight = document.getElementById("weight").innerHTML
//         unit = currentWeight.split(" ")[1]
//         currentWeight = currentWeight.split(" ")[0]  
//         console.log("currentWeight is : " +  currentWeight)
//         // console.log(currentWeight);
//         var e = document.getElementById("addOrSubtract");
//         var addOrSubtract = e.value;

//         var amount = document.getElementById("amount").value;

//         if (addOrSubtract == 0){
//             var leftOverAmount = parseFloat(currentWeight) - parseFloat(amount);
//             console.log("leftOverAmount is : " + leftOverAmount)
//         }else{
//             var leftOverAmount = parseFloat(currentWeight) + parseFloat(amount);
//             console.log("currentWeight is : " + currentWeight)
//             console.log("amount is : " + amount)
//             console.log("leftOverAmount is : " + leftOverAmount)
//         }
        
//         $.ajax({
//             url: '/write?id=' + id + '&amount=' + leftOverAmount,
//             type: 'PUT',
//             success: function (result) {
//                 console.log(result)
//                 swal("Done", "For this stock, there are " + leftOverAmount + " " + unit + " left", "success",{
//                     button: "Aww yeaaahhh!",
//                   })
//                 .then((value) => {
//                     location.reload();
//                   });;
//             }
//         });
//     }
