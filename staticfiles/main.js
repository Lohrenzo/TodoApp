// var alertBox = document.getElementById("alert-box");
// var form = document.getElementById('post-form');

// const itemName = document.getElementById('id_item_name');
// const itemList = document.getElementById('id_item_list');

// const csrf = document.getElementsByName('csrfmiddlewaretoken');
// const url = "";


// form.addEventListener('submit', e=>{
//     e.preventDefault()
//     // const item_data = itemName.value
//     const form_data = new FormData()
//     form_data.append('csrfmiddlewaretoken', csrf[0].value)
//     form_data.append('itemName', itemName.value)
//     form_data.append('itemList', itemList.value)

//         $.ajax({
//             type: 'POST',
//             url: url,
//             data: form_data,
//             success: function(response){
//                 console.log(response);
//             },
//             error: function(error){
//                 // console.log(error);
//                 alert(error);
//             },
//             cache: false,
//             contentType: false,
//             processData: false,
//         });
// })



var cancel = document.querySelector(".cancel");

function previousPage() {
    window.history.back();
}
cancel.addEventListener("click", previousPage);
















$(document).ready(function(){

    // setInterval(function(){

    //     $.ajax({
    //         type: 'GET',
    //         url: "{% url 'get_items' todo_list.pk %}",
    //         success: function(response){
    //             console.log(response)

    //             // $("#display").empty();
    //             // for (var key in response.list_items) {
    //             //     var temp = "<th>"+response.list_items[key].item_name+"</th>";
    //             //     $("#display").append(temp);
    //             // }
    //         },
    //         error: function(response){
    //             console.log("An Error Occured")
    //         }
    //     });

    // }, 1000);

});

// $(document).on('submit', '#post-form', function(e){
//     e.preventDefault();
    
//     $.ajax({
//             type: 'POST',
//             url: "{% url 'new_item' %}",
//             data: {
//                 item_name: $('#item_name').val(),
//                 // completed: $('#completed').val(),
//                 item_list: $('#item_list').val(),
//                 csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
//             },
//             success: function(data){
//                 alert(data);
//             },
//     });
// });


// // var list = "{{todo_list}}";
// // document.getElementById("item-list").selected = list;
