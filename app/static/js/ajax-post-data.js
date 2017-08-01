<script type="text/javascript">

    $('form.ajax').on('submit', function () {

    var that = $(this); // whole form object
    var url = that.attr('action');
    var type = that.attr('method');

    var data = {};
    // data object will be send through jquery method and we need to pass it as a json object
    // json containing name of the field and value of the field

    // find all form fields called name - they contain some data to save to db
    that.find('[name]').each( function(index, value) {
        var thatInsideEach = $(this); // this is this for each elemet of the form containing attr name
        var name = thatInsideEach.attr('name');
        var nameValue = thatInsideEach.val();

        data[name] = nameValue;
    });

    $.ajax({
        url: url,
        type: type,
        data: data,
        success: function(response) {

            // clear form fields now on because success
            that.find('[name]').each( function() {
                $(this).val('');
            });

            // send info about success
            $('div#name-data').empty();
            $('div#name-data').append('Succesuly saved to DB').css('color', 'red');
            console.log(response);
        }
    });

    return false;
    });

    </script>
