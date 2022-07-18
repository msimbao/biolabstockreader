var id=806;
let urlString = window.location.href;
let paramString = urlString.split('?')[1];
let queryString = new URLSearchParams(paramString);
for(let pair of queryString.entries()) {
    console.log("Key is:" + pair[0]);
    console.log("Value is:" + pair[1]);
    id = pair[1] 
}
console.log(id);

$.post( "/test?id=" + id, function( data ) {
$( ".id" ).html( data.id );
$( ".name" ).html( data.name );
$( ".storage" ).html( data.storage.name );
$( ".weight" ).html( data.weight + ' ' + data.weight_unit.name );
});

