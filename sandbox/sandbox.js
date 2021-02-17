// const spinners = document.querySelectorAll('.spinner');
// const $spinnerWrapper = $('#spinner-wrapper');

// for (let spinner of spinners){
//     spinner.addEventListener('click', function(evt){
//         $spinnerWrapper.show();
//     });
// }



// $('#myModal').on('shown.bs.modal', function () {
//     $('#myInput').trigger('focus')
//   })
const $spinnerModal = $('#spinnerModal');

$(window).on('load', function(e) {
    $spinnerModal.modal('show');

    setTimeout(function() {
        $spinnerModal.modal("hide");
      }, 3500);

});