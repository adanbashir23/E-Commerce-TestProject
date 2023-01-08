// $("#formComment").on("submit", function(e){
//   e.preventDefault();
//   e.stopPropagation();
//   var $this = $(this);
//   var valid = true;
//   $('#formComment textarea').each(function() {
//       let $this = $(this);

//       if(!$this.val()) {
//           valid = false;
//           $this.parents('.validate').find('.mySpan').text('The '+$this.attr('name').replace(/[\_]+/g, ' ')+' field is required');
//       }
//   });

//   if(valid){
//       $(".btnSave").text('Saving....').attr('disabled',true);
//       let data = $this.serialize();
//       //ajax
//       $.ajax({
//           url: $this.attr('action'),
//           type: "POST",
//           data: data,
//           dataType: 'json',
//           success: function(resp){
//               if(resp.message === 'success'){
//                   getComments();
//               }else{
//                   alert(resp.message);
//               }

//               $(".btnSave").text('Save').attr('disabled',false);
//           },
//           error: function(resp){
//               console.log('something went wrong');
//               $(".btnSave").text('Save').attr('disabled',false);
//           }
//       });
//   }
// }
// )

$('#product-review-form').on('submit', function(event){
    event.preventDefault();
    console.log("form submitted!")  // sanity check
    create_comment();
});

function create_comment() {
    $.ajax({
        url : "create_comment/", // the endpoint
        type : "POST", // http method
        data : { the_post : $('#comment-text').val() }, // data sent with the post request

        // handle a successful response
        success : function(json) {
            $('#comment-text').val(''); // remove the value from the input
            console.log(json); // log the returned json to the console
            console.log("success"); // another sanity check
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });




    // console.log('is working')
    // console.log($('comment-text'.val()))
}
